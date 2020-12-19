# Bad example

def get_logged_in_user_email_or_mock(mock_email: bool = False) -> str:
    if mock_email:
        return 'mock@kostakuu.rs'
    else:
        # Imaging I did something nice and read real email
        return 'me@kostakuu.rs'


# Good example

def get_logged_in_user_email() -> str:
    # Imaging I did something nice and read real email
    return 'me@kostakuu.rs'


def get_mocked_logged_in_user_email() -> str:
    return 'mock@kostakuu.rs'
