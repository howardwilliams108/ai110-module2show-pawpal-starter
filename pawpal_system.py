# PawPal+ - Pet Care Management System
# This file contains the main classes for the system.

from datetime import date
from dataclasses import dataclass, field
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
        self.completed = True


class Scheduler:

    def sort_by_time(self, tasks):
        # Sort tasks by their scheduled time
        return sorted(tasks, key=lambda task:(task.due_date, task.time))

    def filter_tasks(self, tasks, completed=None):
        # Filter tasks based on their completion status
        if completed is None:
            return tasks

        filtered_tasks = []

        for task in tasks:
            if task.completed == completed:
                filtered_tasks.append(task)

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
