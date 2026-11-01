# PawPal+ - Pet Care Management System
# This file contains the main classes for the system.

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta


class Owner:
    def __init__(self, name, preferences=None):
        self.name = name
        self.preferences = preferences if preferences is not None else {}
        self.pets = []

    def add_pet(self, pet):
        # Add a pet to the owner's list of pets
        self.pets.append(pet)

    def get_all_tasks(self):
        # Get all tasks for all pets owned by this owner
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        # Add a new task to this pet's task list
        self.tasks.append(task)

    def get_tasks(self):
        # Return all tasks for this pet
        return self.tasks


@dataclass
class Task:
    description: str
    time: str
    duration: int
    priority: str
    frequency: str
    due_date: date
    completed: bool = False

    def mark_complete(self):
        # Mark this task as completed
        self.completed = True


class Scheduler:
    def sort_by_time(self, tasks):
        # Sort tasks by their scheduled date and time
        return sorted(tasks, key=lambda task: (task.due_date, task.time))

    def filter_tasks(self, tasks, completed=None):
        # Filter tasks based on their completion status
        if completed is None:
            return tasks

        filtered_tasks = []

        for task in tasks:
            if task.completed == completed:
                filtered_tasks.append(task)

        return filtered_tasks

    def filter_by_pet(self, owner, pet_name):
        # Return tasks belonging to the selected pet
        filtered_tasks = []

        for pet in owner.pets:
            if pet.name == pet_name:
                filtered_tasks.extend(pet.tasks)

        return filtered_tasks

    def detect_conflicts(self, tasks):
        # Detect scheduling conflicts among tasks
        conflicts = []
        sorted_tasks = self.sort_by_time(tasks)

        for i in range(len(sorted_tasks) - 1):
            current_task = sorted_tasks[i]
            next_task = sorted_tasks[i + 1]

            if current_task.due_date == next_task.due_date and current_task.time == next_task.time:
                conflicts.append((current_task, next_task))

        return conflicts

    def mark_task_complete(self, pet, task):
        # Skip tasks that are already completed
        if task.completed:
            return

        # Mark the current task as completed
        task.mark_complete()

        # Create the next task if it repeats
        if task.frequency.lower() == "daily":
            next_date = task.due_date + timedelta(days=1)
        elif task.frequency.lower() == "weekly":
            next_date = task.due_date + timedelta(days=7)
        else:
            return

        # Create a new task for the next occurrence
        next_task = Task(
            task.description,
            task.time,
            task.duration,
            task.priority,
            task.frequency,
            next_date
        )

        pet.add_task(next_task)

    def generate_daily_plan(self, owner, plan_date, available_minutes):
        # Get incomplete tasks scheduled for the selected date
        tasks = []

        for pet in owner.pets:
            for task in pet.tasks:
                if task.due_date == plan_date and not task.completed:
                    tasks.append((pet, task))

        # Assign numeric values to task priorities
        priorities = {"high": 1, "medium": 2, "low": 3}

        # Sort tasks by priority first, then time
        tasks.sort(
            key=lambda item: (
                priorities.get(item[1].priority.lower(), 4),
                item[1].time
            )
        )

        selected_tasks = []
        skipped_tasks = []
        remaining_time = available_minutes

        for pet, task in tasks:
            # Check if the task fits the remaining time
            if task.duration > remaining_time:
                skipped_tasks.append((pet, task, "Not enough available time"))
                continue

            # Calculate the starting time of the task
            start = datetime.combine(
                task.due_date,
                datetime.strptime(task.time, "%H:%M").time()
            )

            # Calculate when the task ends
            end = start + timedelta(minutes=task.duration)

            conflict_found = False

            # Compare with tasks already selected
            for _, selected_task, _ in selected_tasks:
                selected_start = datetime.combine(
                    selected_task.due_date,
                    datetime.strptime(selected_task.time, "%H:%M").time()
                )
                selected_end = selected_start + timedelta(minutes=selected_task.duration)

                # Check whether the time intervals overlap
                if start < selected_end and end > selected_start:
                    conflict_found = True
                    break

            if conflict_found:
                skipped_tasks.append((pet, task, "Overlaps another scheduled task"))
            else:
                selected_tasks.append(
                    (pet, task, "Selected based on priority and available time")
                )
                remaining_time -= task.duration

        return selected_tasks, skipped_tasks
