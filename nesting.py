from typing import List


# Bad example

def get_emails() -> List[str]:
    try:
        with open('users.txt', 'r') as file:
            # Now imagine I did something fancy and I changed the emails variable
            return ['me@kostakuu.rs']  # This is just mock data
    except Exception:
        # Imagine I logged exception
        pass

    return []


# Good example

def try_to_read_emails() -> List[str]:
    try:
        return get_emails_better()
    except Exception:
        # Imagine I logged exception
        pass

    return []


def get_emails_better() -> List[str]:
    with open('users.txt', 'r') as file:
        # Now imagine I did something fancy and I changed the emails variable
        return ['me@kostakuu.rs']  # This is just mock data
