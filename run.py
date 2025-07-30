# Test file for moving cursor 123
import time
import schedule
import pyautogui
import abc123


# makes proxecution pause for 10 sec

# Perform the desired operations here

timeout_start = time.time()
timeout = 29880


while time.time() < timeout_start + timeout:
    test = 0

    
    pyautogui.moveTo(300, 300, duration=1)

    # moves mouse to 1000, 1000.
    pyautogui.dragRel(1, 0, duration=1)

    # drags mouse 100, 0 relative to its previous position,
    # thus dragging it to 1100, 1000
    pyautogui.dragRel(0, 10, duration=1)
    pyautogui.dragRel(-10, 0, duration=1)
    pyautogui.dragRel(0, -10, duration=1)
    time.sleep(30)
    if test == 2:
        break
    test -= 1
	