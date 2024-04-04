import pytest
import sys
from unique_char_counter2.src.command_line_parser import parser_uniq_chars


test_case = (
    ('--file', 'text.txt', 1),
    ('--string', 'aba', 1),
    ('--string', 'a', 1)
)


@pytest.mark.parametrize('command, data, result', test_case)
def test_count_unique_characters(monkeypatch, command, data, result):
    monkeypatch.setattr(sys, 'argv', ['command_line_parser', command, data])
    assert parser_uniq_chars() == result
