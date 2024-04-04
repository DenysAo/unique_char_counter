from collections import Counter
from functools import lru_cache


@lru_cache
def count_unique_chars(input_str: str) -> int:
    unique_count = sum((filter(lambda item: item == 1, Counter(input_str).values())))

    return unique_count
