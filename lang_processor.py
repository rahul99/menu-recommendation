# encoding=utf8
import re
import nltk
nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem.porter import PorterStemmer
import unittest

stop_words = set(stopwords.words('english'))

def rm_repeat_chars(inp_str):
    return re.sub(r'(.)(\1){2,}', r'\1\1', inp_str)

def rm_non_english_chars(inp_str: str) -> str:
    # remove non-ascii chars
    return re.sub("([^\x00-\x7F])+"," ",inp_str)

def rm_numbers(inp_str):
    return re.sub(r'[0-9]', '', inp_str)

def rm_stop_words(inp_str: str) -> str:
    word_tokens = word_tokenize(inp_str)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = " ".join(filtered_sentence)
    return filtered_sentence

def stem(inp_str: str) -> str:
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in inp_str]
    stemmed_str = " ".join(stemmed)

def pre_process(inp_str: str) -> str:
    inp_str = inp_str.lower().replace(',', '').replace('(', '').replace(')', '')
    inp_str = rm_repeat_chars(inp_str)
    inp_str = rm_numbers(inp_str)
    inp_str = rm_non_english_chars(inp_str)
    inp_str = rm_stop_words(inp_str)
    inp_tr = stem(inp_str)
    return inp_str


class TestStringMethods(unittest.TestCase):
    def test_pre_process(self):
        inp_str = "This is an example sentence containing repeat chars numbers 79 and non-english ¨∆˚®œ√ and the stop words filtration"
        output = pre_process(inp_str)
        expected = "example sentence containing repeat chars numbers non-english stop words filtration"
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()