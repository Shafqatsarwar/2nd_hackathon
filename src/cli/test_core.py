from src.cli.main import tasks, add_task, view_tasks, toggle_task, update_task, delete_task
import io
import sys

def mock_input(inputs):
    """Helper to mock multiple inputs."""
    sys.stdin = io.StringIO("\n".join(inputs) + "\n")

def test_full_suite():
    print("=== STARTING PHASE I COMPONENT TESTING ===")
    tasks.clear()

    # 1. Test Add Task
    print("\nTesting: Add Task...")
    mock_input(["Buy Milk", "Whole milk only"])
    add_task()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy Milk"
    assert tasks[0]["id"] == 1
    print("✅ Add Task: Success")

    # 2. Test View Tasks (Output check)
    print("\nTesting: View Tasks...")
    # Redirect stdout to capture print
    captured_output = io.StringIO()
    sys.stdout = captured_output
    view_tasks()
    sys.stdout = sys.__stdout__
    assert "Buy Milk" in captured_output.getvalue()
    print("✅ View Tasks: Success")

    # 3. Test Toggle status
    print("\nTesting: Toggle Status...")
    mock_input(["1"]) # Task ID 1
    toggle_task()
    assert tasks[0]["completed"] is True
    print("✅ Toggle Status: Success")

    # 4. Test Update Task
    print("\nTesting: Update Task...")
    mock_input(["1", "Buy Bread", "White bread"])
    update_task()
    assert tasks[0]["title"] == "Buy Bread"
    assert tasks[0]["description"] == "White bread"
    print("✅ Update Task: Success")

    # 5. Test Delete Task
    print("\nTesting: Delete Task...")
    mock_input(["1"])
    delete_task()
    assert len(tasks) == 0
    print("✅ Delete Task: Success")

    print("\n=== ALL CORE FUNCTIONS PASSED ===")

if __name__ == "__main__":
    try:
        test_full_suite()
    except Exception as e:
        print(f"\n❌ Test Suite Failed: {e}")
        sys.exit(1)
