from lib.duplicate import duplicate

def test_duplicate_returns():
    string = 'i'
    assert duplicate(string) == '('

def test_duplicate_two_characters():
    string = 'ii'
    assert duplicate(string) == '))'

def test_duplicate_two_diff_characters():
    string = 'ib'
    assert duplicate(string) == '(('

def test_duplicate_three_char():
    string = 'iib'
    assert duplicate(string) == '))('

def test_duplicate_four_char():
    string = 'iibb'
    assert duplicate(string) == '))))'

def test_duplicate_five_char():
    string = 'iibbc'
    assert duplicate(string) == '))))('

def test_duplicate_six_char():
    string = 'iibbcw'
    assert duplicate(string) == '))))(('

def test_duplicate_three_duplicates():
    string = 'iibbcwi'
    assert duplicate(string) == '))))(()'

def test_duplicate_capital():
    string = 'IibbCwi'
    assert duplicate(string) == '))))(()'

def test_duplicate_three_inrow():
    string = 'IiibbCwi'
    assert duplicate(string) == ')))))(()'
