import curses
import time


class MainScreen:
    def __init__(self, screen: curses.window) -> None:
        self.screen = screen

    def draw_hor_border(
        self, char: str, y: int, x: int, length: int, ms_delay: float = 0.0
    ) -> None:
        """Draw a happy little line rooHappy"""
        move_mod = 1 if length >= 0 else -1
        if not ms_delay:
            self.screen.addstr(y, x, char * length)
        else:
            for idx in range(abs(length)):
                self.screen.addstr(y, x + (move_mod * idx), char)
                self.screen.refresh()
                time.sleep(ms_delay / 1000)
        self.screen.refresh()

    def draw_vert_border(
        self, char: str, y: int, x: int, height: int, ms_delay: float = 0.0
    ) -> None:
        """Draw a fun vertical line rooBirb"""
        move_mod = 1 if height >= 0 else -1
        for idx in range(abs(height)):
            self.screen.addstr(y + (move_mod * idx), x, char)
            self.screen.refresh()
            time.sleep(ms_delay / 1000)

        self.screen.refresh()

    def main(self) -> None:
        """Super powerful docstring"""
        # Clear screen
        self.screen.clear()

        self.screen.addstr("Hello from inside curses")

        self.screen.addstr("General Kenobi")

        self.screen.addstr(2, 0, f"{self.screen.getmaxyx()}")

        self.draw_hor_border("-", 4, 4, 50)
        self.draw_hor_border("+", 5, 4, 50, 10)
        self.draw_hor_border("+", 6, 53, -50, 10)

        self.draw_vert_border("|", 5, 55, 15, 0)
        self.draw_vert_border("|", 5, 56, 15, 10)
        self.draw_vert_border("|", 19, 57, -15, 10)

        self.screen.getkey()


def main(screen: curses.window) -> None:
    """Super powerful docstring"""
    mainscreen = MainScreen(screen)
    mainscreen.main()


if __name__ == "__main__":
    curses.wrapper(main)
