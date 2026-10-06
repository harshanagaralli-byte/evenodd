from even_odd import even_odd


def test_even():
    assert even_odd(10) == "Even"


def test_odd():
    assert even_odd(7) == "Odd"


def test_zero():
    assert even_odd(0) == "Even"


def test_negative():
    assert even_odd(-5) == "Odd"