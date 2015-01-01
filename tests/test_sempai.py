import os
import shutil
import sys
import tempfile

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


class TestSempai(object):

    def setup(self):
        self.direc = tempfile.mkdtemp(prefix='jsonsempai')
        sys.path.append(self.direc)

        with open(os.path.join(self.direc, 'sempai.json'), 'w') as f:
            f.write(TEST_FILE)

    def teardown(self):
        sys.path.remove(self.direc)
        shutil.rmtree(self.direc)

    def test_import(self):
        with jsonsempai.imports():
            import sempai
        assert sempai

    def test_access(self):
        with jsonsempai.imports():
            import sempai
        assert sempai.three == 3

    def test_access_nested(self):
        with jsonsempai.imports():
            import sempai
        assert sempai.one.two.three == 3

    def test_acts_like_dict(self):
        with jsonsempai.imports():
            import sempai
        assert sempai.one.two == {"three": 3}

    def test_set(self):
        with jsonsempai.imports():
            import sempai
        sempai.one.two.three = 4
        assert sempai.one.two.three == 4

    def test_del(self):
        with jsonsempai.imports():
            import sempai
        del sempai.one.two.three
        assert sempai.one.two.get('three', 'not at home') == 'not at home'

    def test_location(self):
        del sys.modules['sempai'] # force the module to be reloaded
        with jsonsempai.imports():
            import sempai
        assert sempai.__file__ == os.path.join(self.direc, 'sempai.json')

    def test_array(self):
        with jsonsempai.imports():
            import sempai
        assert sempai.array[0] == {"nested": "but dotted"}

    def test_array_dotting(self):
        with jsonsempai.imports():
            import sempai
        assert sempai.array[0].nested == "but dotted"

    def test_array_nested_dotting(self):
        with jsonsempai.imports():
            import sempai
        assert sempai.array[1].array[0].and_nested_again == "dotted"

    def test_obj_in_list_in_list(self):
        with jsonsempai.imports():
            import sempai
        assert sempai.lots_of_lists[0][0].in_da_list == True
