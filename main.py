import time

import keyboard

from base import Console
from content import Content
from screen import Screen
from window import Window


console = Console()
console.clear()
 
screen = Screen()

keyboard.add_hotkey('alt+Tab', screen.focus_next)
keyboard.add_hotkey('alt+q', screen.close_focused)
keyboard.add_hotkey('alt+s', screen.test_spawn)
keyboard.add_hotkey('alt+1', screen.scroll_down_content_in_focused)
keyboard.add_hotkey('alt+2', screen.scroll_up_content_in_focused)

win1 = Window(
    'Alt + Tab -> focus next window',
    width=40
)

win2 = Window(
    'Alt + q -> close window',
    width=30,
    x = 80
)

win3 = Window(
    'Alt + s -> spawn window',
    width=30,
    x = 41
)

win4 = Window(
    'Alt + Right/Left/Up/Down -> move window',
    width=60,
    y = 13
)

win5 = Window(
    'Alt + Shift + Right/Left/Up/Down -> resize window',
    width=70,
    y = 30,
)

# screen.spawn(win1)
# screen.spawn(win2)
# screen.spawn(win3)
# screen.spawn(win4)
screen.spawn(win5)

frame_rate: float = 1 / int(input('Frame rate: '))

full_string = '''
# gunciron + nginx easy deploy
Tired from copipasting your configs over and over?

This is great solution for you!

# Installing

```bash
git clone https://github.com/ImCocos/Django-Nginx-Gunicorn-Deploy.git
```

# Deploying

1. ```
    cd Django-Nginx-Gunicorn-Deploy
    sudo python3.11 make.py
    cp config.example.ini sites/<site_name>.ini
    ```
2. Reload shell

3. Fill the config.(store it in Django-Nginx-Gunicorn-Deploy/sites)
    > Required fileds are marked with [*], other aren't necessary.

4. ```
    sitemanager help
    ```

# Dependencies

 - nginx
 - python v3.11
'''
# full_string_len = len(full_string)
# string = ''
# c = 0
win5.content = Content(full_string)
while True:
    win5.title = f'{win5.scroll_value}'
    console.read(screen)
    screen.draw_windows()
    console.draw(screen)

    # win5.content = Content(string)
    # string += full_string[c]
    # if c < full_string_len - 1:
    #     c += 1
    # else:
    #     string += '\n'
    #     c = 0

    time.sleep(frame_rate)
