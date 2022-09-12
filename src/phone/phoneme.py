"""
This module contains phonetic structures to represent in the speech.
"""

from src.phone.phonology import Phonology
from src.phone.grapheme import Cover, is_accent, remove_accent


class Phone:
    """
    Representation of a Phone, a single sound.

    Attributes
    ----------
    symbol : str
        Symbol that represents this phonetic sound.
    accent : bool
        Flag noting if this sound is accented.
    audio : str
        Audio file representing this phone, after matching.
    duration : float
        Length of the audio in seconds representing this phone
    """
    def __init__(self, symbol: str, accent: bool = False):
        """
        Construct a new Phone object.

        Parameters
        ----------
        symbol : str
            Symbol that represents this phonetic sound.
        accent : bool
            Flag noting if this sound is accented.
        """
        self.symbol = symbol
        self.accent = accent
        self.audio = ''
        self.duration = 0

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return '<{}>'.format(self.symbol)


class Phoneme:
    """
    Representation of a Phoneme, a unit of language, which can be represented one or more Phones.

    Attributes
    ----------
    symbol : str
        Symbol that represents this phonetic Phoneme.
    phonology : ``Phonology``
        Map of graphemes to phonemes in PIE.
    """

    def __init__(self, symbol: str, phonology: repr(Phonology)):
        self.phoneme = symbol

        # handle accent
        self.unaccented = self.phoneme
        self.accent = False
        if is_accent(self.phoneme):
            self.unaccented = remove_accent(self.phoneme)
            self.accent = True

        # determine Cover
        self.cover = Cover.find(self.unaccented)

        # set ipa
        self.symbol = phonology.get(self.unaccented)

        # split into individual phones
        self.phones = []
        if isinstance(self.symbol, list):
            # multiple phones
            for symb in self.symbol:
                self.phones.append(Phone(symb, accent=self.accent))
        else:
            # singleton
            self.phones.append(Phone(self.symbol, accent=self.accent))

    def ipa(self):
        """
        Retrieve the IPA string for this Phoneme.

        Returns
        -------
        str
            IPA representation of the Phoneme.
        """
        ipa = ''
        if isinstance(self.symbol, list):
            for phone in self.phones:
                ipa += phone.symbol
        else:
            ipa += self.symbol
        return ipa.replace('`', '\'')

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return '<{}>'.format(self.symbol)

