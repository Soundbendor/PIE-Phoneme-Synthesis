"""
This module contains functions to match audio sounds to each Phoneme.
"""
import os
from os.path import exists
from typing import List, Tuple
import regex as re
import pandas as pd

# DIR = 'C:\praat\swadesh\out\\'
# csv_file = 'phonemes.csv'

# def count_row(dir: str):
#     print('Swadesh word count')
#     for file in os.listdir(dir):
#         if file.endswith('.txt'):
#             df = pd.read_csv(dir + file, delimiter=',', engine='python', encoding='utf-16')
#             print(file, len(df))
# df = count_row(DIR)


def load_phonemes(dir: str, csv: str) -> pd.DataFrame:
    """
    Load the dataframe of phonetic sounds.

    Parameters
    ----------
    dir : str
        Directory containing the list of phonetic sounds for each language.
    csv : str
        CSV file containing the set of phonetic sounds.

    Returns
    -------
    pd.DataFrame
        Dataframe containing the dataset of phones for all languages.
    """

    if exists(csv):
        df = pd.read_csv(csv, sep=',', encoding='utf-16')
    else:
        # print("Creating phonemes.csv")
        df = pd.DataFrame(
            columns=['prev', 'curr', 'next', 'next2', 'next3', 'word', 'ipa', 'lang', 'family', 'start', 'end', 'dur',
                     'file'])
        for file in os.listdir(dir):
            if file.endswith('.txt'):
                data = pd.read_csv(dir + file, delimiter=',', engine='python', encoding='utf-16')
                data.columns = df.columns.str.replace(' ', '')
                df = pd.concat([df, data], ignore_index=True)
        df.to_csv(csv, sep=',', encoding='utf-16')
    return df
#print(os.getcwd())
#data = load_phonemes('./dat/phones/', './dat/phonemes.csv')
data = load_phonemes('C:\praat\swadesh\out2\\', './dat/phonemes.csv')


# load the data
def phone_df():
    return data


def get_cc(file: str) -> str:
    """
    Extract the country code abbreviation from the audio file name.

    Parameters
    ----------
    file : str
        Name of the audio file.

    Returns
    -------
    str
        String representing the country code.
    """
    regex = '.+_(.+)-.*-.*.wav'
    match = re.match(regex, file)
    if match:
        return match.group(1)
    else:
        print("Problem not CC for {}".format(file))
        return ''


def set_audio(phones: list, index: int, data: pd.DataFrame, data_idx: int) -> None:
    """
    Update the Phone object with the audio file.

    Parameters
    ----------
    phones : list
        List of Phones to match.
    index : int
        Index of the target Phone in the list.
    data : pd.DataFrame
        Dataframe of phones to audio files.
    data_idx : int
        Index of the target row in the dataframe.

    Returns
    -------
    None
    """
    phones[index].audio = get_file(data, data_idx)
    phones[index].cc = get_cc(phones[index].audio)
    phones[index].duration = data.iloc[data_idx]['dur']


def match_phones(phones: list) -> bool:
    """
    Match each Phone in the list with an audio file.

    Parameters
    ----------
    phones : list
        List of Phones to match.

    Returns
    -------
    bool
        True if successful, or raises an exception if failed.
    """
    lst = phones

    # print(phones)
    while len(lst) > 0:
        syllables = []
        i = 0
        while i < len(lst) and str(lst[i]) != '.':
            syllables.append(lst[i])
            i += 1
        lst = lst[i + 1:]
        match_syllable(data, syllables)
    return True


def match_syllable(data: pd.DataFrame, phones: List) -> bool:
    """
    Match each Phone in the list with an audio file.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe of phones to audio files.
    phones : list
        List of Phones to match.

    Returns
    -------
    bool
        True if successful, or raises an exception if failed.
    """
    # match entire word
    n = len(phones)
    if n <= 3:
        idx, m = find_ngram(data, phones, n=len(phones), start=True, end=True)
        if m == n:
            for i in range(n):
                set_audio(phones, n - m - i, data, idx + i)
            return True

    # match end
    n = len(phones)
    idx, m = find_ngram(data, phones, n=min(n, 3), end=True)
    for i in range(m):
        set_audio(phones, n - m + i, data, idx + i)
    phones = phones[:n - m]

    # match start
    n = len(phones)
    idx, m = find_ngram(data, phones, n=min(n, 3), start=True)
    for i in range(m):
        set_audio(phones, i, data, idx + i)
    phones = phones[m:]

    # match middle
    while len(phones) > 0:
        n = len(phones)
        idx, m = find_ngram(data, phones, n=min(n, 3))
        for i in range(m):
            set_audio(phones, i, data, idx + i)
        phones = phones[m:]
    return True


def find_ngram(data: pd.DataFrame, phones: List, n: int = 1, start: bool = False, end: bool = False) -> tuple[int, int]:
    """
    Match an n-gram of Phone in the dataframe.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe of phones to audio files.
    phones : list[Phone]
        List of Phones to match.
    n : int
        Number of phones to match, defaults to 1.
    start : bool
        Flag if priority to match at the beginning, defaults to False.
    end : bool
        Flag if priority to match at the end, defaults to False.

    Returns
    -------
    tuple[int, int]
        Tuple containing the index of the match in the dataframe and the number of phones matched.
    """
    idx, m = 0, 0

    if n == 3:
        idx, m = find_tri(data, phones, start, end)

    if n == 2:
        idx, m = find_bi(data, phones, start, end)

    if n == 1:
        idx, m = find_uni(data, phones, start, end)

    return idx, m


def find_uni(data: pd.DataFrame, phones: List, start: bool = False, end: bool = False) -> Tuple[int, int]:
    """
    Match a single phone in the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe of phones to audio files.
    phones : list[Phone]
        List of Phones to match.
    start : bool
        Flag if priority to match at the beginning, defaults to False.
    end : bool
        Flag if priority to match at the end, defaults to False.

    Returns
    -------
    tuple[int, int]
        Tuple containing the index of the match in the dataframe and the number of phones matched.
    """
    n = len(phones)
    if start and end:
        # print('uni-both', str(phones[n - 1]))
        unigram_df = data[(data['prev'].isnull()) & (data['curr'] == str(phones[n - 1])) & (data['next'].isnull())]
    elif end:
        # print('uni-end', str(phones[n - 1]))
        unigram_df = data[(data['curr'] == str(phones[n - 1])) & (data['next'].isnull())]
    elif start:
        # print('uni-start', str(phones[n - 1]))
        unigram_df = data[(data['prev'].isnull()) & (data['curr'] == str(phones[0]))]
    else:
        unigram_df = data[(data['curr'] == str(phones[0]))]

    if len(unigram_df) == 0:
        # last try
        unigram_df = data[(data['curr'] == str(phones[0]))]

    if len(unigram_df) > 0:
        idx = unigram_df.sample(n=1).index[0]
        return idx, 1
    else:
        raise ValueError("Phoneme not found uni " + str(phones), start, end)


def find_bi(data: pd.DataFrame, phones: list, start: bool = False, end: bool = False) -> Tuple[int, int]:
    """
    Match a pair of phone in the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe of phones to audio files.
    phones : list[Phone]
        List of Phones to match.
    start : bool
        Flag if priority to match at the beginning, defaults to False.
    end : bool
        Flag if priority to match at the end, defaults to False.

    Returns
    -------
    tuple[int, int]
        Tuple containing the index of the match in the dataframe and the number of phones matched.
    """
    audio = []
    if start and end:
        bigram_df = data[
            (data['prev'].isnull()) & (data['curr'] == str(phones[0])) & (
                    data['next'] == str(phones[1])) & (
                data['next2'].isnull())]
    elif start:
        bigram_df = data[
            (data['prev'].isnull()) & (data['curr'] == str(phones[0])) & (data['next'] == str(phones[1]))]
    elif end:
        n = len(phones)
        bigram_df = data[(data['curr'] == str(phones[n - 2])) & (data['next'] == str(phones[n - 1])) & (
            data['next2'].isnull())]
    else:
        bigram_df = data[(data['curr'] == str(phones[0])) & (data['next'] == str(phones[1]))]

    if len(bigram_df) > 0:
        # bigram found
        idx = bigram_df.sample(n=1).index[0]
        return idx, 2
    else:
        # find unigram
        return find_uni(data, phones, start, end)


def find_tri(data: pd.DataFrame, phones: List, start: bool = False, end: bool = False) -> Tuple[int, int]:
    """
    Match a trio of phones in the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe of phones to audio files.
    phones : list[Phone]
        List of Phones to match.
    start : bool
        Flag if priority to match at the beginning, defaults to False.
    end : bool
        Flag if priority to match at the end, defaults to False.

    Returns
    -------
    tuple[int, int]
        Tuple containing the index of the match in the dataframe and the number of phones matched.
    """
    audio = []
    if start and end:
        trigram_df = data[
            (data['prev'].isnull()) & (data['curr'] == str(phones[0])) & (
                    data['next'] == str(phones[1])) & (
                    data['next2'] == str(phones[2])) & (
                data['next3'].isnull())]
    elif start:
        trigram_df = data[
            (data['prev'].isnull()) & (data['curr'] == str(phones[0])) & (
                    data['next'] == str(phones[1])) & (
                    data['next2'] == phones[2])]
    elif end:
        n = len(phones)
        trigram_df = data[
            (data['curr'] == str(phones[n - 3])) & (data['next'] == str(phones[n - 2])) & (
                    data['next2'] == str(phones[n - 1])) & (
                data['next3'].isnull())]
    else:
        trigram_df = data[
            (data['curr'] == str(phones[0])) & (data['next'] == str(phones[1])) & (
                    data['next2'] == str(phones[2]))]

    if len(trigram_df) > 0:
        # trigram found
        idx = trigram_df.sample(n=1).index[0]
        return idx, 3
    else:
        # find bigram
        return find_bi(data, phones, start, end)


def get_file(data: pd.DataFrame, idx: int) -> str:
    """
    Return the path of the audio file at the provided index.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe of phones to audio files.
    idx :
        Index of the dataframe to query.

    Returns
    -------
    str
        Repeat the directory+file name of the retrieved audio file.
    """
    rows = data.iloc[idx]
    f = rows['file']
    d = rows['lang']
    file = d + '/' + f
    return file
