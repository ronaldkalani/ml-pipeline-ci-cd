import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import add

def test_add():
    assert add(2, 3) == 5

