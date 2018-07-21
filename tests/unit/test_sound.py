import pytest


def test_import():
    import arcade
    assert 'load' in arcade.load_sound.__name__


@pytest.mark.not_ci
@pytest.mark.parametrize('sound_format', ('wav', 'mp3', 'ogg'))
def test_play_sound(sound_format):
    import arcade
    fn = 'tests/unit/laser1.' + sound_format
    my_sound = arcade.load_sound(fn)
    arcade.play_sound(my_sound)
