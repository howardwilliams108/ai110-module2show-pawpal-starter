
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    # Create a task
    task = Task("Morning Walk", "08:00", 30, "High", "Daily", date(2026, 10, 29))

    # Check that the task starts incomplete
    assert task.completed == False

    # Mark the task as completed
    task.mark_complete()

    # Check that the task is now completed
    assert task.completed == True


def test_task_addition():
    # Create a pet
    pet = Pet("Buddy", "Dog")

    # Create a task
    task = Task("Morning Walk", "08:00", 30, "High", "Daily", date(2026, 10, 29))

    # Check that the pet has no tasks initially
    assert len(pet.tasks) == 0

    # Add the task to the pet
    pet.add_task(task)

    # Check that the pet now has one task
    assert len(pet.tasks) == 1


def test_scheduling_conflict():
    # Create two tasks with the same date and time
    task1 = Task(
        "Walking", "08:00", 30, "High",
        "Once", date(2026, 10, 30)
    )

    task2 = Task(
        "Medication", "08:00", 10, "High",
        "Once", date(2026, 10, 30)
    )

    # Create the scheduler and check for conflicts
    scheduler = Scheduler()
    conflicts = scheduler.detect_conflicts([task1, task2])

    # Verify that one conflicting pair was detected
    assert len(conflicts) == 1
    assert conflicts[0] == (task1, task2)


def test_daily_recurring_task():
    # Create a pet and a daily task
    pet = Pet("Buddy", "Dog")

    task = Task(
        "Morning Walk",
        "08:00",
        30,
        "High",
        "Daily",
        date(2026, 10, 29)
    )

    pet.add_task(task)

    # Complete the task using the scheduler
    scheduler = Scheduler()
    scheduler.mark_task_complete(pet, task)

    # Check the original task is completed
    assert task.completed == True

    # Check that a new task was created
    assert len(pet.tasks) == 2

    # Check the new task's date and completion status
    new_task = pet.tasks[1]
    assert new_task.due_date == date(2026, 10, 30)
    assert new_task.completed == False


def test_weekly_recurring_task():
    # Create a pet and a weekly task
    pet = Pet("Max", "Cat")

    task = Task(
        "Grooming",
        "10:00",
        30,
        "Medium",
        "Weekly",
        date(2026, 10, 29)
    )

    pet.add_task(task)

    # Complete the weekly task
    scheduler = Scheduler()
    scheduler.mark_task_complete(pet, task)

    # Check that the original task is completed
    assert task.completed == True

    # Check that a new task was created
    assert len(pet.tasks) == 2

    # Verify the new task's date and status
    new_task = pet.tasks[1]
    assert new_task.due_date == date(2026, 11, 5)
    assert new_task.completed == False


def test_one_time_task():
    # Create a pet and a one-time task
    pet = Pet("Buddy", "Dog")

    task = Task(
        "Vet Appointment",
        "14:00",
        60,
        "High",
        "Once",
        date(2026, 10, 29)
    )

    pet.add_task(task)

    # Count tasks before completion
    before_count = len(pet.tasks)

    # Complete the task
    scheduler = Scheduler()
    scheduler.mark_task_complete(pet, task)

    # Count tasks after completion
    after_count = len(pet.tasks)

    # Verify the task was completed
    assert task.completed == True

    # Verify no additional task was created
    assert before_count == after_count
    assert len(pet.tasks) == 1


def test_duplicate_completion():
    # Create a pet and daily task
    pet = Pet("Buddy", "Dog")

    task = Task(
        "Morning Walk",
        "08:00",
        30,
        "High",
        "Daily",
        date(2026, 11, 1)
    )

    pet.add_task(task)
    scheduler = Scheduler()

    # Completing the task for the first time
    scheduler.mark_task_complete(pet, task)

    # Check that the next occurrence was created
    assert len(pet.tasks) == 2

    # Try completing the same task again
    scheduler.mark_task_complete(pet, task)

    # Verify no additional task was created
    assert len(pet.tasks) == 2
    assert task.completed == True