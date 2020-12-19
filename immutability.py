from typing import List


# Bad example

def get_emails() -> List[str]:
    emails: List[str] = []

    try:
        with open('users.txt', 'r') as file:
            # Now imagine I did something fancy and I changed the emails variable
            emails = ['me@kostakuu.rs']  # This is just mock data
    except Exception:
        # Imagine I logged exception
        pass

    return emails


# Good example

def get_emails_better() -> List[str]:
    try:
        with open('users.txt', 'r') as file:
            # Now imagine I did something fancy and I changed the emails variable
            return ['me@kostakuu.rs']  # This is just mock data
    except Exception:
        # Imagine I logged exception
        pass

    return []
