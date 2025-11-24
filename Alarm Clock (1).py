import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    sound_file = r"C:\vs code\Python Projects\coolzone.mp3"
  
    
    pygame.mixer.init()  
    
    alarm_triggered = False 
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time and not alarm_triggered:
            print("Alarm ringing!")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            alarm_triggered = True 
            
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            print("Alarm ended. Press Ctrl+C to exit or set a new alarm.")
        
        time.sleep(10)  

def validate_time_format(alarm_time):
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    while True:
        alarm_time = input("Set alarm time (HH:MM): ")
        if validate_time_format(alarm_time):
            break
        else:
            print("Invalid time format. Please enter time as HH:MM.")
    
    set_alarm(alarm_time)



