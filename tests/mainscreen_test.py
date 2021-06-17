"""Tests for mainscreen.py"""
# from eggmenu.mainscreen import MainScreen
from eggmenu.mainscreen import MenuBorder


def test_at_end_horizontal() -> None:
    """Check stops horizontally"""
    border = MenuBorder(0, 0, 10, "h", "#")

    assert not border.at_end(), border.stop

    border.index = 10

    assert border.at_end(), border.stop

    border = MenuBorder(0, 9, -10, "h", "#")

    assert not border.at_end(), border.stop

    border.index = -1

    assert border.at_end(), border.stop


def test_at_end_vertical() -> None:
    """Check stops vertically"""
    border = MenuBorder(0, 0, 10, "v", "#")

    assert not border.at_end(), border.stop

    border.index = 10

    assert border.at_end(), border.stop

    border = MenuBorder(9, 0, -10, "v", "#")

    assert not border.at_end(), border.stop

    border.index = -1

    assert border.at_end(), border.stop
