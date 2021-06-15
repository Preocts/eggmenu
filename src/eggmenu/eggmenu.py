"""
Simple text menu

Author: Preocts
Git   : https://github.com/Preocts/eggmenu
"""
import subprocess  # nosec
import sys
from typing import Any
from typing import Dict


class EggMenu(object):
    """Simple menus"""

    def __init__(self) -> None:
        self._menu_title = "Menu Selections:"
        self._menu_items: Dict[str, Any] = {}
        return

    def set_title(self, title: str) -> None:
        """Sets the title of the menu"""
        self._menu_title = str(title)

    def add_choice(self, label: str, func: object, *args: Any, **kwargs: Any) -> bool:
        """Add a menu option. "Label", function, (args), (kwargs)

        Any arguments or keyword arguments to be run with the function
        should be passed here.
        """
        try:
            self._menu_items[label] = {
                "name": label,
                "function": func,
                "args": args,
                "kwargs": kwargs,
            }
        except Exception:
            return False
        return True

    def del_choice(self, label: str) -> bool:
        """Delete a menu option, "Label" """
        if label not in self._menu_items:
            return False
        del self._menu_items[label]
        return True

    def clear_screen(self) -> None:
        """Clears screen, should work on most systems"""
        if sys.platform in ["linux", "darwin"]:
            subprocess.call("clear", shell=True)  # nosec
        elif sys.platform in ["win32", "cygwin"]:
            subprocess.call("cls", shell=True)  # nosec

    def print_menu(self) -> None:
        """Prints menu"""
        print(self._menu_title)
        for count, label in enumerate(self._menu_items.keys()):
            print(f"\t{count + 1}) {label}")
        return

    def run_command(self, menu_choice: str) -> Any:
        """Runs stored command by menu #"""
        return_value = None
        try:
            count = int(menu_choice)
        except ValueError:
            print("Invalid input, menu options must be integers.")
            return return_value
        options = list(self._menu_items)
        try:
            opt = options[count - 1]
        except IndexError:
            print("Invalid option.")
            return return_value

        if self._menu_items[opt]["args"] and self._menu_items[opt]["kwargs"]:
            return_value = self._menu_items[opt]["function"](
                *self._menu_items[opt]["args"], **self._menu_items[opt]["kwargs"]
            )
        elif self._menu_items[opt]["args"]:
            return_value = self._menu_items[opt]["function"](
                *self._menu_items[opt]["args"]
            )
        elif self._menu_items[opt]["kwargs"]:
            return_value = self._menu_items[opt]["function"](
                **self._menu_items[opt]["kwargs"]
            )
        else:
            return_value = self._menu_items[opt]["function"]()

        return return_value
