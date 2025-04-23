import pytest
from television import Television


def test_init_defaults():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle_on_off():
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)

def test_mute_when_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Volume = 0" in str(tv)

def test_unmute_restores_volume():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()
    assert "Volume = 1" in str(tv)

def test_mute_when_off():
    tv = Television()
    tv.mute()
    assert "Power = False" in str(tv)

def test_unmute_when_off():
    tv = Television()
    tv.mute()
    tv.mute()
    assert "Power = False" in str(tv)

def test_channel_up_when_off():
    tv = Television()
    tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_up_when_on():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)

def test_channel_up_wraps_to_min():
    tv = Television()
    tv.power()
    for _ in range(4):
        tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_down_when_off():
    tv = Television()
    tv.channel_down()
    assert "Channel = 0" in str(tv)

def test_channel_down_when_on():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_down()
    assert "Channel = 0" in str(tv)

def test_channel_down_wraps_to_max():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)

def test_volume_up_when_off():
    tv = Television()
    tv.volume_up()
    assert "Volume = 0" in str(tv)

def test_volume_up_when_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)

def test_volume_up_unmutes_and_increases():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_volume_up_caps_at_max():
    tv = Television()
    tv.power()
    for _ in range(5):
        tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_volume_down_when_off():
    tv = Television()
    tv.volume_down()
    assert "Volume = 0" in str(tv)

def test_volume_down_after_up():
    tv = Television()
    tv.power()
    for _ in range(3):
        tv.volume_up()
    tv.volume_down()
    assert "Volume = 1" in str(tv)
