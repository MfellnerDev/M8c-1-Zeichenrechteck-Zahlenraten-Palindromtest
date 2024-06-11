
def ist_palindrom(text):
    text = text.lower().replace(' ', '')
    return text == text[::-1]

def ist_satzpalindrom(satz):
    filtered_satz = ''.join(filter(str.isalnum, satz)).lower()
    return ist_palindrom(filtered_satz)

def test_palindrom_functions():
    assert ist_palindrom("Otto")
    assert not ist_palindrom("Hello")
    assert ist_satzpalindrom("Regine, wette weniger!")
    assert not ist_satzpalindrom("This is not a palindrome")
    print("All tests passed.")

if __name__ == "__main__":
    test_palindrom_functions()
