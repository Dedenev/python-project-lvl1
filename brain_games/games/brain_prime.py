#!/usr/bin/env python3
"""Prime number game."""
import random

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def generate_question():
    """Generate a random number.

    Returns:
        Return number (int)
    """
    number_size_limiter = 99
    return random.randint(1, number_size_limiter)


def calculate_correct_answer(question):
    """Determine if a number is prime.

    Args:
        question (int): some number

    Returns:
        Return 'yes' or 'no' (str)
    """
    if question == 2:
        return 'yes'
    if question % 2 == 0 or question < 2:
        return 'no'
    for item in range(3, int(question ** 0.5) + 1, 2):  # noqa: WPS110
        if question % item == 0:
            return 'no'
    return 'yes'
