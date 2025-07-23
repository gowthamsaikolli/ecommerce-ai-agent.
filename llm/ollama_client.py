import requests

OLLAMA_HOST = "http://127.0.0.1:3000"
OLLAMA_MODEL = "llama3.2"  # or whatever model name you use

def ask_ollama(prompt: str, system: str = "You are a helpful data analyst."):
    """
    Send a prompt to the Ollama model and return its response.
    """
    url = f"{OLLAMA_HOST}/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "options": {"temperature": 0.3}
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=120)
        response.raise_for_status()
        reply = response.json()
        if "message" in reply and "content" in reply["message"]:
            return reply["message"]["content"].strip()
        elif "messages" in reply and len(reply["messages"]) > 0:
            return reply["messages"][-1]["content"].strip()
        else:
            return "Error: Unexpected model response format."
    except requests.RequestException as e:
        return f"Error communicating with Ollama: {str(e)}"
