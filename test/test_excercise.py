from lib.exercise import *
from unittest.mock import Mock

def test_returns_time_difference():
    fake_get_server_time = Mock()
    response_mock = Mock()
    fake_get_server_time.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1668687754}

    #this was the bit i was finding hard
    timer_mock = Mock()
    timer_mock.time.return_value = 1668687754.875396

    timeerr = TimeError(fake_get_server_time, timer_mock)
    assert timeerr.error() == -0.8753960132598877