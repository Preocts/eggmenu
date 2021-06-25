"""Create a titled menu in the center of the screen"""
import curses
from typing import List


class MenuSizeError(Exception):
    ...


class MenuOptionsOverflow(Exception):
    ...


class TitledMenu:
    """Super powerful docstring"""

    def __init__(
        self,
        screen: curses.window,  # type: ignore
        menu_title: str,
        menu_options: List[str],
    ) -> None:
        """Super powerful docstring"""
        self.screen = screen
        self.screen_max_y, self.screen_max_x = self.screen.getmaxyx()
        self.title = menu_title
        self.menu_options = menu_options

        if len(menu_title) > self.screen_max_x:
            raise MenuSizeError("Title too large for the dispaly")
        if len(menu_options) + 6 > self.screen_max_y:
            raise MenuOptionsOverflow("Too many options to fit on the display")

        self.top_y = 2

    def draw(self) -> None:
        """Super powerful docstring"""
        self._draw_row(self.top_y, self.title)

        for idx, row in enumerate(self.menu_options):
            self._draw_row(self.top_y + idx + 2, row)

        self.screen.refresh()

    def _draw_row(self, loc_y: int, value: str) -> None:
        """Super powerful docstring"""
        padding = (self.screen_max_x - len(value)) // 2
        self.screen.addstr(loc_y, padding, value)


def main(screen: curses.window) -> None:  # type: ignore
    """Super powerful docstring"""
    options = [
        "Release the kraken",
        "Go to bed",
        "Stay up late and code",
        "Do thirty push ups",
        "Cookies",
        "Exit",
    ]
    mainmenu = TitledMenu(screen, "This is a superpowerful menu", options)
    mainmenu.draw()
    screen.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
