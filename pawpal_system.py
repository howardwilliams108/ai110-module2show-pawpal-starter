# PawPal+ - Pet Care Management System
# This file contains the main classes for the system.

from dataclasses import dataclass, field
class Owner:
    def __init__(self, name, preferences=None):
        self.name = name
        self.preferences = preferences if preferences is not None else {}
        self.pets = []

    def add_pet(self, pet):
        pass

    def get_all_tasks(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def get_tasks(self):
        pass



@dataclass
class Task:
    description: str
    time: str
    duration: int
    priority: str
    frequency: str
    completed: bool = False

    def mark_complete(self):
        pass


class Scheduler:

    def sort_by_time(self, tasks):
        pass

    def filter_tasks(self, tasks):
        pass

    def detect_conflicts(self, tasks):
        pass
