import pytest
import pyglet


@pytest.fixture
def pyglet_window(mocker):
    yield mocker.patch.object(pyglet.window.Window, "__init__")


@pytest.fixture
def pyglet_clock(mocker):
    yield mocker.patch('pyglet.clock')
