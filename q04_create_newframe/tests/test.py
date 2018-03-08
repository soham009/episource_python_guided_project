import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from inspect import getargspec
from unittest import TestCase
from ..build import q04_create_newframe

path = 'data/episource.txt'
data = q04_create_newframe(path)

features = list(q04_create_newframe(path)['words'])
expected = ['Holmes', 'Masser', 'matter', 'Maberley']

class TestRead_textfile(TestCase):

    def test_read_textfile(self):
        arg = getargspec(q04_create_newframe).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_list(self):
        self.assertEqual(features, expected, "Expected list of variables does not match returned list of variables")
