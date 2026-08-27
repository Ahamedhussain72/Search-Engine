from flask import Flask, render_template, request, jsonify
import cohere
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Initialize Cohere (replace with your API key or env var)
co = cohere.Client("your api key here")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message.strip():
        return jsonify({'reply': "Please type a message."})

    try:
        response = co.chat(
            model="command-nightly",
            message=user_message,
            temperature=0.8
        )
        reply = response.text
        return jsonify({'reply': reply})
    except Exception as e:
        print("Error:", e)
        return jsonify({'reply': f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
