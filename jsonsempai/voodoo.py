import sys

from .sempai import SempaiContextLoader

sys.meta_path.append(SempaiContextLoader)
