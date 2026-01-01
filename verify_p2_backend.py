import requests
import json

BASE_URL = "http://127.0.0.1:800"
USER_ID = "guest_user"
TOKEN = "guest_token" # Using guest bypass for simplicity in testing

def test_backend():
    print("--- Starting Backend Feature Verification ---")
    
    # 1. Test List Tasks (Empty initially)
    print("\n[1] Testing List Tasks...")
    res = requests.get(f"{BASE_URL}/api/{USER_ID}/tasks", headers={"Authorization": f"Bearer {TOKEN}"})
    print(f"Status: {res.status_code}")
    tasks = res.json()
    print(f"Tasks found: {len(tasks)}")

    # 2. Test Create Task
    print("\n[2] Testing Create Task...")
    payload = {"title": "Dummy Verification Task", "description": "Auto-generated test"}
    res = requests.post(
        f"{BASE_URL}/api/{USER_ID}/tasks", 
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    print(f"Status: {res.status_code}")
    if res.status_code == 201:
        new_task = res.json()
        task_id = new_task['id']
        print(f"Created Task ID: {task_id}")
    else:
        print(f"Error: {res.text}")
        return

    # 3. Test Toggle (Complete)
    print("\n[3] Testing Toggle Task...")
    res = requests.patch(
        f"{BASE_URL}/api/{USER_ID}/tasks/{task_id}/complete",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    print(f"Status: {res.status_code}")
    if res.status_code == 200:
        print(f"Task completed state: {res.json()['completed']}")

    # 4. Test Update
    print("\n[4] Testing Update Task...")
    update_payload = {"title": "Updated Dummy Task"}
    res = requests.put(
        f"{BASE_URL}/api/{USER_ID}/tasks/{task_id}",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
        data=json.dumps(update_payload)
    )
    print(f"Status: {res.status_code}")
    if res.status_code == 200:
        print(f"Updated Title: {res.json()['title']}")

    # 5. Test Delete
    print("\n[5] Testing Delete Task...")
    res = requests.delete(
        f"{BASE_URL}/api/{USER_ID}/tasks/{task_id}",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    print(f"Status: {res.status_code}")
    if res.status_code == 200:
        print("Delete confirmed.")

    # 6. Final verification - Should be empty
    print("\n[6] Final List Check...")
    res = requests.get(f"{BASE_URL}/api/{USER_ID}/tasks", headers={"Authorization": f"Bearer {TOKEN}"})
    print(f"Status: {res.status_code}")
    print(f"Final Tasks found: {len(res.json())}")

    print("\n--- Backend Verification Complete ---")

if __name__ == "__main__":
    test_backend()
