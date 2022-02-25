import os
import random
from string import ascii_letters, ascii_lowercase, digits


def get_basename(filename):
    base, ext = os.path.splitext(os.path.basename(filename))
    return base, ext


def generate_random_string(filename, size=10):
    base, ext = get_basename(filename)
    random_str = "".join(random.choice(ascii_letters.join(digits)) for i in range(size))

    return f"{base}{random_str}{ext}"
