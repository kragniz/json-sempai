import jsonsempai

import os
import shutil
import sys
import tempfile

TEST_FILE = '''{
"three": 3
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

    def test_access(self):
        import sempai
        assert sempai.three == 3

    def test_location(self):
        import sempai
        assert sempai.__file__ == os.path.join(self.direc, 'sempai.json')
