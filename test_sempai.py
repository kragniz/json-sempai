import jsonsempai

import os
import shutil
import sys
import tempfile

TEST_FILE = '''{
    "three": 3,
    "one": {
        "two": {
            "three": 3
        }
    }
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
        import sempai
        assert sempai

    def test_access(self):
        import sempai
        assert sempai.three == 3

    def test_access_nested(self):
        import sempai
        assert sempai.one.two.three == 3

    def test_acts_like_dict(self):
        import sempai
        assert sempai.one.two == {"three": 3}

    def test_set(self):
        import sempai
        sempai.one.two.three = 4
        assert sempai.one.two.three == 4

    def test_del(self):
        import sempai
        del sempai.one.two.three
        assert sempai.one.two.get('three', 'not at home') == 'not at home'

    def test_location(self):
        import sempai
        assert sempai.__file__ == os.path.join(self.direc, 'sempai.json')
