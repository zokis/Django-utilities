# coding: utf-8
from random import choice, getrandbits

CHARS_CHOICES_R = '$#23456qwertasdfgzxcvbQWERTASDF'
CHARS_CHOICES_L = 'GZXCVB789yuiophjknmYUIPHJKLNM&'
CHARS_CHOICES = CHARS_CHOICES_R + CHARS_CHOICES_L


def password_generator(passwordLength=12):
    alternate_hands = bool(getrandbits(1))
    password = []
    if not alternate_hands:
        for i in range(passwordLength):
            password += choice(CHARS_CHOICES)
    else:
        for i in range(passwordLength):
            if i % 2 == 0:
                password.append(choice(CHARS_CHOICES_L))
            else:
                password.append(choice(CHARS_CHOICES_R))
    return ''.join(password)
