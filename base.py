from typing import List, Literal

import sys

import os

from image import Image


class Console:
    clear_cmd: Literal['clear', 'cls']

    def __init__(self) -> None:
        self.clear_cmd = 'clear' if sys.platform == 'linux' else 'cls'

    def clear(self) -> None:
        os.system(self.clear_cmd)
    
    def image_to_text(self, image: List[str]) -> str:
        return '\n'.join([string for string in image])

    def draw(self, image: Image) -> None:
        print(image.to_text())


console = Console()
im1 = Image([
    '0000000000000000000',
    '0000000000000000000',
    '0000000000000000000',
    '0000000000000000000',
    '0000000000000000000',
    '0000000000000000000',
])

# console.clear()
im2 = Image(
    [
        f'+--------------+',
        f'| Hello world! |',
        f'+--------------+',
    ]
)

im3 = im1.insert(im2, 1, 1)
console.draw(im3)
