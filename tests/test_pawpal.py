
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
