import re
import pandas as pd

def read_data(file_name):
    df = pd.read_csv(file_name, header=None)
    return df

def clean_hash_ment(text):
    text = text.replace("\n", " ")
    clean_text = re.sub("@[A-Za-z0-9_]+", "", text)
    clean_text = re.sub("#[A-Za-z0-9_]+", "", clean_text)
    return clean_text

def check_regex(text):
    text = re.sub(r'[^a-z\s]+', '', text, flags=re.IGNORECASE)
    return text


def remove_diacritics(text):
    # define the mapping from diacritic characters to non-diacritic characters
    mapping = {
        '\u00c7': 'C', '\u00e7': 'c',
        '\u011e': 'G', '\u011f': 'g',
        '\u0130': 'I', '\u0131': 'i',
        '\u015e': 'S', '\u015f': 's',
        '\u00d6': 'O', '\u00f6': 'o',
        '\u00dc': 'U', '\u00fc': 'u',
        '\u0152': 'OE', '\u0153': 'oe',
        '\u0049': 'I', '\u0131': 'i',
    }

    # replace each diacritic character with its non-diacritic counterpart
    text = ''.join(mapping.get(c, c) for c in text)

    return text