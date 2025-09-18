import tkinter as tk
from tkinter import messagebox
import time

# Simulate 5 LEDs for exit path
LED_COUNT = 5
led_labels = []

def trigger_emergency():
    messagebox.showwarning("EMERGENCY!", "Emergency detected! Activating exit lights.")
    for i, led in enumerate(led_labels):
        led.config(bg="green")
        root.update()
        time.sleep(0.3)  # sequential lighting
    # Flashing effect
    for _ in range(3):
        for led in led_labels:
            led.config(bg="red")
        root.update()
        time.sleep(0.2)
        for led in led_labels:
            led.config(bg="green")
        root.update()
        time.sleep(0.2)

# GUI setup
root = tk.Tk()
root.title("IoT Emergency Exit Light Simulator")
root.geometry("400x300")

tk.Label(root, text="Emergency Exit Path Simulation", font=("Arial", 14)).pack(pady=10)

# LED representation
led_frame = tk.Frame(root)
led_frame.pack(pady=20)

for i in range(LED_COUNT):
    led = tk.Label(led_frame, text=f"LED {i+1}", bg="grey", width=10, height=2, relief="raised")
    led.grid(row=0, column=i, padx=5)
    led_labels.append(led)

# Emergency button
emergency_button = tk.Button(root, text="Trigger Emergency", font=("Arial", 14), bg="red", fg="white", command=trigger_emergency)
emergency_button.pack(pady=20)

root.mainloop()
