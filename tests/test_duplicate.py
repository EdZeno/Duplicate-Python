from lib.duplicate import duplicate

def test_duplicate_returns():
    string = 'i'
    assert duplicate(string) == '('

def test_duplicate_two_characters():
    string = 'ii'
    assert duplicate(string) == ')'
