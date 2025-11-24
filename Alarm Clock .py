import tkinter as tk
import datetime
import time
import threading

alarms = []  # List to store all alarms

def check_alarms():
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")  # Current time
        for a in alarms:
            if a == now:            # If alarm matches current time
                show_popup(a)     
                alarms.remove(a)    # Remove alarm after ringing
                update_list()       
        time.sleep(1)

def show_popup(t):
    p = tk.Toplevel(root)
    p.title("Alarm")
    tk.Label(p, text=f"Alarm: {t}", font=("Arial",14)).pack(pady=10)
    tk.Button(p, text="OK", command=p.destroy).pack(pady=5)

def add_alarm():
    h,m,s = hour.get(), minute.get(), second.get()

    # Check inputs are digits
    if not(h.isdigit() and m.isdigit() and s.isdigit()):
        return

    # Formatting time
    t = f"{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}"
    alarms.append(t)
    update_list()

def delete_alarm():
    sel = box.curselection()
    if sel:
        alarms.pop(sel[0])   # Remove selected alarm
        update_list()

# Refresh the display
def update_list():
    box.delete(0, tk.END)
    for a in alarms:
        box.insert(tk.END, a)
        
root = tk.Tk()
root.title("Alarm Clock")
tk.Label(root, text="Alarm Clock", font=("Arial",16)).pack(pady=10)

# Input fields for HH MM SS
f = tk.Frame(root); f.pack()
hour = tk.Entry(f, width=3); hour.grid(row=0,column=0)
minute = tk.Entry(f, width=3); minute.grid(row=0,column=1)
second = tk.Entry(f, width=3); second.grid(row=0,column=2)

tk.Button(root, text="Add Alarm", command=add_alarm).pack(pady=5)

# Listbox to show alarms
box = tk.Listbox(root, width=20, height=8); box.pack()

tk.Button(root, text="Delete", command=delete_alarm).pack(pady=5)
threading.Thread(target=check_alarms, daemon=True).start()

root.mainloop()
