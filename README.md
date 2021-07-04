# Task-Manager (Introduction)

It is a simple todo application in which a user can add a task with their respective status(completed/pending), and alongside the list of tasks are shown to the user,
later a user can update the status of the task. Also this is a multi user application (i.e.), the user currently logged-in can only see/amanager their tasks.

A. Main-Section(Todo's):- In this section there is a form to fill-in a new task and alongside- there is a table that shows details of all thye tasks user have added till now,
                          user can also change the ststus of the task or delete a task.
                         
B. PEnding Tasks(Upcoming): In this there are those tasks listed with status pending.


# Main Dependencies used

1. Django==3.1.2
2. django-crispy-forms==1.12.0

# How to Run

1. Download the Project

2. Download all the dependencies :- In cmd move to your dir(The dir where you have downloaded the project) and type = " pip install -r requirements.txt " This will download all the dependencies

3. Now, (in cmd) type "python manage.py runserver" to run the project, and the project would be runing you local machine on :- "localhost:8000"
