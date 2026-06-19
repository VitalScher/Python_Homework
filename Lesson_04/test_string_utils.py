import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("Python", "Python"),
    ("волга", "Волга"),
    ("горький17", "Горький17")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    skypro", "skypro"),
    ("    hello world", "hello world"),
    ("    123", "123"),
    ("    17-23", "17-23")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol", [
    ("SkyPro", "S"),
    ("Hellow, world", ","),
    ("17-23", "7")
])
def test_contains_positive(input_str, input_symbol):
    assert string_utils.contains(input_str, input_symbol) is True

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Hello world", " ", "Helloworld"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("hello", "hello"),
    ("    ", ""),
    ("24 апреля", "24 апреля")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ("SkyPro", "t"),
    ("Hellow, world", "a"),
    ("17-23", "5")
])
def test_contains_negative(input_str, input_symbol):
    assert string_utils.contains(input_str, input_symbol) is False

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("SkyPro", "m", "SkyPro"),
    ("Hello world", "2", "Hello world"),
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
