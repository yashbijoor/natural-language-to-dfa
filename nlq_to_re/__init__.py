__all__=['nlq_to_re']

from .extractChars import extract_chars
from .createRegex import construct_regex


def nlq_to_re(charset, nlq):
    char_dictionary = extract_chars(nlq)
    regex = construct_regex(charset, char_dictionary)
    return regex, char_dictionary