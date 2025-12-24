import requests
import json

BASE_URL = "http://127.0.0.1:800"

def test_agent_consult():
    print("--- Testing Agent Consult Endpoint ---")
    
    payload = {
        "query": "Fix the critical login bug asap",
        "context": "task"
    }
    
    try:
        res = requests.post(f"{BASE_URL}/api/agent/consult", json=payload)
        print(f"Status: {res.status_code}")
        if res.status_code == 200:
            print("Agent Response:")
            print(json.dumps(res.json(), indent=2))
        else:
            print(f"Error: {res.text}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_agent_consult()
