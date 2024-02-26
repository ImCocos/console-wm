from typing import List, Literal
import sys
import os

import keyboard

from screen import Screen


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
