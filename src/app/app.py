"""
This module contains the Streamlit app.
"""
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from src.app.fetcher import fetch_word
from src.app.phonology_options import digrams
from src.app.phonology_select import add_phonology
from src.main import split_sentences, AUDIO_DIR
from src.phone.phonology import Phonology
from src.app.sampler import sheep_and_horses, king_and_god, vocab_word
from src.util.converter import convert_sentence, buffer
np.seterr(divide='ignore')

rand_word_dict = fetch_word()
if 'random_word' not in st.session_state:
    st.session_state['random_word'] = rand_word_dict


def load_map(phonology: repr(Phonology)) -> None:
    """
    Load mapping from Phonology.

    Parameters
    ----------
    phonology : `Phonology`
        PIE `Phonology` map

    Returns
    -------
    None
    """
    for label in st.session_state.keys():
        if label == 'random_word':
            continue
        key = label.replace('*', '').replace('[', '').replace(']', '').strip()
        value = st.session_state[label]
        if value in digrams:
            phonology.set(key, digrams[value])
        else:
            phonology.set(key, value)


def speak(audio_container, txt2spk, pauses=True, spectrogram=False):
    """
    Synthesis the text and add the IPA and audio to Streamlit.

    Parameters
    ----------
    audio_container : st.container
        ``Streamlit`` container for the synthesized speech.
    txt2spk : str
        Text to synthesize to speech.
    pauses : bool
        Flag if to include pauses (silence) between words and sentences. For single words, set to False.
    spectrogram : bool
        Flag if to include the spectrogram of the audio.

    Returns
    -------

    """
    audio_container.empty()
    with st.spinner('Generating speech...'):
        sentences = split_sentences(txt2spk, phonology)

        accent = st.session_state['accent']
        if len(sentences) == 1:
            pauses = False
        if len(sentences) > 0:
            out = convert_sentence(sentences[0], AUDIO_DIR, pauses=pauses, accent=accent)
            ipa = sentences[0].ipa().replace('`', r'\'')
            for s in sentences[1:]:
                out = out.append(convert_sentence(s, AUDIO_DIR, pauses=pauses, accent=accent))
                ipa += s.ipa().replace('`', r'\'')

            if out:
                if not pauses:
                    audio_container.info(ipa.replace('.', ''))  # remove period from single word
                else:
                    audio_container.info(ipa)

                # add audio
                buf = buffer(out)
                audio_container.audio(buf, format='audio/wav')

                # add spectrogram
                if spectrogram:
                    Pxx, freq, bins, im = plt.specgram(out.get_array_of_samples(), Fs=out.frame_rate, NFFT=512)
                    plt.ylabel('Frequency [Hz]')
                    plt.xlabel('Time [sec]')
                    ax = plt.gca()
                    ax.set_ylim([0, 4000])
                    audio_container.pyplot(plt)


def display_definition(word_container, word_d: dict) -> None:
    """
    Format and display a PIE word from Wiktionary.

    Parameters
    ----------
    word_d : dict
        Word dictionary containing the word, url, part of speech, and url.
    word_container : ``Streamlit`` container
        ``Streamlit`` container to place the definition.
    """
    word_container.empty()
    word_container.subheader('[' + word_d['word'] + '](' + word_d['url'] + ')')
    word_container.write(' *' + word_d['pos'] + '*')
    defin_str = ''
    if len(word_d['definition']) == 1:
        defin_str += ' * ' + word_d['definition'][0] + '  \n  '
    else:
        for defin in word_d['definition']:
            defin_str += '1) ' + defin + '  \n  '
    word_container.caption(defin_str)


# Phonology tab
with st.expander("Select Phonology"):
    phonology = Phonology()
    add_phonology(phonology)
    load_map(phonology)

# Audio modes
word_tab, text_tab, sheep_story_tab, king_story_tab = st.tabs(
    ['Random Word', 'Enter Text', '"Sheep and the Horses"', '"King and the god"'])

# Random word
with word_tab:
    random_word_cols = st.columns(4)
    with random_word_cols[0]:
        st.markdown(' ')
        st.markdown(' ')
        word_speak_button = st.button('Speak', help='Synthesis the word')

    with random_word_cols[2]:
        st.markdown(' ')
        st.markdown(' ')
        random_word_button = st.button('New Word', help='Select a random word from Wiktionary')
    with random_word_cols[3]:
        vocab_select = st.selectbox('Vocabulary List:',
                                    ['Wiktionary', 'adjectives', 'adverbs', 'anatomy', 'animals', 'colors', 'food',
                                     'kinship', 'nature', 'numerals', 'pronouns', 'religion', 'society', 'time',
                                     'tools', 'verbs'])
    random_word_container = st.container()
    random_word_audio_container = st.container()

# Free text
with text_tab:
    txt = 'óynos, dwóh₁, tréyes, kʷetwóres, pénkʷe'
    text_input = st.text_area('Enter text:', txt, help='Enter PIE text to synthesis to speech')
    speak_button_text = st.button('Speak', key='speak_button_text', help='Synthesize speech')
    freetext_audio_container = st.container()

# Sheep story
with sheep_story_tab:
    title_str = '### **[' + sheep_and_horses['title'] + '](' + sheep_and_horses['url'] + ')**'
    st.write(title_str)
    st.write(sheep_and_horses['eng'])
    st.success(sheep_and_horses['pie'])
    speak_button_sheep = st.button('Speak', key='speak_button_sheep', help='Synthesize speech')
    sheep_audio_container = st.container()

# King story
with king_story_tab:
    title_str = '### **[' + king_and_god['title'] + '](' + king_and_god['url'] + ')**'
    st.write(title_str)
    st.write(king_and_god['eng'])
    st.success(king_and_god['pie'])
    speak_button_king = st.button('Speak', key='speak_button_king', help='Synthesize speech')
    king_audio_container = st.container()

if random_word_button:
    if vocab_select == 'Wiktionary':
        # display a random word from Wiktionary
        rand_word_dict = fetch_word()
        st.session_state['random_word'] = rand_word_dict
        display_definition(random_word_container, rand_word_dict)
        speak(random_word_audio_container, rand_word_dict['word'], pauses=False, spectrogram=True)
    else:
        # fetch from specific word list
        vocab_word_dict = fetch_word(vocab_word(vocab_select))
        st.session_state['random_word'] = vocab_word_dict
        display_definition(random_word_container, vocab_word_dict)
        speak(random_word_audio_container, vocab_word_dict['word'], pauses=False, spectrogram=True)

if word_speak_button:
    display_definition(random_word_container, st.session_state['random_word'])
    speak(random_word_audio_container, st.session_state['random_word']['word'], pauses=False, spectrogram=True)

if speak_button_text:
    speak(freetext_audio_container, text_input, pauses=True, spectrogram=True)

if speak_button_sheep:
    speak(sheep_audio_container, sheep_and_horses['pie'], pauses=True, spectrogram=False)

if speak_button_king:
    speak(king_audio_container, king_and_god['pie'], pauses=True, spectrogram=False)
