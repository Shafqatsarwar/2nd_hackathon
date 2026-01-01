import requests
import json

BASE_URL = "http://127.0.0.1:800"
USER_ID = "admin"
TOKEN = "admin_token" 

def test_admin_flow():
    print("--- Starting Admin Backend Verification ---")
    
    # 1. Test List Tasks 
    print(f"\n[1] Testing List Tasks for {USER_ID}...")
    try:
        res = requests.get(f"{BASE_URL}/api/{USER_ID}/tasks", headers={"Authorization": f"Bearer {TOKEN}"})
        print(f"Status: {res.status_code}")
        if res.status_code == 200:
            tasks = res.json()
            print(f"Tasks found: {len(tasks)}")
        else:
            print(f"Error: {res.text}")
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    # 2. Test Create Task
    print(f"\n[2] Testing Create Task for {USER_ID}...")
    payload = {"title": "Admin Vault Task", "description": "Testing admin persistence"}
    res = requests.post(
        f"{BASE_URL}/api/{USER_ID}/tasks", 
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    print(f"Status: {res.status_code}")
    if res.status_code == 201:
        new_task = res.json()
        print(f"Created Task: {new_task['title']} (ID: {new_task['id']})")
    else:
        print(f"Error: {res.text}")

    print("\n--- Admin Verification Complete ---")

if __name__ == "__main__":
    test_admin_flow()
