import pytest
from unique_char_counter2.src.unique_char_counter import count_unique_chars

test_valid_cases = [
    ('abcabc', 0),
    ('aabbcc', 0),
    ('abcdef', 6),
    ('aabbccddee', 0),
    ('abcdabcd', 0),
    ('aabbccdd', 0),
]

@pytest.mark.parametrize('data, result', test_valid_cases)
def test_count_unique_chars(data, result):
    assert count_unique_chars(data) == result
