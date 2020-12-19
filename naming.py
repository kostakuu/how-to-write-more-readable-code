# Bad examples

a: int = 3
wtxt: str = "Hi, there!"
successful: bool = True


def translation() -> str:
    return "English translation"


# Good examples

number_of_rounds: int = 3
welcome_text: str = "Hi, there!"
is_successful: bool = True


def get_translation() -> str:
    return "English translation"
