import pytest


class TestFormatter:

    def test_inside_class(self):
        pass

    @pytest.mark.parametrize('test_id', [1, 2, 3, 4])
    def test_inside_class_parametrize(self, test_id):
        assert (test_id)


def test_outside_of_class():
    pass
