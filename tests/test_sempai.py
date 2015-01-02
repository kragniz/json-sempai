import os
import shutil
import sys
import tempfile
import unittest

import jsonsempai

TEST_FILE = '''{
    "three": 3,
    "one": {
        "two": {
            "three": 3
        }
    },
    "array": [
        {"nested": "but dotted"},
        {"array": [
            {"and_nested_again": "dotted"}
        ]}
    ],
    "lots_of_lists": [[{"in_da_list": true}]]
}'''


class TestSempai(unittest.TestCase):

    def setUp(self):
        self.direc = tempfile.mkdtemp(prefix='jsonsempai')
        sys.path.append(self.direc)

        with open(os.path.join(self.direc, 'sempai.json'), 'w') as f:
            f.write(TEST_FILE)

    def tearDown(self):
        sys.path.remove(self.direc)
        shutil.rmtree(self.direc)

    def test_import(self):
        with jsonsempai.imports():
            import sempai
        self.assertTrue(sempai is not None)

    def test_access(self):
        with jsonsempai.imports():
            import sempai
        self.assertEqual(3, sempai.three)

    def test_access_nested(self):
        with jsonsempai.imports():
            import sempai
        self.assertEqual(3, sempai.one.two.three)

    def test_acts_like_dict(self):
        with jsonsempai.imports():
            import sempai
        self.assertEqual({"three": 3}, sempai.one.two)

    def test_set(self):
        with jsonsempai.imports():
            import sempai
        sempai.one.two.three = 4
        self.assertEqual(4, sempai.one.two.three)

    def test_del(self):
        with jsonsempai.imports():
            import sempai
        del sempai.one.two.three
        self.assertEqual('not at home',
                         sempai.one.two.get('three', 'not at home'))

    def test_location(self):
        del sys.modules['sempai'] # force the module to be reloaded
        with jsonsempai.imports():
            import sempai
        self.assertEqual(os.path.join(self.direc, 'sempai.json'),
                         sempai.__file__)

    def test_array(self):
        with jsonsempai.imports():
            import sempai
        self.assertEqual({"nested": "but dotted"},
                         sempai.array[0])
    def test_array_dotting(self):
        with jsonsempai.imports():
            import sempai
        self.assertEqual('but dotted', sempai.array[0].nested)

    def test_array_nested_dotting(self):
        with jsonsempai.imports():
            import sempai
        self.assertEqual('dotted', sempai.array[1].array[0].and_nested_again)

    def test_obj_in_list_in_list(self):
        with jsonsempai.imports():
            import sempai
        self.assertTrue(sempai.lots_of_lists[0][0].in_da_list)
