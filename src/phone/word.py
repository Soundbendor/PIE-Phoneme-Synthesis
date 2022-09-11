from typing import List

from src.phone.phonology import Phonology
from src.phone.grapheme import add_accent
from src.phone.pause import Pause, PauseType
from src.phone.phoneme import Phoneme, Phone
from src.util.matcher import match_phones
from src.util.parser import normalize, tokenize, syllabize


class Word:
    """
    Representation of a single Word.

    Attributes
    ----------
    text : str
        Text to represent with this Word.
    phonology : ``Phonology``
        Map of graphemes to phonemes in PIE.

    Returns
    -------
    str
        IPA representation of the Phoneme.
    """

    def __init__(self, text: str, phonology: repr(Phonology)):
        self.text = text
        self.word = normalize(text, phonology)
        self.phonemes = []

        # tokenize
        for token in tokenize(self.word):
            if not phonology.verify(token):
                raise ValueError('\'{}\' in {} ({}) is not a valid character in PIE'.format(token, self.word, text))
            self.phonemes.append(Phoneme(token, phonology))

        # syllables
        syllable_str = syllabize(self.cover())
        for i in range(len(syllable_str)):
            if syllable_str[i] == '.':
                self.phonemes.insert(i, Pause(PauseType.Syllable))

        # match audio files for each phone
        match_phones(self.phones())

        # print(self.word)
        # print(self.phonemes)
        # print('==============')

    def cover(self) -> str:
        """
        Constructs a string of Cover symbols from the set of phonemes

        Returns
        -------
        str
            String of Cover symbols representing this Word.
        """
        retstr = ''
        for phoneme in self.phonemes:
            retstr += str(phoneme.cover)
        return retstr

    def phones(self) -> List[Phone]:
        """
        Produce a list of all `Phone`s contained in this Phoneme.

        Returns
        -------
        list
            List of phones for this word.
        """
        phones = []
        for phoneme in self.phonemes:
            phones.extend(phoneme.phones)
        return phones

    def ipa(self) -> str:
        """
        Retrieve the IPA string for this Word.

        Returns
        -------
        str
            IPA representation of the Word.
        """
        ipa = ''
        for phoneme in self.phonemes:
            if phoneme.accent:
                ipa += add_accent(phoneme.symbol)
            else:
                ipa += phoneme.ipa()
        return ipa

    def __str__(self):
        return self.word


class Phrase:
    """
    Representation of a phrase or clause.

    Attributes
    ----------
    text : str
        Text to represent with this Phrase.
    words : list
        List of Words in this Sentence.
    """

    def __init__(self, text: str, words: List[Word]):
        self.text = text
        self.words = words

    def ipa(self) -> str:
        """
        Retrieve the IPA string for this Phrase.

        Returns
        -------
        str
            IPA representation of the Phrase.
        """
        ipa = ''
        for w in self.words:
            ipa += w.ipa() + ' '
        ipa = ipa[:-1] + ','
        return ipa


class Sentence:
    """
    Representation of a single Sentence.

    Attributes
    ----------
    text : str
        Text to represent with this Sentence.
    phrases : list
        List of Phrases in this Sentence.
    """

    def __init__(self, text: str, phrases: List[Phrase]):
        self.text = text
        self.phrases = phrases

    def ipa(self) -> str:
        """
        Retrieve the IPA string for this Sentence.

        Returns
        -------
        str
            IPA representation of the Sentence.
        """
        ipa = ''
        for p in self.phrases:
            ipa += p.ipa() + ' '
        if ipa[-2] == ',':
            ipa = ipa[:-2] + '. '
        else:
            ipa = ipa[:-1] + '. '
        return ipa

