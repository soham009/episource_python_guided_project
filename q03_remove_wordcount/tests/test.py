import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from inspect import getargspec
from unittest import TestCase
from ..build import q03_remove_wordcount

path = 'data/episource.txt'
data = q03_remove_wordcount(path)


class TestRead_textfile(TestCase):

    def test_read_textfile(self):
        arg = getargspec(q03_remove_wordcount).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_length(self):
        self.assertEqual(data.shape ,(221,2), "The Expected return shape does not match with the return shape")
