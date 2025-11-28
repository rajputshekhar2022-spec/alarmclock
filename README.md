# Python Alarm Clock VITyarthi Project
# Alarm Clock — Interactive Alarm Management System
The following project is an interactive Alarm Clock Application developed using Python with IPyWidgets and Threading.

It allows users to create, delete, and manage multiple alarms with a clean GUI-based .

## Overview of the project 

The Python Alarm Clock Application provides an interactive alarm management system that helps users set, manage, and delete alarms. The project effectively uses IPyWidgets for building a neat and user-friendly UI and uses Python threading to continuously monitor alarm times in the background without disturbing the user interface.

It allows the user to input time in the format HH:MM:SS, set multiple alarms, list all active alarms, and delete any alarm if desired. A background daemon thread constantly compares the current system time with the stored alarm list and triggers a notification whenever an alarm condition is met.


## Features 
- Major Functional Modules.
  
- Alarm Creation Module.

- Users can enter HH:MM:SS to add new alarms.

- Alarm Monitoring Module

- A background thread checks for scheduled alarms and triggers notifications.

- Alarm Management Module

- Users can view, select, and delete alarms via a dropdown interface.

### Additional Features

- Real-time alarm checking.

- Clean interactive UI using ipywidgets.

- Non-blocking background execution.

- Notification output when alarm time coincides with system time


 ## Technologies Used
- Technologygoal
- Python_CORE programming language
- IPyWidgets\tGUI for input fields & buttons
- Threading	Non-blocking alarm monitoring
- Datetime	Timing comparison and display

## Steps to install and run the project
- Install Python
- Dowload the project
- Run the programme
- Start using the Alram

## Usage Instruction 

Follow these steps to use the Python Alarm Clock Application:

### 1. Enter Alarm Time

- You will see three input fields:

- Hour (0–23)

- Minute (0–59)

- Second (0–59)

- Type the desired alarm time in HH:MM:SS format.

### 2. Add an Alarm

- After entering the time, click “Add Alarm”.

- The alarm will be added to the internal list.

- All active alarms will appear in the dropdown menu.

### 3. View Available Alarms

- Open the "Select Alarm to Delete" dropdown.

- All added alarms will be displayed.

- Helps you track existing alarms.

### 4. Delete an Alarm

- Select any alarm from the dropdown menu.

- Click “Delete Selected Alarm” to remove it.

- The alarm will immediately disappear from the list.

### 5. Alarm Triggering

- Keep the notebook running.

- A background thread continuously checks system time.

- When it matches an alarm time:

- A notification appears in the output box (e.g., “Alarm ringing for 07:30:00!”).

### 6. Add Multiple Alarms

- You can add any number of alarms.

## Result

![image alt]()
















  

- All alarms will trigger independently at their scheduled times.


  
  
