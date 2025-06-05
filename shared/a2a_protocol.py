import requests

def send_message(message: dict):
    try:
        res = requests.post("http://127.0.0.1:8000/a2a", json=message)
        return res.json()["response"]
    except Exception as e:
        return f"Error: {e}"
