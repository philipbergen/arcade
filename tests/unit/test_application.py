import pyglet
import arcade


def test_import():
    assert "Window" == arcade.Window.__name__


def test_constructs(pyglet_window):
    w = arcade.Window()
    assert "Window" == w.__class__.__name__


def test_initializes_defaults(mocker, pyglet_window):
    mocker.patch.object(pyglet.window.Window, "set_fullscreen")
    mocker.patch.object(arcade.Window, "set_update_rate")
    w = arcade.Window()
    pyglet.window.Window.__init__.assert_called_once_with(
        width=800,
        height=600,
        caption="Arcade Window",
        resizable=False
    )
    pyglet.window.Window.set_fullscreen.assert_called_once_with(False)
    w.set_update_rate.assert_called_once_with(1 / 60)
    assert False is w.invalid


def test_update(mocker, pyglet_window):
    w = arcade.Window()
    assert None is w.on_update(1.1111)


def test_set_update_rate_constructor(pyglet_window, pyglet_clock):
    w = arcade.Window()
    pyglet_clock.unschedule.assert_called_with(w.on_update)
    pyglet_clock.schedule_interval.assert_called_with(w.on_update, 1 / 60)


def test_set_update_rate(pyglet_window, pyglet_clock):
    w = arcade.Window()
    w.set_update_rate(1 / 2)
    pyglet_clock.unschedule.assert_called_with(w.on_update, )
    pyglet_clock.schedule_interval.assert_called_with(w.on_update, 0.5)


def test_on_mouse_motion(pyglet_window):
    w = arcade.Window()
    assert None is w.on_mouse_motion(0, 0, 0, 0)


def test_on_mouse_press(pyglet_window):
    w = arcade.Window()
    assert None is w.on_mouse_press(0, 0, 0, 0)


def test_on_mouse_drag(pyglet_window, mocker):
    w = arcade.Window()
    mocker.patch.object(w, "on_mouse_motion")
    assert None is w.on_mouse_drag(0, 0, 0, 0, 0, 0)
    w.on_mouse_motion.assert_called_once_with(0, 0, 0, 0)


def test_on_mouse_release(pyglet_window):
    w = arcade.Window()
    assert None is w.on_mouse_release(0, 0, 0, 0)


def test_on_mouse_scroll(pyglet_window):
    w = arcade.Window()
    assert None is w.on_mouse_scroll(0, 0, 0, 0)
