import pytest

from kharosthi.numbers import KharosthiNumber


def test_create():
    num = KharosthiNumber("𐩃")


def test_cannot_supply_invalid_kharosthi_numbers_to_constructor():
    with pytest.raises(Exception):
        num = KharosthiNumber(1)


def test_create_from_single_representable_int():
    num = KharosthiNumber.from_int(3)
    assert str(num) == "𐩂"

    assert str(KharosthiNumber.from_int(1)) == "𐩀"


int_to_kharosthi = [
    (5, "𐩃𐩀"),
    (6, "𐩃𐩁"),
    (7, "𐩃𐩂"),
    (8, "𐩃𐩃"),
    (9, "𐩃𐩃𐩀"),
    (99, "𐩅𐩅𐩅𐩅𐩄𐩃𐩃𐩀"),
    (1996, "𐩇𐩃𐩃𐩀𐩆𐩅𐩅𐩅𐩅𐩄𐩃𐩁"),
    (9999, "𐩃𐩃𐩀𐩇𐩃𐩃𐩀𐩆𐩅𐩅𐩅𐩅𐩄𐩃𐩃𐩀"),
]


@pytest.mark.parametrize("input, expected", int_to_kharosthi)
def test_create_from_non_mappable_int(input, expected):
    num = KharosthiNumber.from_int(input)

    assert str(num) == expected


@pytest.mark.parametrize("expected, input", int_to_kharosthi)
def test_convert_kharosthi_to_int(input, expected):
    num = KharosthiNumber(input)

    assert int(num) == expected


invalid_kharosthi_representations = ["𐩅𐩅𐩅𐩅𐩅", "𐩃𐩃𐩃𐩆"]


@pytest.mark.parametrize("input", invalid_kharosthi_representations)
def test_invalid_kharosthi_representations(input):
    with pytest.raises(ValueError):
        num = KharosthiNumber(input)


def test_negative_numbers_are_invalid():
    with pytest.raises(ValueError):
        num = KharosthiNumber.from_int(-1)

    with pytest.raises(ValueError):
        num = KharosthiNumber.from_int(5) - KharosthiNumber.from_int(6)


def test_subtraction():
    num = KharosthiNumber.from_int(4) - KharosthiNumber.from_int(2)
    assert num == KharosthiNumber.from_int(2)


def test_zero_is_invalid():
    with pytest.raises(ValueError):
        num = KharosthiNumber.from_int(0)

    with pytest.raises(ValueError):
        num2 = KharosthiNumber.from_int(5) - KharosthiNumber.from_int(5)


def test_negative_results_are_invalid():
    with pytest.raises(ValueError):
        num = KharosthiNumber.from_int(4) - KharosthiNumber.from_int(5)


def test_addition():
    num1 = KharosthiNumber.from_int(150)
    num2 = KharosthiNumber.from_int(3200)

    assert num1 + num2 == KharosthiNumber.from_int(3350)


def test_do_not_allow_numbers_over_9999():
    number = 10_000
    with pytest.raises(ValueError):
        num = KharosthiNumber.from_int(number)

    with pytest.raises(ValueError):
        num1 = KharosthiNumber.from_int(5000) + KharosthiNumber.from_int(5000)


def test_equality_with_non_int_should_not_raise():
    num = KharosthiNumber.from_int(1)
    assert (num == object) is False
