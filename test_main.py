import string
from unittest.mock import patch
from main import generate_password

def test_generate_password_length():
    # Test that the password has the desired length
    password_length = 12
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    assert len(password) == password_length

def test_generate_password_lowercase():
    # Test that the password contains at least one lowercase letter
    password_length = 8
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    assert any(char.islower() for char in password)

def test_generate_password_uppercase():
    # Test that the password contains at least one uppercase letter
    password_length = 8
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    assert any(char.isupper() for char in password)

def test_generate_password_digit():
    # Test that the password contains at least one digit
    password_length = 8
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    assert any(char.isdigit() for char in password)

def test_generate_password_symbol():
    # Test that the password contains at least one symbol
    password_length = 8
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    assert any(char in string.punctuation for char in password)

def test_generate_password_common_words():
    # Test that the password does not contain common words
    password_length = 8
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    common_words = ["password", "123456", "qwerty", "letmein", "monkey"]
    assert not any(word in password.lower() for word in common_words)

def test_generate_password_banned_characters():
    # Test that the password does not contain banned characters
    password_length = 8
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    banned_characters = ["'", '"', "\\"]
    assert not any(char in password for char in banned_characters)

def test_generate_password_unique_characters():
    # Test that the password has unique characters
    password_length = 8
    mock_input = lambda _: str(password_length)
    with patch('builtins.input', mock_input):
        password = generate_password(password_length)
    assert len(set(password)) == password_length

if __name__ == '__main__':
    # Call all test cases
    test_generate_password_length()
    test_generate_password_lowercase()
    test_generate_password_uppercase()
    test_generate_password_digit()
    test_generate_password_symbol()
    test_generate_password_common_words()
    test_generate_password_banned_characters()
    test_generate_password_unique_characters()