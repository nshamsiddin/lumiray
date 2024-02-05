import keyboard
from lumiray.monitor_brightness_controller import MonitorBrightnessController

# Create an instance of your controller
controller = MonitorBrightnessController()

step = 10

# Function to increase brightness
def increase_brightness():
    current_brightness = controller.get_brightness()[0]
    new_brightness = min(100, current_brightness + step)  # Increase by 10%, max 100%
    controller.set_brightness(new_brightness)
    print(f"Brightness increased to {new_brightness}%")

# Function to decrease brightness
def decrease_brightness():
    current_brightness = controller.get_brightness()[0]
    new_brightness = max(0, current_brightness - step)  # Decrease by 10%, min 0%
    controller.set_brightness(new_brightness)
    print(f"Brightness decreased to {new_brightness}%")

# Bind keys
keyboard.add_hotkey('f2', decrease_brightness)  # Bind F2 key to decrease brightness
keyboard.add_hotkey('f3', increase_brightness)  # Bind F3 key to increase brightness

# Start listening for keypresses
print("Listening for F2 and F3 to control brightness...")
keyboard.wait('esc')  # Use ESC key to exit the program
