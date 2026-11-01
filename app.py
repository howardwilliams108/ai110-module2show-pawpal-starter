import streamlit as st
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# Initialize the owner and scheduler in session state
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Matthew")


# Initialize or refresh the Scheduler
if (
    "scheduler" not in st.session_state
    or not hasattr(st.session_state.scheduler, "mark_task_complete")
):
    st.session_state.scheduler = Scheduler()
# I used ChatGPT to help me with the above code. I asked it to help me initialize the scheduler in session state and it provided the code above. 
# I also asked it to check if the schedulerhas the mark_task_complete method and if not, reinitialize it. It provided the code above for that as well.  


st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Pet Care Management")

# Geting the owner and pet information
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
pet_name = st.text_input("Pet name", value="Buddy")
species = st.selectbox("Species", ["dog", "cat", "other"])

# Add a pet to the owner
if st.button("Add pet"):
    st.session_state.owner.name = owner_name

    pet = Pet(pet_name, species)
    st.session_state.owner.add_pet(pet)

    st.success(f"{pet.name} was added successfully!")


# Display the owner's pets
if st.session_state.owner.pets:
    st.write("Current pets:")

    for pet in st.session_state.owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets added yet.")



st.markdown("### Tasks")


# Select a pet from the owner's stored pets
if st.session_state.owner.pets:
    pet_names = [pet.name for pet in st.session_state.owner.pets]

    selected_pet_name = st.selectbox(
        "Select a pet",
        pet_names
    )

    selected_pet = next(
        pet for pet in st.session_state.owner.pets
        if pet.name == selected_pet_name
    )
else:
    selected_pet = None
    st.info("Please add a pet before scheduling tasks.")


st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    
# Enter the scheduled time, date, and frequency
task_time = st.time_input("Scheduled time")
task_date = st.date_input("Due date", value=date.today())
frequency = st.selectbox(
    "Frequency",
    ["Once", "Daily", "Weekly"]
)


# Add a task to the selected pet, replacing the block below with the scheduling logic once you implement it.
if st.button("Add task"):
    if selected_pet is not None:
        task = Task(
            task_title,
            task_time.strftime("%H:%M"),
            int(duration),
            priority,
            frequency,
            task_date
        )

        selected_pet.add_task(task)
        st.success(f"{task.description} added to {selected_pet.name}!")
    else:
        st.warning("Please add a pet first.")


# I replaced the st.session_state.tasks with tasks assigned to selected pet

# Display tasks assigned to the selected pet
if selected_pet is not None:
    if selected_pet.tasks:
        st.write(f"Current tasks for {selected_pet.name}:")

        # Prepare task information for display
        task_data = []

        for task in selected_pet.tasks:
            task_data.append({
                "Task": task.description,
                "Date": str(task.due_date),
                "Time": task.time,
                "Duration": task.duration,
                "Priority": task.priority,
                "Frequency": task.frequency,
                "Completed": task.completed
            })

        st.table(task_data)

        # Select an incomplete task to complete
        incomplete_tasks = [
            task for task in selected_pet.tasks
            if not task.completed
        ]

        if incomplete_tasks:
            # Select a task using its position in the list
            task_index = st.selectbox(
                "Select a task to complete",
                range(len(incomplete_tasks)),
                format_func=lambda i: (
                    f"{incomplete_tasks[i].description} - "
                    f"{incomplete_tasks[i].due_date} at "
                    f"{incomplete_tasks[i].time}"
                )
            )

            selected_task = incomplete_tasks[task_index]

            if st.button("Complete task"):
                st.session_state.scheduler.mark_task_complete(
                    selected_pet, selected_task
                )
                st.rerun()

    else:
        st.info(f"No tasks assigned to {selected_pet.name} yet.")



st.divider()

st.subheader("Build Schedule")
st.caption("Generate a pet care schedule based on scheduled dates and times.")




# Generate a schedule using the Scheduler class
if st.button("Generate schedule"):
    all_tasks = st.session_state.owner.get_all_tasks()

    if all_tasks:
        sorted_tasks = st.session_state.scheduler.sort_by_time(all_tasks)
        
        
        # Check for scheduling conflicts
        conflicts = st.session_state.scheduler.detect_conflicts(all_tasks)

        if conflicts:
            st.warning("Scheduling conflicts detected!")

            for first_task, second_task in conflicts:
                st.write(
                    f"{first_task.description} and "
                    f"{second_task.description} are both scheduled "
                    f"for {first_task.due_date} at {first_task.time}."
                )
        else:
            st.success("No scheduling conflicts detected.")


        st.subheader("Pet Care Schedule")

        for task in sorted_tasks:
            st.write(
                f"{task.due_date} | {task.time} - "
                f"{task.description} ({task.priority})"
            )
    else:
        st.info("No tasks scheduled yet.")

"""Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""

