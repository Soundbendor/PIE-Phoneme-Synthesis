"""
Text blurbs used for the About tab in the Streamlit app.
"""

# How to use
about_Use = "To use this tool, first select the Phonology to use. " \
            "For each phoneme in PIE, select a symbol in IPA to represent that sound. " \
            "You may set each consonant and vowel. You can also map vowel-semivowel diphthongs, choose the treatment " \
            "of accent, and set coloring rules for vowels adjacent to laryngeals. \n  \n "
about_Use += "Next select the text to synthesize. You can choose from a 'Random Word' selected from " \
             "[Wiktionary](https://en.wiktionary.org/wiki/Category:Proto-Indo-European_lemmas). You can re-synthesis " \
             "any text to generate a slightly different pronunciation. "
about_Use += "Additionally, you can synthesis the longer passages " \
             "['Schleicher's Fable'](https://en.wikipedia.org/wiki/Schleicher%27s_fable) or " \
             "['The King and the god'](https://en.wikipedia.org/wiki/The_king_and_the_god). " \
             "For comparison, you can listen to an expert linguist pronounce these tales " \
             "[here](https://www.archaeology.org/exclusives/articles/1302-proto-indo-european-schleichers-fable). \n  \n  "
about_Use += "You may also 'Enter Text' to add your own PIE text to synthesize. Note: the characters you enter " \
             "must be valid characters in the " \
             "[Proto-Indo-European](https://en.wiktionary.org/wiki/Wiktionary:About_Proto-Indo-European) language " \
             "or you will receive an error. " \
             "However, we support and automatically remap older transcription forms, such as  *k̂ and *k̑ 🡒 *ḱ."

# About PIE language
about_PIE_text = "[Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language) (PIE) is the " \
                 "reconstructed ancestor of all [Indo-European languages](" \
                 "https://en.wikipedia.org/wiki/Indo-European_languages). PIE is hypothesized to have been spoken as " \
                 "a single language sometime during the late Neolithic through the Early Bronze Age (between 4500 to " \
                 "2500 BCE). According to the [Kurgan hypothesis](https://en.wikipedia.org/wiki/Kurgan_hypothesis), " \
                 "the language likely originated in the [Pontic-Caspian steppe](" \
                 "https://en.wikipedia.org/wiki/Pontic%E2%80%93Caspian_steppe) of eastern Europe.  \n  \n "
about_PIE_text += "Over the following centuries, waves of Indo-European (IE) peoples migrated across much of the " \
                  "Eurasian continent. As they dispersed, their language split and underwent shifts in " \
                  "pronunciation, changes in morphology, and acquisitions of new vocabulary. This process continued " \
                  "for centuries, resulting in the 449 extant [daughter languages](" \
                  "https://en.wikipedia.org/wiki/Indo-European_languages), spoken by more than 3.5 billion people " \
                  "today.  \n  \n  "
about_PIE_text += "There is no historical record of PIE. Like other proto languages, the language was meticulously " \
                  "reconstructed using the [comparative method](https://en.wikipedia.org/wiki/Comparative_method). " \
                  "We do not know precisely what PIE sounded like, " \
                  "and we may never will. Although linguistics have largely converged on the [set of phonemes](" \
                  "https://en.wikipedia.org/wiki/Proto-Indo-European_phonology) in PIE, " \
                  "there remains ongoing debate about the specific pronunciation of some sounds, such as " \
                  "the [stops](https://en.wikipedia.org/wiki/Glottalic_theory), " \
                  "the [dorsals](https://en.wikipedia.org/wiki/Centum_and_satem_languages), " \
                  "the [laryngeals](https://en.wikipedia.org/wiki/Laryngeal_theory). " \

about_Limitations = "Given our process concatenating different phonetic sounds from different languages, the " \
                    "synthesized speech sounds robotic as we do not attempt prosodic interpretation. " \
                    "Additionally, we missing several potential sounds, " \
                    "such as /qʷ/ /ɢʷ/ and /ɢʷʰ/, which are exceedingly rare in the world's extant languages. " \
                    "In these cases, we provide alternate di-graphs as imperfect substitutions. \n  \n  "
about_Limitations += "For these reasons, it is not possible to accurately synthesis speech for this reconstructed " \
                     "language. This tool is intended for research purposes as a flexible 'calculator' " \
                     "to explore different hypothetical pronunciations of PIE. \n  " \
                     "As such, the synthesized speech should be considered an approximation of PIE, " \
                     "rather than historically accurate renditions."

# About TTS tool
about_Tool = "This is a text-to-speech system for the Proto-Indo-European language that uses phonetic concatenative " \
             "synthesis. Using [Swadesh lists](https://en.wiktionary.org/wiki/Appendix:Swadesh_lists), we synthesized " \
             "words from 100 different languages using the [espeak-ng](https://github.com/espeak-ng/espeak-ng) " \
             "formant synthesizer. We split these words into individual phones using [Praat](" \
             "https://www.fon.hum.uva.nl/praat/) and saved them to a database. \n \n "
about_Tool += "To synthesize PIE speech for a specific word, we randomly select phonetic sounds from our database of " \
              "individual phonetic sounds that match the target phoneme. For more natural pronunciations, " \
              "we prioritize matching two or three consecutive phones from a single source when available.  "

# About Author
about_Author = "This tool was designed by [Patrick Donnelly](https://eecs.oregonstate.edu/people/donnelly-patrick) " \
               "and the [Soundbendor lab](https://soundbendor.org/) at [Oregon State University](" \
               "https://eecs.oregonstate.edu/). "
