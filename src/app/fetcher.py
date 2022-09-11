"""
Fetches Proto Indo European words from the Wiktionary.
"""

import pandas as pd
import regex as re
import requests
import os

# PIE word list
pie_word_list = 'dat/pie_wiktionary_words.txt'
pie_word_df = pd.read_csv(pie_word_list, delimiter=',', engine='python', encoding='utf-16')

# variables to build Wiktionary URL
PIE_URL_prefix = r'https://en.wiktionary.org/w/api.php?action=parse&page='
PIE_URL_lang = r'Reconstruction:Proto-Indo-European/'
PIE_URL_suffix = r'&prop=wikitext&format=json&formatversion=1'
PARTS_OF_SPEECH = r'Root|Noun|Verb|Adjective|Adverb|Numeral|Pronoun|Particle|Determiner|Interjection|Prefix|Suffix|Root [\d]'


def all_words():
    result_df = pd.DataFrame(columns=['word', 'definition', 'pos', 'gender', 'url'])
    for index, row in pie_word_df.iterrows():
        word = pie_word_df.iloc[index].values[0].replace(PIE_URL_lang, '')
        word_dict = fetch_word(word)
        print(word_dict['word'], word_dict['pos'], word_dict['definition'])
        result_df = pd.concat([result_df, pd.DataFrame(word_dict)], ignore_index=True)
    result_df.to_csv('wiki_definitions.csv', sep=',', encoding='utf-16')









def random_word() -> str:
    """
    Fetch a random word from the Wiktionary list.

    Returns
    -------
    str
        Random PIE word.
    """
    word = '-'
    # find a word that is not a suffix
    while re.match('^-', word):
        word = pie_word_df.sample(n=1)['word'].values[0].replace(PIE_URL_lang, '')
    return word


def fetch_word(word: str = None) -> dict:
    """
    Fetch a word from Wiktionary.

    Parameters
    ----------
    word : str
        Word to fetch if given, otherwise fetch a random word.

    Returns
    -------
    dict
        dictionary containing the information: 'word', 'definition', 'url', 'pos', and 'gender'.
    """
    if not word:
        # pick a random word
        word = random_word()

    # create URL to Wiktionary
    url = PIE_URL_prefix + PIE_URL_lang + word + PIE_URL_suffix
    #print(url)

    # retrieve Wiktionary page and handle potential errors
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error contacting the Wiktionary API. Status Code: {res.status_code}.')

    res_json = res.json()
    if 'error' in res_json.keys():
        error = res_json['error']
        raise RuntimeError('Error contacting Wiktionary for word ' + word + ': ' + error['info'] + ": " + error['code'])

    if 'parse' not in res_json.keys():
        raise RuntimeError('Unknown error while querying Wiktionary.')

    # grab the Wiktionary text
    wiki_text = res_json['parse']['wikitext']['*']
    # title = res_json['parse']['title']  # not needed

    pos = ''
    pos_found = False
    gender = ''
    definitions = []
    word_dict = {}

    # parse each word in Wiktionary result
    for line in wiki_text.splitlines():
        # find the part of speech
        pos_result = re.search('===(' + PARTS_OF_SPEECH + ')===', line)
        if pos_result:
            pos = pos_result.group(1).lower()
            pos = re.sub(r'\s[\d]', '', pos)
            pos_found = True

        # find gender of noun
        gender_result = re.search(r'\{\{ine-noun\|([mfn]|m or f)[\|\}].*\}', line)
        if gender_result:
            pos = 'noun, ' + gender_result.group(1)

        if pos_found:
            # alternate definitions
            if re.search(r'\{\{alt form\|', line):
                # find alternate definition, type 1
                alt_form = re.search(r'\{\{alt form\|ine-pro\|(.*?)\|t=(.*)\}\}', line)
                defin = 'alternate form of [' + alt_form.group(
                    1) + '](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/' + alt_form.group(1).replace(
                    '*', '') + '), *' + alt_form.group(2) + '*'
                definitions.append(defin)
            elif re.search(r'\{\{alternative form of\|', line):
                # find alternate definition, type 2
                alt_form = re.search(r'\{\{alternative form of\|ine-pro\|(.*?)\}\}', line)
                defin = 'alternate form of [' + alt_form.group(
                    1) + '](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/' + alt_form.group(1).replace(
                    '*', '') + ')'
                definitions.append(defin)
            elif re.search(r'\{\{n-g\|or', line):
                # skip this type of alt form
                continue
            elif re.search(r'\{\{n-g\|', line):
                # find alternate definition, type 3 (n-g)
                alt_form = re.search(r'\{\{n-g\|(.*)\}\}', line)
                defin = alt_form.group(1).lower()
                defin = re.sub(r'\[*', '', defin)
                defin = re.sub(r'\]*\}*', '', defin)
                defin = defin.strip()
                definitions.append(defin)
            elif re.search('\{\{non-gloss definition\|.*\}\}', line):
                alt_form = re.search(r'\{\{non-gloss definition\|(.*)\}\}', line)
                defin = alt_form.group(1).lower()
                defin = defin.strip()
                definitions.append(defin)
            elif re.search('\{\{alternative reconstruction of\|ine-pro\|(.*)\}\}', line):
                alt_form = re.search(r'\{\{alternative reconstruction of\|ine-pro\|(.*)\}\}', line)
                defin = 'alternative reconstruction of [' + alt_form.group(1) + \
                    '](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/' + alt_form.group(
                    1).replace('*', '') + ')'
                definitions.append(defin)

            # find definition
            if re.match('^#', line):
                # text clean up
                defin = re.sub(r'#\s', '', line)
                defin = re.sub(r'<ref>.*?</ref>', '', defin)
                defin = re.sub(r'<ref.*?>.*?</ref>', '', defin)
                defin = re.sub(r'<ref.*?>', '', defin)
                defin = re.sub(r'</ref>', '', defin)
                defin = re.sub(r'\{\{.*?\}\}', '', defin)
                defin = re.sub(r'[#\[\]]', '', defin)
                defin = re.sub(r'[*:]', '', defin)
                defin = re.sub(r'[|]', '/', defin)
                defin = re.sub(r'\(disputed - see talk page\)', '', defin)
                defin = re.sub(r'\(= \)', '', defin)
                defin = re.sub('\'\'', '', defin).strip()
                if defin:
                    if re.match(r'^\s*[,→] ', defin):
                        # continuation, append to previous
                        definitions[-1] = definitions[-1] + defin
                    else:
                        definitions.append(defin)

        url = 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/' + word.replace(' ', '_')
        word_dict = {'word': word, 'pos': pos, 'definition': definitions, 'url': url, 'gender': gender}

    return word_dict
