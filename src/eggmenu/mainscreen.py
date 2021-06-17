"""
Draw happy menus

TODO:
- Out of Bounds capture
- curses type stubbing
"""
import curses
import time
from typing import Tuple


class HorizontalBar:
    """Super powerful docstring"""

    def __init__(self, y: int, x: int, length: int, char: str) -> None:
        """Super powerful docstring"""
        self.char = char
        self.x = x
        self.y = y
        self.move_mod = 1 if length >= 0 else -1
        self.stop = x + length
        self.index = x

    def draw(self) -> Tuple[int, int, str, bool]:
        """Draw"""
        if self.move_mod > 0:
            more = not (self.index > self.stop)
        else:
            more = not (self.index < self.stop)

        return_values = (self.y, self.index, self.char, more)
        if more:
            self.index += self.move_mod
        return return_values


class VerticalBar:
    """Super powerful docstring"""

    def __init__(self, y: int, x: int, height: int, char: str) -> None:
        """Super powerful docstring"""
        self.char = char
        self.x = x
        self.y = y
        self.move_mod = 1 if height >= 0 else -1
        self.stop = y + height
        self.index = y

    def draw(self) -> Tuple[int, int, str, bool]:
        """Draw"""
        if self.move_mod > 0:
            more = not (self.index > self.stop)
        else:
            more = not (self.index < self.stop)

        return_values = (self.index, self.x, self.char, more)
        if more:
            self.index += self.move_mod
        return return_values


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
        draw_horizontal_lines = [
            HorizontalBar(top, left, width, "#"),
            HorizontalBar(top + height, left + width, -(width), "#"),
        ]
        draw_vertical_lies = [
            VerticalBar(top, left, height, "@"),
            VerticalBar(top + height, left + width, -(height), "@"),
        ]

        while True:
            check_set = []
            for hline, vline in zip(draw_horizontal_lines, draw_vertical_lies):
                check_set.append(self._draw_char(*hline.draw()))
                check_set.append(self._draw_char(*vline.draw()))
                self.screen.refresh()
                time.sleep(0.005)

            if not any(check_set):
                break

    def _draw_char(self, y: int, x: int, char: str, flag: bool) -> bool:
        """Super powerful docstring"""
        if flag:
            self.screen.addstr(y, x, char)
        return flag

    def main(self) -> None:
        """Super powerful docstring"""
        self.screen.clear()
        self.screen.addstr(0, 0, "0123456789" * 6)

        self.draw_hor_border("-", 1, 1, 45)
        self.draw_hor_border("-", 13, 1, 45)
        self.draw_ver_border("|", 2, 0, 10)
        self.draw_ver_border("|", 2, 47, 10)

        self.draw_frame(2, 1, 10, 45)

        self.screen.getkey()


def main(screen: curses.window) -> None:  # type: ignore
    """Super powerful docstring"""
    mainscreen = MainScreen(screen)
    mainscreen.main()


if __name__ == "__main__":
    curses.wrapper(main)
