"""
This module contains functions to convert a text sequence to audio.
"""
from typing import List

from pydub import AudioSegment

from src.phone.pause import Pause, PauseType
from src.phone.phoneme import Phone
from src.phone.word import Word, Sentence


def buffer(sound: AudioSegment) -> bytes:
    """
    Load an AudioSegment as a 'wav' into a bytes object.

    Parameters
    ----------
    sound : AudioSegment
        AudioSegment to buffer

    Returns
    -------
    bytes
        Buffer of raw audio.
    """
    import io
    buf = io.BytesIO()
    sound.export(buf, format="wav")
    return buf.getvalue()


def convert_phone(phone: Phone, audio_dir: str, accent: str = 'pitch') -> List[AudioSegment]:
    """
    Synthesize a single Phone to an AudioSegment.

    Parameters
    ----------
    phone : Phone
        Phone to convert to audio.
    audio_dir : str
        Directory of audio files.
    accent : str
         Determines which accent mode to use in synthesis.

    Returns
    -------
    list[AudioSegment]
        list of AudioSegments representing the Phone.
    """
    audiofile = audio_dir + phone.audio

    if isinstance(phone, Pause):
        # pause
        sound = AudioSegment.silent(duration=Pause(PauseType.Syllable).silence())
    else:
        if phone.accent and accent == 'pitch':
            reg_sound = AudioSegment.from_wav(audiofile)
            octaves = 0.05
            new_sample_rate = int(reg_sound.frame_rate * (2.0 ** octaves))
            sound = reg_sound._spawn(reg_sound.raw_data, overrides={'frame_rate': new_sample_rate})
            sound = sound.set_frame_rate(16000)
        elif phone.accent and accent == 'stress':
            sound = AudioSegment.from_wav(audiofile) + 3
        else:
            sound = AudioSegment.from_wav(audiofile)
    return sound


def convert_word(word: Word, audio_dir: str, start: int = 0, accent: str = 'pitch') -> List[AudioSegment]:
    """
    Synthesize a Word object to an AudioSegment.

    Parameters
    ----------
    word : Word
        Word to convert to audio.
    audio_dir : str
        Directory of audio files.
    start : int
        Start time of the audio phone in context.
    accent : str
        Determines which accent mode to use in synthesis.

    Returns
    -------
    List[AudioSegment]
        Synthesized audio of the Word.
    """
    sounds = []
    phones = word.phones()
    for phone in phones:
        if isinstance(phone, Pause):
            sound = AudioSegment.silent(duration=phone.silence())
        else:
            sounds.extend(convert_phone(phone, audio_dir, accent=accent))
    # add pause after word
    sounds.extend(AudioSegment.silent(duration=Pause(PauseType.Word).silence()))
    return sounds


def convert_sentence(sentence: Sentence, audio_dir: str, start: int = 0, pauses: bool = False,
                     accent: str = 'pitch') -> AudioSegment:
    """
    Synthesis a Sentence object to AudioSegment.

    Parameters
    ----------
    sentence : Sentence
        Sentence to convert to audio.
    audio_dir : str
        Directory of audio files.
    start : int
        Start time of the audio phone in context.
    pauses : bool
        Flag to determine if to add silence for the Pause.
    accent : str
        Determines which accent mode to use in synthesis.

    Returns
    -------
    AudioSegment
        Synthesized audio of the Sentence.
    """
    sounds = []

    # synthesize
    for phrase in sentence.phrases:
        for word in phrase.words:
            sounds.extend(convert_word(word, audio_dir, start=start, accent=accent))
        # add pause after phrase
        if pauses:
            sounds.extend(AudioSegment.silent(duration=Pause(PauseType.Phrase).silence()))

    # add pause after sentence
    if pauses:
        sounds.extend(AudioSegment.silent(duration=Pause(PauseType.Sentence).silence()))

    # concatenate the audio together
    out = sounds[0]
    for snd in sounds[1:]:
        out += snd

    return out
