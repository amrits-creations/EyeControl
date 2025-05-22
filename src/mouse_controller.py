import pyautogui

class MouseController:
    """
    Controls the system mouse cursor using normalized gaze coordinates and blink events.
    """
    def __init__(self):
        # Get actual screen dimensions
        self.screen_width, self.screen_height = pyautogui.size()

    def move_cursor(self, norm_x: float, norm_y: float):
        """
        Move the mouse cursor to normalized screen coordinates (0.0‒1.0).
        """
        x = norm_x * self.screen_width
        y = norm_y * self.screen_height
        pyautogui.moveTo(x, y)

    def click(self, left_blink: bool, right_blink: bool):
        """
        Perform left or right click based on blink flags.
        """
        if left_blink:
            pyautogui.click(button='left')
        if right_blink:
            pyautogui.click(button='right')

    def process(self, norm_x: float, norm_y: float, left_blink: bool, right_blink: bool):
        """
        Combined operation: move cursor and then handle clicks.
        """
        self.move_cursor(norm_x, norm_y)
        self.click(left_blink, right_blink)
