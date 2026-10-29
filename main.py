from datetime import date
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

