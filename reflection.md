# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
1. The user can schedule tasks such as, walking, feeding, and medication.
2. The user can add pets and store their basic information.
3. The user can view their daily schedules and track completed tasks.

- Briefly describe your initial UML design.
My initial UML design includes four(4) main classes:
Owner, Pet, Task, and Scheduler; Owner class stores information about the pet owner, and manages their pet. The Task class represents activities such as feeding and walking, including their duration, priority, and completion status. The Scheduler class organizes tasks by time, filter tasks, and detects scheduling conflicts. The Pet class stores a list of tasks and basic pet information.
- What classes did you include, and what responsibilities did you assign to each? I made a change to my initial UML design by a due_date attribute to the Task class. I did this so the Scheduler can distinguish tasks scheduled at the same time on different days. This will help the system manage daily and weekly tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
My scheduler considers the scheduled time and due date when organizing the pet care tasks. I decided to use this constraints first because the tasks need to be completed at the correct time and on the correct day. The scheduler also stores the task duration and priority. What is implemented also is the conflict detection to identify tasks scheduled at the same time and date.

.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
One tradeoff my scheduler makes is detecting scheduling conflicts based on tasks having the same starting time and date rather than checking their full duration. I chose this approach because it works for identifying tasks that start at the same time. However, the limitation is that tasks with different starting times may still overlap without being detected. This approach is reasonable for the initial version of PawPal+ because it provides basic conflict detection while keeping the scheduling logic manageable.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used ChatGPT and Claude to assist me with designing, implementing, debugging, and testing my PawPal+ project. AI helped me understand how to structure the Owner, Pet, Task, and Scheduler classes and create a UML diagram. I also used AI to understand Python methods, scheduling algorithms, and pytest testing. The most helpful questions were about fixing Python errors, understanding indentation, and implementing recurring tasks and conflict detection. I reviewed the suggestions and tested the code in VS Code to verify that it worked.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
One moment where I did not follow an AI suggestion exactly was when it recommened me in scheduling conflict detection. AI initially suggested using nested loops to compare tasks, but I used sorting and compared neighboring tasks instead. This approach was more efficient for detecting tasks with the same date and starting time and I verified my implementation by running the program in VS Code and creating a pytest test for two tasks scheduled at the same time. The test passed, confirming that the algorithm worked for that scenario.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?


I test seven important functions of my PawPal+ system. I tested whether tasks could be added to pets and marked as completed. I also tested whether the Scheduler could detect tasks scheduled at the same date and time. For recurring tasks, I verified that daily tasks create another task for the following day, weekly tasks create another task seven days later, and one-time tasks do not repeat. All seven automated tests passed successfully.
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am very confident that my scheduler works correctly for the features I have implemented because all six automated tests passed. I also tested the scheduling logic in the terminal and Streamlit application. However, there are still cases I would test if I had more time, such as empty task lists, multiple tasks scheduled at the same time, and tasks with overlapping durations. I would also test what happens when the same recurring task is marked as completed more than once.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The part of this project I am most satisfied with is developing the scheduling system and connecting it to Streamlit. I was able to implement the Owner, Pet, Task, and Scheduler classes to manage pet care activities.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the Streamlit application by allowing users to edit existing tasks and use the daily planner directly from the interface. I would also improve conflict detection to identify tasks with overlapping durations and use owner preferences when generating schedules.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned about designing systems is creating the UML diagram helped me understand the responsibilities of each class and how they interact with one another and how deeply important it is to design the system before implementing the code. 