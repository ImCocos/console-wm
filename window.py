from functools import lru_cache
from typing import List


class Window:
    def __init__(
            self,
            title: str,
            width: int = 16,
            height: int = 10,
            x: int = 0,
            y: int = 0,
    ) -> None:
        self.title = title

        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.work_width = width - 2
        self.work_height = height - 4

        self.text_array = self.get_empty_array()

        self.set_title(title)

    def set_title(self, title: str) -> None:
        for x, title_let in enumerate(title[:self.work_width]):
            self.text_array[1][x + 1] = title_let

    # def get_empty_array(self) -> List[List[str]]:
    #     return [
    #         [
    #             ' ' for _ in range(self.width)
    #         ] for _ in range(self.height)
    #     ]

    # @lru_cache
    def get_empty_array(self) -> List[List[str]]:
        return [
            list('+' + '-' * self.work_width + '+'),
            list('|' + ' ' * self.work_width + '|'),
            list('+' + '-' * self.work_width + '+'),
            *([
                '|',
                *(' ' for _ in range(self.work_width)),
                '|'
            ]
            for _ in range(self.work_height)),
            list('+' + '-' * self.work_width + '+')
        ]
    
    def update(self) -> None:
        self.text_array = self.get_empty_array()
        self.set_title(self.title)
