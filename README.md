# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```text
Today's Schedule
----------------
08:00 - Morning Walk (High)
09:00 - Breakfast (Medium)
12:00 - Medication (High)
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:


```text
tests/test_pawpal.py::test_task_completion PASSED
tests/test_pawpal.py::test_task_addition PASSED
tests/test_pawpal.py::test_scheduling_conflict PASSED
tests/test_pawpal.py::test_daily_recurring_task PASSED
tests/test_pawpal.py::test_weekly_recurring_task PASSED
tests/test_pawpal.py::test_one_time_task PASSED
tests/test_pawpal.py::test_duplicate_completion PASSED

7 passed in 0.07s


```

## 📐 Smarter Scheduling



| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `sort_by_time()` | It sorts tasks by due date and scheduled time. |
| Filtering | `filter_tasks()`, `filter_by_pet()` | They filter tasks by completion status or pet name. |
| Conflict handling | `detect_conflicts()` | This detects tasks with the same date and start time. |
| Recurring tasks | `mark_task_complete()` | It creates the next occurrence for daily and weekly tasks; one-time tasks do not repeat. |




## 📸 Demo Walkthrough

1. Run the PawPal+ application using `python -m streamlit run app.py`.
2. Enter the owner's name, pet's name, and species, then click **Add pet**.
3. Select a pet and enter a task description, duration, priority, scheduled time, due date, and frequency.
4. Click **Add task** to assign the task to the selected pet.
5. View the pet's tasks in the table, including completion status.
6. Select an incomplete task and click **Complete task**. Daily and weekly tasks create their next occurrence automatically.
7. Click **Generate schedule** to display the owner's pet care tasks in chronological order.
8. If two tasks have the same due date and starting time, the application displays a scheduling conflict warning.


## Current Limitations

- The Streamlit schedule displays tasks chronologically.
- Users cannot edit existing tasks through the interface.
- The displayed conflict detection currently identifies tasks with matching dates and start times.
- Owner preferences are stored but are not applied to scheduling.
- Task information is stored temporarily in Streamlit session state.


