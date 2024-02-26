from functools import lru_cache
from typing import List

import os

from window import Window


class Screen:
    def __init__(self, width: None | int = None, height: None | int = None) -> None:
        res = os.get_terminal_size()
        lines, columns = res.lines - 1, res.columns

        self.width = width or columns
        self.height = height or lines

        self.work_width = self.width - 2
        self.work_height = self.height - 2

        self.text_array = self.get_empty_array()

        self.windows: List[Window] = []

        # self.in_focus: None | Window
        self.__in_focus: int = 0
    
    @property
    def in_focus(self) -> None | Window:
        if self.windows:
            return self.windows[-1]
    
    def focus_next(self) -> None:
        if self.windows:
            w = self.windows.pop(0)
            self.windows.append(w)
    
    def close_focused(self) -> None:
        if self.in_focus:
            self.windows.pop(-1)
            self.focus_next()
    
    def test_spawn(self) -> None:
        win = Window('Test')
        self.insert(win)

    
    def to_text(self) -> str:
        return '\n'.join(
            [
                ''.join(
                    [
                        let for let in string
                    ]
                ) for string in self.text_array
            ]
        )
    
    # @lru_cache
    def get_empty_array(self) -> List[List[str]]:
        return [
            list('+' + '-' * self.work_width + '+'),
            *([
                '|',
                *(' ' for _ in range(self.work_width)),
                '|'
            ]
            for _ in range(self.work_height)),
            list('+' + '-' * self.work_width + '+')
        ]

    def draw_windows(self) -> None:
        self.text_array = self.get_empty_array()
        for window in self.windows:
            window.update()
            for text_y, string in enumerate(window.text_array):
                for text_x, let in enumerate(string):
                    self.text_array[window.y + text_y + 1][window.x + text_x + 1] = let
    
    def insert(self, window: Window) -> None:
        self.windows.append(window)
