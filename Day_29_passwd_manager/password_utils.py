from random import choices, shuffle
from enum import Enum

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PasswordSpec:
    def __init__(self, n_letters: int, n_symbols: int, n_numbers: int):
        self.n_letters = n_letters
        self.n_symbols = n_symbols
        self.n_numbers = n_numbers

class Preset(Enum):
    EASY = PasswordSpec(6, 1, 1)
    MEDIUM = PasswordSpec(8, 2, 2)
    STRONG = PasswordSpec(12, 3, 3)

class PasswordGenerator:
    """
    PasswordGenerator is a utility class for creating random, secure passwords.

    The generator combines characters from three categories:
      - Letters (uppercase and lowercase A–Z)
      - Digits (0–9)
      - Symbols (a configurable set of punctuation characters)

    Methods
    -------
    generate(spec: PasswordSpec) -> str
        Creates a password according to a given PasswordSpec, which defines 
        how many letters, digits, and symbols should be included.

    generate_default() -> str
        Creates a password using a default specification (balanced mix of 
        letters, digits, and symbols). Suitable when no custom spec is needed.

    Notes
    -----
    - Passwords are created by sampling from each character category, then 
      shuffling the result to ensure randomness of order.
    """
    def __init__(self):
        pass
    
    def generate(self, spec:PasswordSpec=Preset.MEDIUM.value) -> str:
        password_l = []

        #generate the needed characters to the spec
        password_l.extend(choices(LETTERS, k = spec.n_letters))
        password_l.extend(choices(SYMBOLS, k = spec.n_symbols))
        password_l.extend(choices(NUMBERS, k = spec.n_numbers))

        #shuffle the characters to make their place random and create the password string
        shuffle(password_l)
        password = "".join(password_l)

        return password