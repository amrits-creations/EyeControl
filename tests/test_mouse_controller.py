# tests/test_mouse_controller.py

import pyautogui
from src.mouse_controller import MouseController

def test_mouse_controller():
    # Monkey‐patch pyautogui methods to capture calls instead of moving the real cursor.
    orig_moveTo = pyautogui.moveTo
    orig_click = pyautogui.click
    calls = []

    def fake_moveTo(x, y):
        calls.append(('moveTo', x, y))

    def fake_click(button='left'):
        calls.append(('click', button))

    pyautogui.moveTo = fake_moveTo
    pyautogui.click = fake_click

    mc = MouseController()

    # Test move_cursor
    mc.move_cursor(0.5, 0.5)
    # Test click behavior
    mc.click(True, False)   # left blink only
    mc.click(False, True)   # right blink only
    # Test combined process
    mc.process(0.1, 0.2, True, True)

    # Restore original functions
    pyautogui.moveTo = orig_moveTo
    pyautogui.click = orig_click

    # Build expected call list
    sw, sh = mc.screen_width, mc.screen_height
    expected = [
        ('moveTo', sw * 0.5, sh * 0.5),
        ('click', 'left'),
        ('click', 'right'),
        ('moveTo', sw * 0.1, sh * 0.2),
        ('click', 'left'),
        ('click', 'right'),
    ]

    assert calls == expected, f"Expected calls {expected}, but got {calls}"

if __name__ == "__main__":
    test_mouse_controller()
    print("MouseController tests passed.")