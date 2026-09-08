import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def generate_response(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()
        return response.json().get("response", "No response generated.")
    except requests.exceptions.ConnectionError:
        return "Ollama is not running. Start Ollama and try again."
    except Exception as error:
        return f"Ollama error: {error}"
