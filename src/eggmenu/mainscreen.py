"""
Draw happy menus

TODO:
- Out of Bounds capture
- curses type stubbing

"""
import curses
import time
from typing import Tuple


class MenuBorder:
    """Super powerful docstring"""

    def __init__(self, y: int, x: int, size: int, direction: str, char: str) -> None:
        """Super powerful docstring"""
        self.char = char
        self.x = x
        self.y = y
        self.move_mod = 1 if size >= 0 else -1
        if direction == "h":
            self.stop = x + size
        else:
            self.stop = y + size
        self.index = x if direction == "h" else y
        self.direction = direction

    def draw(self) -> Tuple[int, int, str, bool]:
        """Super powerful docstring"""
        end = self.at_end()

        if self.direction == "h":
            return_values = (self.y, self.index, self.char, end)
        else:
            return_values = (self.index, self.x, self.char, end)

        if not end:
            self.index += self.move_mod
        return return_values

    def at_end(self) -> bool:
        """Super powerful docstring"""
        return self.index >= self.stop if self.move_mod > 0 else self.index <= self.stop


class MainScreen:
    def __init__(self, screen: curses.window) -> None:  # type: ignore
        self.screen = screen

    def draw_hor_border(self, char: str, y: int, x: int, length: int) -> None:
        """Draw a happy little line rooHappy"""
        self.screen.addstr(y, x, char * (length + 1))

    def draw_ver_border(self, char: str, y: int, x: int, height: int) -> None:
        """Draw a fun vertical line rooBirb"""
        for idx in range(abs(height)):
            self.screen.addstr(y + idx, x, char)

    def draw_frame(self, top: int, left: int, height: int, width: int) -> None:
        """Super powerful docstring"""
        draw_lines = [
            MenuBorder(top, left, width, "h", "#"),
            MenuBorder(top + height - 1, left + width - 1, -(width), "h", "#"),
            MenuBorder(top, left, height, "v", "@"),
            MenuBorder(top + height - 1, left + width - 1, -(height), "v", "@"),
        ]

        while True:
            is_done = []
            for line in draw_lines:
                is_done.append(self._draw_char(*line.draw()))
                self.screen.refresh()
                time.sleep(0.005)

            if all(is_done):
                break

    def _draw_char(self, y: int, x: int, char: str, flag: bool) -> bool:
        """Super powerful docstring"""
        if not flag:
            self.screen.addstr(y, x, char)
        return flag

    def main(self) -> None:
        """Super powerful docstring"""
        self.screen.clear()
        self.screen.addstr(0, 0, "0123456789" * 6)

        self.draw_hor_border("-", 1, 1, 45)
        self.draw_hor_border("-", 12, 1, 45)
        self.draw_ver_border("|", 2, 0, 10)
        self.draw_ver_border("|", 2, 46, 10)

        self.draw_frame(2, 1, 10, 45)

        maxy, maxx = self.screen.getmaxyx()

        self.draw_frame(0, 0, maxy - 1, maxx - 1)

        self.screen.getkey()


def main(screen: curses.window) -> None:  # type: ignore
    """Super powerful docstring"""
    mainscreen = MainScreen(screen)
    mainscreen.main()


if __name__ == "__main__":
    curses.wrapper(main)
