"""
This module contains lists and mappings of symbols and their type.
"""
from enum import Enum

import regex as re

# Vowels (without accent)
short_vowels = ['a', 'e', 'o']
long_vowels = ['ā', 'ē', 'ō']
vowels = short_vowels + long_vowels
semivowels = ['i', 'u']

# Consonants
nasals = ['m', 'n']
stops = ['t', 'tʰ', 'd', 'dʰ']  # T
labials = ['p', 'pʰ', 'b', 'bʰ']  # P
palatovelars = ['ḱ', 'ǵ', 'ǵʰ']
velars = ['k', 'g', 'gʰ']
labiovelars = ['kʷ', 'gʷ', 'gʷʰ']
dorsals = palatovelars + velars + labiovelars  # D
laryngeals = ['h', 'h₁', 'h₂', 'h₃']  # H
fricatives = ['s']
nonlabial_sonorants = ['r', 'l', 'n', 'y']  # R
labial_sonorants = ['m', 'w']  # M
syllabics = ['r̥', 'l̥', 'm̥', 'n̥', 'i', 'u']  # A
sonorants = labial_sonorants + nonlabial_sonorants  # S
consonants = nasals + stops + labials + dorsals + laryngeals + fricatives + sonorants

# map to short vowel
short_vowel = {
    'a': 'a',
    'á': 'á',
    'ā': 'a',
    'ā́': 'á',
    'e': 'e',
    'é': 'é',
    'ē': 'e',
    'ḗ': 'é',
    'i': 'i',
    'í': 'í',
    'ī': 'i',
    'o': 'o',
    'ó': 'o',
    'ō': 'o',
    'ṓ': 'ó',
    'u': 'u',
    'ú': 'ú',
    'ū': 'u',
    'ū́': 'ú',
    'ǣ': 'æ',
    'Ə̄': 'ə',
}

# map to long vowel
long_vowel = {
    'a': 'ā',
    'á': 'ā́',
    'ā': 'ā',
    'ā́': 'ā́',
    'e': 'ē',
    'é': 'ḗ',
    'ē': 'ē',
    'ḗ': 'ḗ',
    'i': 'ī',
    'o': 'ō',
    'ó': 'ṓ',
    'ō': 'ō',
    'ṓ': 'ṓ',
    'u': 'ū',
    'ū': 'ū',
    'ú': 'ū́',
    'ū́': 'ū́',
    'æ': 'ǣ',
    'Ə': 'ə̄',
}


def is_short_vowel(text: str) -> bool:
    """
    Checks if the given value is a short vowel, such as 'a', 'e', or 'o'.

    Parameters
    ----------
    text : str
        Text to check if a short vowel.

    Returns
    -------
    bool
        True if a short vowel, false otherwise.
    """
    regex_uni = '[aeiouáéíóúyɨʉɯʊɪʏøɘɵɤəœɜɛɞʌæɐɶɑɒǽǿάέ]'
    regex_bi = '[äø̞ ɤ̞ e̞]'
    return re.match(regex_uni, text) or re.match(regex_bi, text)


def is_long_vowel(text: str) -> bool:
    """
    Checks if the given value is a long vowel, such as 'ā', 'ē', or 'ō'.

    Parameters
    ----------
    text : str
        Text to check if a long vowel.

    Returns
    -------
    bool
        True if a long vowel, false otherwise.
    """
    regex = '[āēīōūā́ḗṓǣə̄]'
    return re.match(regex, text)


def to_short_vowel(text: str) -> str:
    """
    Converts all long vowels to a short vowels in the given string.

    Parameters
    ----------
    text : str
        Text to convert to short vowels.

    Returns
    -------
    str
        String with short vowels converted to long vowels.
    """
    result = ''
    for char in list(text):
        if is_long_vowel(char):
            result += short_vowel[char]
        else:
            result += char
    return result


def to_long_vowel(text):
    """
    Converts all short vowels to long vowels in the given string.

    Parameters
    ----------
    text :
        Text to convert to long vowels.

    Returns
    -------
    str
        String with long vowels converted to short vowels.
    """
    result = ''
    for char in list(text):
        if is_short_vowel(char):
            result += long_vowel[char]
        else:
            result += char
    return result


def is_diphthong(text: str) -> bool:
    """
    Checks if the given value is a vowel-consonant pair.

    Parameters
    ----------
    text : str
        Text to check if a vowel-consonant diphthong.

    Returns
    -------
        True if a vowel-consonant diphthong, false otherwise.
    """
    # vowel-consonant pair
    regex = '[áéíóúaeiouāēīōūā́ḗṓ][jywiur̥l̥m̥n̥ɪʊ]'
    return re.match(regex, text)


# map to unaccented symbol
de_accent = {
    'á': 'a',
    'ā́': 'ā',
    'é': 'e',
    'ḗ': 'ē',
    'í': 'i',
    'ó': 'o',
    'ṓ': 'ō',
    'ú': 'u',
    'ĺ': 'l',
    'ŕ': 'r',
    'ŕ̥': 'r̥',
    'ḿ': 'm',
    'ḿ̥': 'm̥',
    'ń': 'n',
    'ά': 'ɑ',
    'ǽ': 'æ',
    'έ': 'ɛ',
    'ǿ': 'ø',
}

# map to accented symbol
re_accent = {
    'a': 'á',
    'aː': 'áː',
    'ā': 'ā́',
    'e': 'é',
    'eː': 'éː',
    'ē': 'ḗ',
    'i': 'í',
    'iː': 'íː',
    'o': 'ó',
    'oː': 'óː',
    'ō': 'ṓ',
    'u': 'ú',
    'l': 'ĺ',
    'r': 'ŕ',
    'm': 'ḿ',
    'm̥̩': 'ḿ̥',
    'n': 'ń',
    'ɑ': 'ά',
    'æ': 'ǽ',
    'ɛ': 'έ',
    'ø': 'ǿ',
}


def is_accent(text: str) -> bool:
    """
    Checks if the given value is accented.

    Parameters
    ----------
    text : str
        Text to check if an accented symbol.

    Returns
    -------
    bool
        True if an accented symbol, False otherwise.
    """
    regex = '.*(ā́|[áéíóúḗṓǽǿάέĺŕḿń]).*'
    return re.match(regex, text)


def add_accent(text: str) -> str:
    """
    Adds an accent to the given symbol.

    Parameters
    ----------
    text : str
        Text to add accents.

    Returns
    -------
    str
        Text altered to add accent.
    """
    if isinstance(text, list):
        text = ''.join(text)
    if text in re_accent:
        return re_accent[text]

    # '\u0301' is the acute accent unicode
    return text[:1] + '\u0301' + text[1:]


def remove_accent(text: str) -> str:
    """
    Removes an accent to the given symbol.

    Parameters
    ----------
    text : str
        Text from which to remove accents.

    Returns
    -------
    str
        Text altered to add accent.
    """
    if text in de_accent:
        return de_accent[text]
    result = ''
    for char in list(text):
        if is_accent(char):
            result += de_accent[char]
        else:
            result += char
    return result


class Cover(Enum):
    """
    Enumeration of the different Cover symbols and function (vowel/consonant).

    Attributes
    ----------
    symbol : str
        The symbol used to represent this Cover symbol.
    type : str
        The general type of this symbol, such as Vowel or Consonant.

    """
    Nasals = 0, 'N', 'C'
    Stop = 1, 'T', 'C'
    Labial = 2, 'P', 'C'
    Dorsal = 3, 'D', 'C'
    Laryngeal = 4, 'H', 'C'
    Fricative = 5, 'F', 'C'
    Labial_Sonorant = 6, 'M', 'C'
    Syllabic_Sonorant = 7, 'A', 'A'
    Nonlabial_Sonorant = 8, 'R', 'C'
    Semivowel = 9, 'S', 'S'
    Vowel = 10, 'V', 'V'
    Diphthong = 11, 'G', 'G'

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        obj.symbol = args[1]
        obj.type = args[2]
        return obj

    def type(self):
        return self.type

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

    @staticmethod
    def find(symbol: str) -> 'Cover':
        """
        Find the cover symbol for the given symbol.

        Parameters
        ----------
        symbol : str
            Text for which to find the Cover symbol.

        Returns
        -------
        Cover
            If found, the cover symbol that was matched.

        Raises
        ------
        ValueError
            If a cover symbol is not found for the symbol.
        """
        if symbol in vowels:
            cover = Cover.Vowel
        elif is_diphthong(symbol):
            cover = Cover.Diphthong
        elif symbol in stops:
            cover = Cover.Stop
        elif symbol in labials:
            cover = Cover.Labial
        elif symbol in dorsals:
            cover = Cover.Dorsal
        elif symbol in laryngeals:
            cover = Cover.Laryngeal
        elif symbol in fricatives:
            cover = Cover.Fricative
        elif symbol in labial_sonorants:
            cover = Cover.Labial_Sonorant
        elif symbol in syllabics:
            cover = Cover.Syllabic_Sonorant
        elif symbol in nonlabial_sonorants:
            cover = Cover.Nonlabial_Sonorant
        elif symbol in semivowels:
            cover = Cover.Semivowel
        else:
            raise ValueError('Cover symbol for {} not found'.format(symbol))
        return cover

