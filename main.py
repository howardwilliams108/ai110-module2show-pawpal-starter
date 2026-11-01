from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


# Create an owner
owner = Owner("Matthew")

# Create two pets
pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Max", "Cat")

# Add both pets to the owner
owner.add_pet(pet1)
owner.add_pet(pet2)


# Create three pet care tasks
task1 = Task("Morning Walk", "08:00", 30, "High", "Daily", date(2026, 10, 29))
task2 = Task("Breakfast", "09:00", 15, "Medium", "Daily", date(2026, 10, 29))
task3 = Task("Medication", "12:00", 10, "High", "Daily", date(2026, 10, 29))

# Assign tasks to the pets
pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)


# Create the scheduler
scheduler = Scheduler()

# Get all tasks from the owner's pets
all_tasks = owner.get_all_tasks()

# Sort tasks by date and time
sorted_tasks = scheduler.sort_by_time(all_tasks)

print("All tasks for all pets owned:", all_tasks)
print("Sorted tasks by date and time:", sorted_tasks)

# Display today's schedule
print("Today's Schedule")
print("----------------")

for task in sorted_tasks:
    print(f"{task.time} - {task.description} ({task.priority})")


# Filter tasks belonging to Buddy
buddy_tasks = scheduler.filter_by_pet(owner, "Buddy")

print("\nTasks for Buddy:")
print("----------------")

for task in buddy_tasks:
    print(f"{task.time} - {task.description}")
    

# Test daily recurring tasks
print("\nTesting Daily Recurring Tasks")
print("-----------------------------")

# Mark Buddy's morning walk as completed
scheduler.mark_task_complete(pet1, task1)

# Display Buddy's tasks after completion
for task in pet1.tasks:
    print(f"{task.due_date} - {task.description} - Completed: {task.completed}")


# Test weekly recurring tasks
print("\nTesting Weekly Recurring Tasks")
print("-----------------------------")

# Create a weekly grooming task for Max
weekly_task = Task(
    "Grooming",
    "10:00",
    30,
    "Medium",
    "Weekly",
    date(2026, 10, 29)
)

pet2.add_task(weekly_task)

# Complete the weekly task
scheduler.mark_task_complete(pet2, weekly_task)

# Display Max's grooming tasks
for task in pet2.tasks:
    if task.description == "Grooming":
        print(f"{task.due_date} - {task.description} - Completed: {task.completed}")
        

# Test a one-time task
print("\nTesting One-Time Task")
print("-----------------------------")

# Create a one-time vet appointment for Buddy
one_time_task = Task(
    "Vet Appointment",
    "14:00",
    60,
    "High",
    "Once",
    date(2026, 10, 29)
)

pet1.add_task(one_time_task)

# Count tasks before completing
before_count = len(pet1.tasks)

# Complete the one-time task
scheduler.mark_task_complete(pet1, one_time_task)

# Count tasks after completing
after_count = len(pet1.tasks)

print(f"Task: {one_time_task.description}")
print(f"Completed: {one_time_task.completed}")
print(f"Tasks before: {before_count}")
print(f"Tasks after: {after_count}")



# Test scheduling conflicts
print("\nTesting Scheduling Conflicts")
print("-----------------------------")

# Create two tasks scheduled at the same time
conflict_task1 = Task(
    "Walking",
    "08:00",
    30,
    "High",
    "Once",
    date(2026, 10, 30)
)

conflict_task2 = Task(
    "Medication",
    "08:00",
    10,
    "High",
    "Once",
    date(2026, 10, 30)
)

# Detect conflicts between the tasks
conflicts = scheduler.detect_conflicts(
    [conflict_task1, conflict_task2]
)

# Display any scheduling conflicts
for first_task, second_task in conflicts:
    print(
        f"Conflict: {first_task.description} and "
        f"{second_task.description} are both scheduled "
        f"for {first_task.due_date} at {first_task.time}"
    )

