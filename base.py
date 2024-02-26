import random
import time
from typing import List, Literal
import sys
import os

import keyboard

from screen import Screen
from window import Window


class Console:
    clear_cmd: Literal['clear', 'cls']

    def __init__(self) -> None:
        self.clear_cmd = 'clear' if sys.platform == 'linux' else 'cls'

    def clear(self) -> None:
        os.system(self.clear_cmd)

    def draw(self, screen: Screen) -> None:
        print(screen.to_text(), flush=True)
    
    def read(self, screen: Screen) -> None:

        if keyboard.is_pressed('Right') and keyboard.is_pressed('alt') and keyboard.is_pressed('Shift'):
            if screen.in_focus:
                # if screen.in_focus.x + screen.in_focus.width + 1 < screen.work_width:
                if screen.in_focus.x + screen.in_focus.width < screen.work_width:
                    screen.in_focus.width += 1
                    screen.in_focus.work_width += 1
            return
        if keyboard.is_pressed('Left') and keyboard.is_pressed('alt') and keyboard.is_pressed('Shift'):
            if screen.in_focus:
                if screen.in_focus.width > 2:
                    screen.in_focus.width -= 1
                    screen.in_focus.work_width -= 1
            return
        if keyboard.is_pressed('Up') and keyboard.is_pressed('alt') and keyboard.is_pressed('Shift'):
            if screen.in_focus:
                if screen.in_focus.height > 4:
                    screen.in_focus.height -= 1
                    screen.in_focus.work_height -= 1
            return
        if keyboard.is_pressed('Down') and keyboard.is_pressed('alt') and keyboard.is_pressed('Shift'):
            if screen.in_focus:
                # if screen.in_focus.y + screen.in_focus.height + 1 < screen.work_height:
                if screen.in_focus.y + screen.in_focus.height < screen.work_height:
                    screen.in_focus.height += 1
                    screen.in_focus.work_height += 1
            return

        if keyboard.is_pressed('Right') and keyboard.is_pressed('alt'):
            if screen.in_focus:
                if screen.in_focus.x + screen.in_focus.width < screen.work_width:
                    screen.in_focus.x += 1
            return
        if keyboard.is_pressed('Left') and keyboard.is_pressed('alt'):
            if screen.in_focus:
                if screen.in_focus.x > 0:
                    screen.in_focus.x -= 1
            return
        if keyboard.is_pressed('Up') and keyboard.is_pressed('alt'):
            if screen.in_focus:
                if screen.in_focus.y > 0:
                    screen.in_focus.y -= 1
            return
        if keyboard.is_pressed('Down') and keyboard.is_pressed('alt'):
            if screen.in_focus:
                if screen.in_focus.y + screen.in_focus.height < screen.work_height:
                    screen.in_focus.y += 1
            return


console = Console()

# while True:
#     console.read()
screen = Screen()
# print(
#     screen.width,
#     screen.height,
#     screen.work_width,
#     screen.work_height
# )
console.clear()
 
screen = Screen()
keyboard.add_hotkey('alt+Tab', screen.focus_next)
keyboard.add_hotkey('alt+q', screen.close_focused)
keyboard.add_hotkey('alt+s', screen.test_spawn)

win1 = Window(
    'HIIIII',
    # '',
    width=30
)
screen.insert(win1)
win2 = Window(
    'HIIIII',
    # '',
    width=30
)
screen.insert(win2)

while True:
    win1.title = f'1#x:{win1.x};y:{win1.y};w:{win1.width};h:{win1.height}'
    win2.title = f'2#x:{win2.x};y:{win2.y};w:{win2.width};h:{win2.height}'
    console.read(screen)
    screen.draw_windows()
    console.draw(screen)
 
    time.sleep(0.01)