import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from inspect import getargspec
from unittest import TestCase
from ..build import q01_load_data

path = 'data/episource.txt'
data = q01_load_data(path)


class TestRead_textfile(TestCase):

    def test_read_textfile(self):
        arg = getargspec(q01_load_data).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_length(self):
        self.assertEqual(data[1],6227, "The Expected return length of words does not match with the given length of words")
