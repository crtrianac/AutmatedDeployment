#%%
##This funtions will test a password that
#1 is not empty and do not have any spaces
def is_valid_username(username):
    return bool(username and ' ' not in username)

#This will ensure a password that is longer 8 characterers, that has a digit, that has a special character and has at leaqt one number
def is_valid_password(password):
    return bool(
        len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isalpha() for char in password) and
        any(char.isascii() and not char.isalnum() for char in password)
    )
#This will ensure that the email has a @ and a .
def is_valid_email(email):
    return bool('@' in email and '.' in email)

##Test case for the funtions above

#%%
def test_valid_username():
    assert is_valid_username("john_doe")
    assert not is_valid_username("john doe")
    assert not is_valid_username("")


def test_valid_password():
    assert is_valid_password("P@ssw0rd")
    assert not is_valid_password("password")
    assert not is_valid_password("12345678")
    assert not is_valid_password("P@ssw0r")
    assert is_valid_password("P@ssword123")
#%%
def test_valid_email():
    assert is_valid_email("john@example.com")
    assert not is_valid_email("john@com")
    assert not is_valid_email("john@example")
    assert not is_valid_email("john@examplecom")
#%%
