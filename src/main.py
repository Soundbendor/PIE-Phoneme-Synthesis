import regex as re
from typing import List
import argparse

import numpy as np
from matplotlib import pyplot as plt

np.seterr(divide='ignore')

from src.phone.phonology import Phonology
from src.phone.word import Sentence, Phrase, Word
from src.util.converter import convert_sentence
from src.util.parser import scrub

AUDIO_DIR = 'dat/phones/'
PHONE_FILE = 'dat/phonemes.csv'


def split_sentences(txt: str, phonology: repr(Phonology)) -> List[Sentence]:
    """
    Split the text into Sentences of Words.

    Parameters
    ----------
    txt : str
        Text to split into Words.

    Returns
    -------
    list
         List of Sentences contains Words.
    """
    txt = scrub(txt)
    sentence_split = re.split(r'[\.!?]\s*', txt)
    sentences = []
    for s in sentence_split:
        if len(s) == 0:
            continue
        phrases = []
        phrase_split = re.split(r'[;,:]\s*', s)
        for p in phrase_split:
            if len(p) == 0:
                continue
            words = []
            word_split = re.split(r'\s+', p)
            for w in word_split:
                word = Word(w, phonology)
                words.append(word)
            phrase = Phrase(p, words)
            phrases.append(phrase)
        sentence = Sentence(s, phrases)
        sentences.append(sentence)
    return sentences


def speak(txt: str, outf: str, spect: bool = False, phonology: repr(Phonology) = None) -> None:
    """
    Synthesize speech and save as a .wav file.

    Parameters
    ----------
     txt : str
        PIE text to synthesize to speech.
    outf : str
        Filename to save the resulting .wav file.
    spect : bool
        Flag to generate a spectrogram of the waveform.
    phonology :
        ``Phonology`` map to use.

    Returns
    -------
    None
    """
    if not phonology:
        phonology = Phonology()

    # parse the user text
    sentences = split_sentences(txt, phonology)

    # ignore pauses between words, if more than one sentence
    pauses = True
    if len(sentences) == 1:
        pauses = False

    # if there is any text, otherwise do nothing
    if len(sentences) > 0:
        ipa = ''

        # first sentence
        out = convert_sentence(sentences[0], AUDIO_DIR, pauses=pauses)
        ipa += sentences[0].ipa()

        # append remaining sentences
        for s in sentences[1:]:
            out = out.append(convert_sentence(s, AUDIO_DIR))
            ipa += s.ipa()

        # save wave file and report to stdout
        out.export(outf, format="wav")
        print('Text : ', txt)
        print('IPA  : ', ipa)
        print('Audio: ', outf)

        # generate spectrogram, if requested
        if spect:
            Pxx, freq, bins, im = plt.specgram(out.get_array_of_samples(), Fs=out.frame_rate, NFFT=512)
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')
            ax = plt.gca()
            ax.set_ylim([0, 4000])
            plotf = outf.replace('.wav', '.png')
            plt.savefig(plotf)
            print('Spect: ', plotf)


if __name__ == '__main__':
    # default values
    text = 'h₁a h₁a'
    outfile = 'output.wav'
    spectrogram = False
    phonology = None

    # define command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', type=str, help='Text to synthesize')
    parser.add_argument('-o', '--out', type=str, help='Filename of the output file (wav)')
    parser.add_argument('-s', '--spectrogram', type=bool, help='Generate a spectrogram of the speech.')
    parser.add_argument('-p', '--phonology', type=str, help='Filename of custom phonology file (json)')
    args = parser.parse_args()

    # retrieve user provided arguments
    if args.text:
        text = args.text
    if args.out:
        outfile = args.out
        if not re.search('.wav$', outfile):
            outfile += '.wav'
    if args.spectrogram:
        spectrogram = args.spectrogram
    if args.phonology:
        phonology = args.phonology

    phonology_map = Phonology()
    if args.phonology:
        # update phonology map
        phonology_map.update_phonology(phonology)

    # generate speech
    speak(txt=text, outf=outfile, spect=spectrogram, phonology=phonology_map)
