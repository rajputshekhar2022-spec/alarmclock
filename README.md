Python Alarm Clock with Pygame

This is a simple, command-line-based alarm clock script written in Python that allows the user to set an alarm time (HH:MM). When the current time matches the set time, it plays a specified MP3 file using the pygame library.

Features

Time Validation: Ensures the alarm time is entered in the correct HH:MM format.

Audio Playback: Uses pygame.mixer to load and play an MP3 sound file when the alarm is triggered.

Non-Blocking: Checks the time every 10 seconds to minimize CPU usage while waiting for the alarm time.

Multiple Alarms: After an alarm triggers and the sound finishes, the user is prompted to set a new alarm without restarting the script.

Prerequisites

To run this script, you must have Python installed, along with the required libraries.

1. Python Libraries

You can install the necessary libraries using pip:

pip install pygame


2. Alarm Sound File

The script currently points to a specific path for the alarm sound. You must change this path in the set_alarm function to point to your desired MP3 file.

In the file, update this line:

sound_file = r"C:\vs code\Python Projects\coolzone.mp3" 


To point to your actual file, for example:

sound_file = r"/path/to/your/custom/alarm.mp3"


(Note: If you are on Linux/macOS, remove the r prefix for raw string if your path doesn't contain backslashes.)

How to Run

Save the code: Save the corrected Python code as alarm_clock.py.

Run from terminal: Execute the script using Python:

python alarm_clock.py


Set the time: The script will prompt you to enter the alarm time in 24-hour format (HH:MM).

Set alarm time (HH:MM): 14:30
Alarm set for 14:30.


Alarm Trigger: When the system clock reaches 14:30, the alarm sound will play until the audio file finishes.

New Alarm: Once the alarm cycle is complete, the program will automatically prompt you to set the next alarm time.

Code Structure

set_alarm(alarm_time)

This is the main function that runs the infinite loop, comparing the current time (datetime.datetime.now().strftime("%H:%M")) against the user-defined alarm_time. It handles the initialization of the pygame mixer, loads the MP3, and plays the music.

validate_time_format(alarm_time)

A utility function that uses datetime.datetime.strptime to check if the input string strictly matches the "%H:%MM" format.
