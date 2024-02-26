from typing import Any, Callable, List, Self


class ToTextConverter:
    def from_array(self, array: List[List[str]]) -> str:
        return '\n'.join(
            [
                ''.join(
                    [
                        let for let in string
                    ]
                ) for string in array
            ]
        )


class Image:
    def __init__(self, text: List[str] | List[List[str]], verify_rect: bool = True) -> None:
        self.text_array = self.arraify(text)
        if verify_rect:
            self.verify_rect()

        self.height = len(self.text_array)
        self.width = len(self.text_array[0])
    
    def arraify(self, text: List[str] | List[List[str]]) -> List[List[str]]:
        return [
            [
                let for let in string
            ]
            for string in text
        ]

    def verify_rect(self) -> None:
        first_len = len(self.text_array[0])
        if not all([
            len(string) == first_len
            for string in self.text_array
        ]):
            raise ValueError(f'Image is not rect!')

    def to_text(self) -> str:
        converter = ToTextConverter()
        return converter.from_array(self.text_array)

    def insert(self, im2: Self, image_x: int, image_y: int) -> Self:
        text_array = self.text_array
        for y, string in enumerate(im2.text_array):
            for x, let in enumerate(string):
                text_array[image_y+y][image_x+x] = let
        return self.__class__(text=text_array)
