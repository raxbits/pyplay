import pytest

class TestME():
    def test_basic(self):
        state = True
        name = 'checker'
        assert state, 'c' in name
