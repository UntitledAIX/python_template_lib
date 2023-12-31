import redirect_path as redirect_path
from lib_module import mul, divide


class TestLibModule:
    def test_mul(self):
        assert mul(1, 2) == 2

    def test_div(self):
        assert divide(3, 1) == 3
