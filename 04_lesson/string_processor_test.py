from string_processor import StringProcessor
import pytest

proc = StringProcessor()


@pytest.mark.parametrize('text, result', [
    ('текст', 'Текст.'),
    ('Текст', 'Текст.'),
    ('Текст.', 'Текст.'),
    ('  ', '  .'),
    (1, '.'),
    (None, '.'),
])
def test_first_string(text, result):
    process = proc.process(text)
    assert process == result
