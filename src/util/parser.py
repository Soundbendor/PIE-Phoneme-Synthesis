"""
This module contains functions to clean, transform, and split text to prepare for speech synthesis.
"""
import regex as re

from src.phone.grapheme import to_short_vowel, remove_accent, is_accent, add_accent, is_long_vowel, to_long_vowel
from src.phone.phonology import Phonology


def scrub(text: str) -> str:
    """
    Converts text to lower case, removes unnecessary characters, and normalizes whitespace.

    Parameters
    ----------
    text : str
        Text to scrub of unnecessary characters and whitespace.

    Returns
    -------
    str
        Text scrubbed of unnecessary characters.
    """
    # lower case
    text = text.lower()

    # remove double quotes
    text = text.replace('\"', '')

    # remove hyphens
    text = text.replace('-', '')

    # strip parentheses
    text = re.sub('[\)\(]', '', text)

    # normalize whitespace
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text


def normalize(word: str, phonology: repr(Phonology)) -> str:
    """
    Normalize the text notation of PIE. This remaps alternate notations.

    Follows characters given on https://en.wiktionary.org/wiki/Wiktionary:About_Proto-Indo-European.

    Parameters
    ----------
    word : str
        Text to normalize.
    phonology : ``Phonology``
        Map of PIE phonemes to IPA.

    Returns
    -------
    str
        Normalized version of the input word.
    """
    # breathy to aspirated
    word = word.replace('ʱ', 'ʰ')

    # laryngeals
    word = word.replace('h̥', 'h')
    word = word.replace('hₓ', 'h')
    word = word.replace('ə₁', 'h₁')
    word = word.replace('ə₂', 'h₂')
    word = word.replace('ə₃', 'h₃')

    # preserve laryngeals in brackets
    word = word.replace('h₁', '[h₁]')
    word = word.replace('h₂', '[h₂]')
    word = word.replace('h₃', '[h₃]')

    # aspirated stops
    word = word.replace('bh', '[bʰ]')
    word = word.replace('dh', '[dʰ]')
    word = word.replace('th', '[tʰ]')
    word = word.replace('ǵh', '[ǵʰ]')
    word = word.replace('g\'h', '[ǵʰ]')
    word = word.replace('ĝh', '[ǵʰ]')
    word = word.replace('ĝʰ', '[ǵʰ]')
    word = word.replace('g̑h', '[ǵʰ]')
    word = word.replace('g̑ʰ', '[ǵʰ]')
    word = word.replace('gĥ', '[gʰ]')
    word = word.replace('gh', '[gʰ]')
    word = word.replace('gʷh', '[gʷʰ]')
    word = word.replace('gu̯ʰ', '[gʷʰ]')
    word = word.replace('gu̯h', '[gʷʰ]')
    word = word.replace('gwh', '[gʷʰ]')
    word = word.replace('gʷh', '[gʷʰ]')

    # voiceless stops
    word = word.replace('ku̯', '[kʷ]')
    word = word.replace('k\'', '[ḱ]')
    word = word.replace('k̂', '[ḱ]')
    word = word.replace('k̑', '[ḱ]')
    word = word.replace('kʷ\'', '[kʷ]')
    word = word.replace('ḱ\'', '[ḱ]')

    # voiced stops
    word = word.replace('g\'', '[ǵ]')
    word = word.replace('ĝ', '[ǵ]')
    word = word.replace('g̑', '[ǵ]')
    word = word.replace('gu̯', '[gʷ]')

    # labials
    word = word.replace('t\'', '[t]')
    word = word.replace('p\'', '[p]')

    # semivowels
    word = word.replace('j', '[y]')
    word = word.replace('i̯', '[y]')
    word = word.replace('u̯', '[w]')

    # sonorants (alternate notation)
    word = word.replace('l̩', '[l̥]')
    word = word.replace('m̩', '[m̥]')
    word = word.replace('n̩', '[n̥]')
    word = word.replace('r̩', '[r̥]')

    # fricatives
    word = word.replace('z', '[s]')

    # Beekes
    word = word.replace('ʕʷ', '[h₃]')
    word = word.replace('ʔ', '[h₁]')
    word = word.replace('ʕ', '[h₂]')

    # remove enclosing brackets
    word = word.replace('[', '')
    word = word.replace(']', '')

    return colorize(word, phonology)


def colorize(word: str, phonology: repr(Phonology)) -> str:
    """
    Remap vowels according to vowel coloring sound laws.

    Parameters
    ----------
    word : str
        Text to which to remap the vowels.
    phonology : ``Phonology``
        Map of PIE phonemes to IPA.

    Returns
    -------
    str
        Text input with remapping of vowels adjacent to a laryngeal.
    """
    # laryngeal-vowel
    if re.search('h[₁₂₃][eéēḗ]', word):
        he = re.search('((h[₁₂₃])([eéēḗ]))', word)
        key = he.group(1)
        laryngeal = he.group(2)
        old_vowel = he.group(3)
        new_vowel = phonology.get(to_short_vowel(remove_accent(key))).replace(laryngeal, '')

        if is_accent(old_vowel):
            new_vowel = add_accent(new_vowel)
        if is_long_vowel(old_vowel):
            new_vowel = to_long_vowel(new_vowel)
        word = word.replace(key, laryngeal+new_vowel)

    # vowel-laryngeal
    if re.search('[eéēḗ]h[₁₂₃]', word):
        he = re.search('(([eéēḗ])(h[₁₂₃]))', word)

        key = he.group(1)
        laryngeal = he.group(3)
        old_vowel = he.group(2)
        new_vowel = phonology.get(to_short_vowel(remove_accent(key))).replace(laryngeal, '')

        if is_accent(old_vowel):
            new_vowel = add_accent(new_vowel)
        if is_long_vowel(old_vowel):
            new_vowel = to_long_vowel(new_vowel)
        word = word.replace(key, new_vowel+laryngeal)
    return word


def tokenize(word: str) -> list:
    """
    Split the word into character groups approximating Phonemes.

    Parameters
    ----------
    word : str
        Text to tokenize.

    Returns
    -------
    list
        List of graphemes representing the Phonemes.
    """
    result = []

    # various regular expressions to match
    re_h = 'h[₁₂₃]'
    re_alpv = '.[ʰʱʷʱʲ]+'
    re_diacr = '.[\u0301\u0302]'
    re_sonor = '[lmnrĺḿńŕ]\u0325'
    re_dipth = '[aeoāēōáé́óā́ḗṓ][yw]'
    re_two = "(%s|%s|%s|%s|%s)" % (re_h, re_alpv, re_diacr, re_sonor, re_dipth)

    # match the most specific phone
    while word:
        # print(word)
        m = re.match(re_two, word)
        if m:
            # two or more characters
            start, end = m.span()
            result.append(word[:end - start])
            word = word[end - start:]
        else:
            # single character
            result.append(word[:1])
            word = word[1:]
    return result


def syllabize(cover: str) -> str:
    """
    Given a string of Cover symbols, determine syllable breaks.

    Parameters
    ----------
    cover : str
        Text of cover symbols on which to search for syllable breaks.

    Returns
    -------
    str
        Text of cover symbols with syllable breaks '.' inserted.
    """

    V = '[VARMG]'  # vowels
    C = '[TPDHRMF]'  # consonants
    G = '[G]'  # diphthong

    # example VC.CV.CVC.CVC
    # G.G
    match = re.match('.*({})({}).*'.format(G, G), cover)
    if match:
        cover = re.sub('({})({})'.format(G, G), r'\1.\2', cover)

    # VC.CV
    match = re.match('.*({}{}{}{}).*'.format(V, C, C, V), cover)
    if match:
        cover = re.sub('({}{})({}{})'.format(V, C, C, V), r'\1.\2', cover)

    # VC.VC
    match = re.match('.*({}{}{}{}).*'.format(V, C, V, C), cover)
    if match:
        cover = re.sub('({}{})({}{})'.format(V, C, V, C), r'\1.\2', cover)

    return cover.replace('_', '')



