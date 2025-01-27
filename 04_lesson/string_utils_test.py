from string_utils import StringUtils
import pytest

utils = StringUtils()


# CAPITILIZE
@pytest.mark.positive_test
@pytest.mark.parametrize('text, result', [
    ('текст', 'Текст'),
    ('Текст', 'Текст'),
    ('1текст', '1текст'),
    (' текст', ' текст'),
])
def test_positive_utils_first_string(text, result):
    util = utils.capitilize(text)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, result', [
    ('', ''),
    (' ', ' '),
    ('привет мир', 'Привет мир'),
    (' текст', ' текст'),
])
def test_negative_utils_first_string(text, result):
    util = utils.capitilize(text)
    assert util == result


# не понял как объединить с предыдущим негативным тестом
@pytest.mark.negative_test
@pytest.mark.parametrize('text', [
    1,
    None,
])
def test_exception_negative_utils_first_string(text):
    with pytest.raises(Exception) as exc_info:
        utils.capitilize(text)
    assert "has no attribute" in str(exc_info.value)


# TRIM
@pytest.mark.positive_test
@pytest.mark.parametrize('text, result', [
    (' текст', 'текст'),
    ('текст', 'текст'),
    ('текст  ', 'текст  '),
    ('  текст  ', 'текст  '),
])
def test_positive_utils_trim(text, result):
    util = utils.trim(text)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, result', [
    ('', ''),
    (' ', ''),
])
def test_negative_utils_trim(text, result):
    util = utils.trim(text)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text', [
    1,
    None,
    [],
])
def test_exception_negative_utils_trim(text):
    with pytest.raises(Exception) as exc_info:
        utils.trim(text)
    assert "has no attribute" in str(exc_info.value)


# TO_LIST
@pytest.mark.positive_test
@pytest.mark.parametrize('text, separator, result', [
    ('1:2:3', ':', ['1', '2', '3']),
    ('1ж2ж3', 'ж', ['1', '2', '3']),
    ('абв-абв-абв', '-', ['абв', 'абв', 'абв']),
    ('1 2 3', ' ', ['1', '2', '3']),
])
def test_positive_utils_to_list(text, separator, result):
    util = utils.to_list(text, separator)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, separator, result', [
    ('', '', []),
    ('    ', ' ', []),
])
def test_negative_utils_to_list(text, separator, result):
    util = utils.to_list(text, separator)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, separator', [
    (None, ''),
    (123, ' '),
])
def test_exception_utils_to_list(text, separator):
    with pytest.raises(Exception) as exc_info:
        utils.trim(text)
    assert "has no attribute" in str(exc_info.value)


# CONTAINS
@pytest.mark.positive_test
@pytest.mark.parametrize('text, symb, result', [
    ('Текст', 'е', True),
    ('Текст', 'у', False),
    ('Текст ', ' ', True),
    ('Текст', 'ек', True),
])
def test_positive_utils_contains(text, symb, result):
    util = utils.contains(text, symb)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symb, result', [
    ('', '', True),
    (' ', '', True),
])
def test_negative_utils_contains(text, symb, result):
    util = utils.contains(text, symb)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symb', [
    (None, ''),
    (123, ''),
    (True, '')
])
def test_exception_utils_contains(text, symb):
    with pytest.raises(Exception) as exc_info:
        utils.contains(text, symb)
    assert "has no attribute" in str(exc_info.value)


# DELETE_SYMBOL
@pytest.mark.positive_test
@pytest.mark.parametrize('text, symbol, result', [
    ('Текст', 'е', 'Ткст'),
    ('Текст1', '1', 'Текст'),
    ('ТеААААААкст', 'А', 'Текст'),
    ('У Текст', 'У ', 'Текст'),
])
def test_positive_utils_delete(text, symbol, result):
    util = utils.delete_symbol(text, symbol)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symbol, result', [
    ('', '', ''),
    ('   ', ' ', ''),
])
def test_negative_utils_delete(text, symbol, result):
    util = utils.delete_symbol(text, symbol)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symbol', [
    (None, 'a'),
    (123, 'a'),
    (True, 'a')
])
def test_exception_utils_delete(text, symbol):
    with pytest.raises(Exception) as exc_info:
        utils.contains(text, symbol)
    assert "has no attribute" in str(exc_info.value)


# STARTS_WITH
@pytest.mark.positive_test
@pytest.mark.parametrize('text, symb, result', [
    ('Текст', 'Т', True),
    ('Текст', 'т', False),
    ('текст', 'т', True),
    (' Текст', ' ', True),
])
def test_positive_utils_start(text, symb, result):
    util = utils.starts_with(text, symb)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symb, result', [
    ('', '', True),
    (' ', ' ', True),
])
def test_negative_utils_start(text, symb, result):
    util = utils.starts_with(text, symb)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symbol', [
    (None, 'a'),
    (123, 'a'),
    (True, 'a')
])
def test_exception_utils_start(text, symbol):
    with pytest.raises(Exception) as exc_info:
        utils.starts_with(text, symbol)
    assert "has no attribute" in str(exc_info.value)


# END_WITH
@pytest.mark.positive_test
@pytest.mark.parametrize('text, symb, result', [
    ('Текст', 'т', True),
    ('Текст', 'Т', False),
    ('Текст ', ' ', True),
    ('Текст', ' ', False),
])
def test_positive_utils_end(text, symb, result):
    util = utils.end_with(text, symb)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symb, result', [
    ('', '', True),
    ('   ', ' ', True),
])
def test_negative_utils_end(text, symb, result):
    util = utils.end_with(text, symb)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, symbol', [
    (None, 'a'),
    (123, 'a'),
    (True, 'a')
])
def test_exception_utils_end(text, symbol):
    with pytest.raises(Exception) as exc_info:
        utils.starts_with(text, symbol)
    assert "has no attribute" in str(exc_info.value)


# IS_EMPTY
@pytest.mark.positive_test
@pytest.mark.parametrize('text, result', [
    ('', True),
    ('т', False),
    (' ', True),
])
def test_positive_utils_empty(text, result):
    util = utils.is_empty(text)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text', [
    None,
    123,
    True,
])
def test_exception_utils_empty(text):
    with pytest.raises(Exception) as exc_info:
        utils.is_empty(text)
    assert "has no attribute" in str(exc_info.value)


# LIST_TO_STRING
@pytest.mark.positive_test
@pytest.mark.parametrize('text, separator, result', [
    (['1', '2', '3'], ':', '1:2:3'),
    (['1', '2', '3'], '-', '1-2-3'),
    (['а', 'аа', 'ааа'], '-а-', 'а-а-аа-а-ааа'),
    (['1', '2', '3'], '', '123'),
])
def test_positive_utils_to_string(text, separator, result):
    util = utils.list_to_string(text, separator)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text, separator, result', [
    ([], '', ''),
    ('aaaaa', '', 'aaaaa'),
])
def test_negative_utils_to_string(text, separator, result):
    util = utils.list_to_string(text, separator)
    assert util == result


@pytest.mark.negative_test
@pytest.mark.parametrize('text', [
    None,
    123,
    True,
])
def test_exception_utils_empty(text):
    with pytest.raises(Exception) as exc_info:
        utils.list_to_string(text)
    assert "has no" in str(exc_info.value)