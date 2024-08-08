import os
import subprocess

# Set the environment variable
os.environ['DISTUTILS_USE_SDK'] = '1'

# Run the setup.py script
subprocess.check_call(['python', 'setup.py', 'install'])
