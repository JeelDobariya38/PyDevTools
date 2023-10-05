# Tests/conftest.py

import sys
import os

# Get the absolute path to the project directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Get the absolute path to the Pyutils directory
pyutils_dir = os.path.join(project_dir, 'Pyutils')

# Add Pyutils to sys.path if it's not already there
if pyutils_dir not in sys.path:
    sys.path.insert(0, pyutils_dir)
