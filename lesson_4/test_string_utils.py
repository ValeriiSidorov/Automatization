import pytest
from string_utils import StringUtils

stringutils = StringUtils()

# CAPITALIZED


@pytest.mark.parametrize("str , result",
                         [("valerii", "Valerii"), ("валерий", "Валерий"),
                          ("123", "123"), ("валерий sidorov", "Валерий sidorov")])
def test_capitalize_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(str)
    assert res == result


@pytest.mark.parametrize("str , result",
                         [("11valerii", "11valerii"), ("@валерий", "@валерий"), (" ", " "), ("", "")])
def test_capitalize_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(str)
    assert res == result


def test_capitalize_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

# TRIM


@pytest.mark.parametrize("str , result",
                         [(" valerii", "valerii"), (" валерий", "валерий"), (" 123", "123"),
                          (" валерий sidorov", "валерий sidorov")])
def test_trim_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.trim(str)
    assert res == result


@pytest.mark.parametrize("str , result",
                         [("valerii sidorov", "valerii sidorov"), ("валерий сидоров", "валерий сидоров"),
                          (" валерий ", "валерий "), (" ", ""), ("", "")])
def test_trim_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.trim(str)
    assert res == result


def test_trim_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.trim(None)

# TO_LIST


@pytest.mark.parametrize("str , delimeter, result",
                         [("a_b_c_d", "_", ["a", "b", "c", "d"]), ("1_2_3_4", "_", ["1", "2", "3", "4"]),
                          ("а_б_в_г", "_", ["а", "б", "в", "г"]), ("a b c d", " ", ["a", "b", "c", "d"])])
def test_to_list_delimeter_positive(str, delimeter, result):
    stringutils = StringUtils()
    res = stringutils.to_list(str, delimeter)
    assert res == result


@pytest.mark.parametrize("str , result",
                         [("a,b,c,d", ["a", "b", "c", "d"]), ("1,2,3,4", ["1", "2", "3", "4"]),
                          ("а,б,в,г", ["а", "б", "в", "г"]), ("a,b,c d", ["a", "b", "c d"])])
def test_to_list_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.to_list(str)
    assert res == result


@pytest.mark.parametrize("str , result",
                         [("abcd", ["abcd"]), ("1234", ["1234"]),
                          ("абвг", ["абвг"]), ("abc d", [
                              "abc d"]), (" ", []), ("", []),
                          (" , , , , ", [" ", " ", " ", " ", " "])])
def test_to_list_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.to_list(str)
    assert res == result


def test_to_list_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.to_list(None)


# CONTAINS

@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "i", True), ("12345", "4", True),
                          ("Валерий", "л", True), ("123Валерий 1123", "В", True),
                          ("Валерий Сидоров", " ",
                           True), ("Валерий_Сидоров", "Валерий", True),
                          ("", "", True), (" ", " ", True)])
def test_contains_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.contains(str, symbol)
    assert res == result


@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "S", False), ("12345", "0", False),
                          ("Валерий", "F", False), ("123Валерий1123", "4", False),
                          ("Валерий_Сидоров", " ", False), ("", " ", False)])
def test_contains_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.contains(str, symbol)
    assert res == result


def test_contains_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contain(None)

# DELETE_SYMBOL


@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "i", "Valer"), ("12345", "4", "1235"),
                          ("Валерий", "л", "Ваерий"), ("123Валерий 1123",
                                                       "В", "123алерий 1123"),
                          ("Валерий Сидоров", " ", "ВалерийСидоров"), ("Валерий_Сидоров", "Валерий", "_Сидоров")])
def test_delete_symbol_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(str, symbol)
    assert res == result


@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "S", "Valerii"), ("12345", "0", "12345"),
                          ("Валерий", "О", "Валерий"), ("123Валерий 1123",
                                                        "Z", "123Валерий 1123"),
                             ("ВалерийСидоров", " ", "ВалерийСидоров"), (
                                 "Валерий_Сидоров", "Иван", "Валерий_Сидоров"),
                             ("", " ", ""), (" ", "", " ")])
def test_delete_symbol_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(str, symbol)
    assert res == result


def test_delete_symbol_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, None)


# STARTS_WITH

@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "V", True), ("12345", "1", True),
                          ("Валерий", "В", True), ("123Валерий 1123", "1", True),
                          (" Валерий Сидоров", " ", True),
                          ("", "", True), (" ", " ", True)])
def test_starts_with_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.starts_with(str, symbol)
    assert res == result


@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "S", False), ("12345", "0", False),
                          ("Валерий", "F", False), ("123Валерий1123", "4", False),
                          ("Валерий_Сидоров", " ", False), ("", " ", False)])
def test_starts_with_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.starts_with(str, symbol)
    assert res == result


def test_starts_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.starts_with(None, None)

# END_WITH


@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "i", True), ("12345", "5", True),
                          ("Валерий", "й", True), ("123Валерий 1123", "3", True),
                          ("Валерий Сидоров ", " ", True),
                          ("", "", True), (" ", " ", True)])
def test_end_with_positive(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.end_with(str, symbol)
    assert res == result


@pytest.mark.parametrize("str , symbol, result",
                         [("Valerii", "S", False), ("12345", "0", False),
                          ("Валерий", "F", False), ("123Валерий1123", "4", False),
                          ("Валерий_Сидоров", " ", False), ("", " ", False)])
def test_end_with_negative(str, symbol, result):
    stringutils = StringUtils()
    res = stringutils.end_with(str, symbol)
    assert res == result


def test_end_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.end_with(None, None)

# IS_EMPTY


@pytest.mark.parametrize("str , result", [("", True), ("          ", True)])
def test_is_empty_positive(str, result):
    stringutils = StringUtils()
    res = stringutils.is_empty(str)
    assert res == result


@pytest.mark.parametrize("str , result",
                         [("valerii sidorov", False), ("валерий сидоров", False),
                          (" валерий ", False), ("!@#$%^&*", False),  ("\n\t\r ", False)])
def test_is_empty_negative(str, result):
    stringutils = StringUtils()
    res = stringutils.is_empty(str)
    assert res == result


def test_is_empty_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.is_empty(None)

# LIST_TO_STRING


@pytest.mark.parametrize("list , result",
                         [(["a", "b", "c", "d"], "a, b, c, d"), (["1", "2", "3", "4"], "1, 2, 3, 4"),
                          (["а", "б", "в", "г"], "а, б, в, г"), (["a", "b", "c d"], "a, b, c d")])
def test_list_to_string_positive(list, result):
    stringutils = StringUtils()
    res = stringutils.list_to_string(list)
    assert res == result


@pytest.mark.parametrize("list , joiner, result",
                         [(["a", "b", "c", "d"], "_", "a_b_c_d"), (["1", "2", "3", "4"], "_", "1_2_3_4"),
                          (["а", "б", "в", "г"], "_", "а_б_в_г"), (["a", "b", "c", "d"], " ", "a b c d")])
def test_list_to_string_joiner_positive(list, joiner, result):
    stringutils = StringUtils()
    res = stringutils.list_to_string(list, joiner)
    assert res == result


@pytest.mark.parametrize("list , result",
                         [(["abcd"], "abcd"), (["1234"], "1234"),
                          (["абвг"], "абвг"), (["abc d"], "abc d"),
                          ([" "], " "), ([], ""),
                          ([" ", " ", " ", " ", " "], " ,  ,  ,  ,  ")])
def test_list_to_string_negative(list, result):
    stringutils = StringUtils()
    res = stringutils.list_to_string(list)
    assert res == result


def test_list_to_string_with_none():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.list_to_string(None)
