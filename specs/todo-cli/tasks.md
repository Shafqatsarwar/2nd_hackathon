# Tasks: Phase I Core Features

### Task 1: Main Menu & Exit
- Build a loop that captures user numeric choice.
- Choice '6' exits the program gracefully.

### Task 2: Add Task Logic
- Prompt for Title.
- Prompt for Description.
- Save `{"id": len(tasks)+1, "title": title, "description": desc, "completed": False}`.

### Task 3: View Tasks Logic
- Iterate `tasks` list.
- Format output: `[ID] [Status] Title: Description`.

### Task 4: Update Task Logic
- Input ID.
- Verify ID exists.
- Prompt for new details; update the dictionary.

### Task 5: Delete Task Logic
- Input ID.
- Remove from list if found.

### Task 6: Toggle Status Logic
- Input ID.
- `task["completed"] = not task["completed"]`.
