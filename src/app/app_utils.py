"""
This module contains functions used by the Streamlit app.
"""
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from src.app.phonology_options import digrams
from src.main import split_sentences, AUDIO_DIR
from src.phone.phonology import Phonology
from src.util.converter import convert_sentence, buffer
np.seterr(divide='ignore')


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


def speak(phonology: repr(Phonology), audio_container, txt2spk, pauses=True, spectrogram=False):
    """
    Synthesis the text and add the IPA and audio to Streamlit.

    Parameters
    ----------
    phonology : `Phonology`
        Mapping of PIE phonemes to IPA.
    audio_container : st.container
        `Streamlit` container for the synthesized speech.
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
        try:
            sentences = split_sentences(txt2spk, phonology)
        except ValueError as ve:
            st.error(ve)
        else:
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
    word_container : `Streamlit` container
        `Streamlit` container to place the definition.
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



