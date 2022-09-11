import json
import regex as re

PHONOLOGY_FILE = 'dat/PIE_default.json'


class Phonology:
    """

    """

    def __init__(self):
        self.PIE = {}
        self.load_phonology()

    def get(self, key: str) -> str:
        return self.PIE[key]

    def set(self, key: str, value: str) -> None:
        self.PIE[key] = value

    def verify(self, symbol: str) -> bool:
        """
        Determines if the string is a valid (normalized) PIE grapheme.

        Parameters
        ----------
        symbol : str
            Text to verify as a valid symbol in PIE.

        Returns
        -------
        bool
            True if the given symbol is a valid PIE character, False otherwise.
        """
        return symbol in self.PIE

    def load_phonology(self, phonology: str = None) -> None:
        """
        Load the PIE phonology from the give .json file.

        Parameters
        ----------
        phonology : str
            Filename of the .json file containing the phonological mapping.

        Raises
        ------
        ValueError
            If the provided phonology file is not a .json file
        """
        if not phonology:
            phonology = PHONOLOGY_FILE

        if not re.search('.json$', phonology):
            raise ValueError("Phonology map must be .json")

        with open(phonology, 'r', encoding='utf16') as f:
            self.PIE = json.load(f)

    def update_phonology(self, phonology: str) -> bool:
        """
        Updates the default PIE phonology using the provided .json file.

        Parameters
        ----------
        phonology : str
            Filename of the .json file containing the phonological mapping.

        Returns
        -------
        bool
            True if successful, otherwise throws an exception.

        Raises
        ------
        ValueError
            If the provided phonology file is not a .json file
        """
        if not re.search('.json$', phonology):
            raise ValueError("Phonology map must be .json")

        with open(phonology, 'r', encoding='utf16') as f:
            update_PIE = json.load(f)

        # merge phonology
        self.PIE = self.PIE | update_PIE
        return True
