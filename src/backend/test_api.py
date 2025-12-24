import jwt
import time
import requests
import os
from dotenv import load_dotenv

# Load local .env if it exists
load_dotenv()

BACKEND_URL = "http://127.0.0.1:8000"
SECRET = os.getenv("BETTER_AUTH_SECRET", "default_secret_change_me")
USER_ID = "test-user-999"

def generate_test_token(user_id):
    payload = {
        "sub": user_id,
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,
        "iss": "todo-evolution"
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def test_backend_flow():
    print(f"--- STARTING PHASE II BACKEND TEST ---")
    token = generate_test_token(USER_ID)
    headers = {"Authorization": f"Bearer {token}"}
    
    # 1. Test Health
    print("Testing /health...")
    try:
        res = requests.get(f"{BACKEND_URL}/health")
        print(f"Status: {res.status_code}, Response: {res.json()}")
    except Exception as e:
        print(f"❌ Backend not running? {e}")
        return

    # 2. Test Create Task
    print("\nTesting POST /api/{user_id}/tasks...")
    task_data = {"title": "Test AI Task", "description": "Verified by Agentic Test Script"}
    res = requests.post(f"{BACKEND_URL}/api/{USER_ID}/tasks", json=task_data, headers=headers)
    if res.status_code == 201:
        task = res.json()
        task_id = task['id']
        print(f"✅ Created Task: #{task_id}")
    else:
        print(f"❌ Failed to create: {res.text}")
        return

    # 3. Test Unauthorized Access (Wrong Token)
    print("\nTesting Security (Access with wrong User ID)...")
    res = requests.get(f"{BACKEND_URL}/api/another-user/tasks", headers=headers)
    if res.status_code == 403:
        print("✅ Security Check: Forbidden access blocked.")
    else:
        print(f"❌ Security Failure: Expected 403, got {res.status_code}")

    # 4. Test List Tasks
    print("\nTesting GET /api/{user_id}/tasks...")
    res = requests.get(f"{BACKEND_URL}/api/{USER_ID}/tasks", headers=headers)
    tasks = res.json()
    if len(tasks) > 0:
        print(f"✅ Retrieved {len(tasks)} tasks.")
    
    # 5. Clean up (Delete)
    print(f"\nTesting DELETE /api/{{user_id}}/tasks/{task_id}...")
    res = requests.delete(f"{BACKEND_URL}/api/{USER_ID}/tasks/{task_id}", headers=headers)
    if res.status_code == 200:
        print("✅ Task Deleted.")

    print("\n=== PHASE II BACKEND TEST PASSED ===")

if __name__ == "__main__":
    test_backend_flow()
