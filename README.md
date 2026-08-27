# Smart Semantic Search Engine

A simple web-based chatbot built with Flask and Cohere. Users can send messages through a clean browser interface and receive AI-generated responses from the Cohere language model.

## Features

- Responsive chat interface
- Real-time message exchange without page reloads
- Typing indicator while the response is generated
- Cohere-powered conversational responses
- Empty-message validation and connection error handling

## Tech Stack

- Python
- Flask
- Cohere API
- HTML, CSS, and vanilla JavaScript

## Project Structure

```text
chatbot/
├── app.py                 # Flask application and chat API
├── templates/
│   └── home.html          # Chat interface
└── README.md
```

## Requirements

- Python 3.9 or later
- A [Cohere API key](https://dashboard.cohere.com/api-keys)

## Installation

1. Clone the repository and open the project directory:

	```bash
	git clone <your-repository-url>
	cd chatbot
	```

2. Create and activate a virtual environment:

	**Windows PowerShell**

	```powershell
	python -m venv chatbot
	.\chatbot\Scripts\Activate.ps1
	```

	**macOS/Linux**

	```bash
	python3 -m venv chatbot
	source chatbot/bin/activate
	```

3. Install the dependencies:

	```bash
	pip install flask cohere
	```

4. In `app.py`, replace the placeholder value in `cohere.Client(...)` with your Cohere API key.

	Do not commit a real API key to GitHub. For a public repository, load the key from an environment variable before deploying the application.

## Run Locally

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## API

### `POST /chat`

Send a JSON request:

```json
{
  "message": "Hello!"
}
```

The response contains the chatbot reply:

```json
{
  "reply": "Hello! How can I help you?"
}
```

## Notes

- The application currently runs with Flask's debug mode enabled for local development.
- The Cohere model is configured as `command-nightly` in `app.py`.
- Add production configuration, authentication, rate limiting, and secure secret management before deploying publicly.

## License

This project is available for personal and educational use. Add a license file if you plan to distribute it publicly.
