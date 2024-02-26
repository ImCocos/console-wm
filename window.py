from typing import List

from content import Content


class Window:
    def __init__(
            self,
            title: str,
            width: int = 16,
            height: int = 10,
            x: int = 0,
            y: int = 0,
            content: None | Content = None,
    ) -> None:
        self.scroll_value = 0

        self.title = title

        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.work_width = width - 2
        self.work_height = height - 4

        self.frame_up = '-'
        self.frame_right = '|'

        self.text_array = self.get_empty_array()

        self.set_title(title)

        self.content: None | Content = content


    def set_title(self, title: str) -> None:
        for x, title_let in enumerate(title[:self.work_width]):
            self.text_array[1][x + 1] = title_let
    
    def insert_content(self, content: Content) -> None:
        for y, string in enumerate(content.text_array[:self.work_height]):
            for x, let in enumerate(string[:self.work_width]):
                self.text_array[y + 3][x + 1] = let

    def get_empty_array(self) -> List[List[str]]:
        return [
            list('+' + self.frame_up * self.work_width + '+'),
            list(self.frame_right + ' ' * self.work_width + self.frame_right),
            list('+' + self.frame_up * self.work_width + '+'),
            *([
                self.frame_right,
                *(' ' for _ in range(self.work_width)),
                self.frame_right
            ]
            for _ in range(self.work_height)),
            list('+' + self.frame_up * self.work_width + '+')
        ]
    
    def update(self) -> None:
        self.text_array = self.get_empty_array()
        if self.content:
            self.insert_content(Content(self.content.text_array[self.scroll_value:]))
        self.set_title(self.title)
