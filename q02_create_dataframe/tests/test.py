import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from inspect import getargspec
from unittest import TestCase
from ..build import q02_create_dataframe

path = 'data/episource.txt'
data = q02_create_dataframe(path)


class TestRead_textfile(TestCase):

    def test_read_textfile(self):
        arg = getargspec(q02_create_dataframe).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_length(self):
        self.assertEqual(data.shape ,(1552,2), "The Expected return shape does not match with the return shape")
