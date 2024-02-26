import time

import keyboard

from base import Console
from screen import Screen
from window import Window


console = Console()
console.clear()
 
screen = Screen()

keyboard.add_hotkey('alt+Tab', screen.focus_next)
keyboard.add_hotkey('alt+q', screen.close_focused)
keyboard.add_hotkey('alt+s', screen.test_spawn)

win1 = Window(
    'Alt + Tab -> focus next window',
    # '',
    width=40
)
screen.insert(win1)
win2 = Window(
    'Alt + q -> close window',
    # '',
    width=30,
    x = 80
)
screen.insert(win2)
win3 = Window(
    'Alt + s -> spawn window',
    # '',
    width=30,
    x = 41
)
screen.insert(win3)
win4 = Window(
    'Alt + Right/Left/Up/Down -> move window',
    # '',
    width=60,
    y = 13
)
screen.insert(win4)
win5 = Window(
    'Alt + Shift + Right/Left/Up/Down -> resize window',
    # '',
    width=70,
    y = 30
)
screen.insert(win5)


while True:
    console.read(screen)
    screen.draw_windows()
    console.draw(screen)

    time.sleep(0.01)
