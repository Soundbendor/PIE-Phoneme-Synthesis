"""
This module contains structures to represent a Pause in the speech.

The following types of Pauses are supported:
    - Clause
    - Word
    - Clause
    - Sentence
    - Paragraph
"""
from enum import Enum
import random


class PauseType(Enum):
    """
    Enumeration of the possible types of pauses in speech.

    Each PauseType contains a symbol and a maximum suggested duration.

    Attributes
    ----------
    symbol : str
        The symbol used to represent this Pause in IPA.
    length : float
        The maximum duration (in seconds) used for this Pause.
    """
    Syllable = 0, '.', 0.005
    Word = 1, ' ', 0.15
    Phrase = 2, ',', 0.25
    Sentence = 3, '.', 0.65
    Paragraph = 4, '\n', 1.0

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        obj.symbol = args[1]
        obj.length = args[2]
        return obj

    def __str__(self):
        return self.symbol


class Pause:
    """
    Representation of a Pause, used to separate words and sentences.

    Attributes
    ----------
    pause_type : PauseType
        The symbol(s) that represent this Phoneme.
    """

    def __init__(self, pause_type: PauseType):
        """
        Construct a new Pause object.

        Parameters
        ----------
        pause_type : PauseType
            The symbol(s) that represent this Phoneme.
        """
        self.pause_type: 'PauseType' = pause_type
        self.accent: bool = False  # pause is always unaccented
        #self.symbol: str = pause_type.symbol
        self.phones: list = []

    def silence(self) -> int:
        """
        Generates a random duration to be used as silence for this pause.

        Returns
        -------
        int
            A random pause duration in milliseconds.
        """
        return round(random.uniform(self.pause_type.length / 2, self.pause_type.length) * 1000)

    def ipa(self) -> str:
        """
        Produce an IPA symbol for this Pause (e.g., ' ' or '.').

        Returns
        -------
        str
            IPA representation of the Pause.
        """
        return self.pause_type.symbol if self.pause_type != PauseType.Syllable else ''

    def __str__(self):
        return str(self.pause_type)

    def __repr__(self):
        return '<{}>'.format(self.pause_type)
