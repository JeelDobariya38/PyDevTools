# # Tests/conftest.py

# import sys
# import os

# # Get the absolute path to the project directory
# project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# # Get the absolute path to the PyDevTools directory
# pydevtools_dir = os.path.join(project_dir, 'PyDevTools')

# # Add PyDevTools to sys.path if it's not already there
# if pydevtools_dir not in sys.path:
#     sys.path.insert(0, pydevtools_dir)



# new code

import sys
import os

# Get the absolute path to the project directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add pydevtools to sys.path if it's not already there
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)