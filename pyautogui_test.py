# Serch for pyautogui
import PyAutoGUI


distance = 200

while distance > 0:
        PyAutoGUI.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        PyAutoGUI.drag(0, distance, duration=0.5)   # move down
        PyAutoGUI.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        PyAutoGUI.drag(0, -distance, duration=0.5)  # move up
