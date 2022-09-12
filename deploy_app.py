import streamlit as st

from src.app.fetcher import fetch_word
from src.app.sampler import sheep_and_horses, king_and_god, vocab_word

# Title and Icon
# alternate: \U0001F304
from src.app.app_utils import load_map, display_definition, speak
from src.app.phonology_select import add_phonology
from src.phone.phonology import Phonology

st.set_page_config(page_title="PIE Text-to-Speech", page_icon='\U0001F5EF')
st.title('Proto-Indo-European Text to Speech')

# initial random word
rand_word_dict = fetch_word()
if 'random_word' not in st.session_state:
    st.session_state['random_word'] = rand_word_dict

# Phonology tab
with st.expander("Select Phonology"):
    phonology = Phonology()
    add_phonology(phonology)
    load_map(phonology)

# Audio modes
word_tab, text_tab, sheep_story_tab, king_story_tab = st.tabs(
    ['Random Word', 'Enter Text', '"Sheep and the Horses"', '"King and the god"'])

# Random word tab
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

# Free text  tab
with text_tab:
    txt = 'óynos, dwóh₁, tréyes, kʷetwóres, pénkʷe'
    text_input = st.text_area('Enter text:', txt, help='Enter PIE text to synthesis to speech')
    speak_button_text = st.button('Speak', key='speak_button_text', help='Synthesize speech')
    freetext_audio_container = st.container()

# Sheep story tab
with sheep_story_tab:
    title_str = '### **[' + sheep_and_horses['title'] + '](' + sheep_and_horses['url'] + ')**'
    st.write(title_str)
    st.write(sheep_and_horses['eng'])
    st.success(sheep_and_horses['pie'])
    speak_button_sheep = st.button('Speak', key='speak_button_sheep', help='Synthesize speech')
    sheep_audio_container = st.container()

# King story tab
with king_story_tab:
    title_str = '### **[' + king_and_god['title'] + '](' + king_and_god['url'] + ')**'
    st.write(title_str)
    st.write(king_and_god['eng'])
    st.success(king_and_god['pie'])
    speak_button_king = st.button('Speak', key='speak_button_king', help='Synthesize speech')
    king_audio_container = st.container()

# speak random word
if random_word_button:
    if vocab_select == 'Wiktionary':
        # display a random word from Wiktionary
        rand_word_dict = fetch_word()
        st.session_state['random_word'] = rand_word_dict
        display_definition(random_word_container, rand_word_dict)
        speak(phonology, random_word_audio_container, rand_word_dict['word'], pauses=False, spectrogram=True)
    else:
        # fetch from specific word list
        vocab_word_dict = fetch_word(vocab_word(vocab_select))
        st.session_state['random_word'] = vocab_word_dict
        display_definition(random_word_container, vocab_word_dict)
        speak(phonology, random_word_audio_container, vocab_word_dict['word'], pauses=False, spectrogram=True)

# repeat random word
if word_speak_button:
    display_definition(random_word_container, st.session_state['random_word'])
    speak(phonology, random_word_audio_container, st.session_state['random_word']['word'], pauses=False, spectrogram=True)

# speak free text
if speak_button_text:
    speak(phonology, freetext_audio_container, text_input, pauses=True, spectrogram=True)

# speak Sheep story
if speak_button_sheep:
    speak(phonology, sheep_audio_container, sheep_and_horses['pie'], pauses=True, spectrogram=False)

# speak King story
if speak_button_king:
    speak(phonology, king_audio_container, king_and_god['pie'], pauses=True, spectrogram=False)
