from scratch.part1 import get_score

def test_multiple_matches():
    assert get_score("card1: 12 23 34 | 23 34 45") == 2

def test_one_match():
    assert get_score("card2: 12 23 34 | 34 56 78") == 1

def test_no_matches():
    assert get_score("card3: 100 23 34 | 45 56 78 100") == 1

def test_all_matches():
    assert get_score("card4: 12 23 34 | 12 23 34") == 4

def test_empty_scratched_numbers():
    assert get_score("card5: | 12 23 34") == 0

def test_empty_winning_numbers():
    assert get_score("card6: 12 23 34 | ") == 0
