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

        with open(os.path.join(self.direc, 'test_sempai.json'), 'w') as f:
            f.write(TEST_FILE)

    def teardown(self):
        shutil.rmtree(self.direc)

    def test_import(self):
        import test_sempai
