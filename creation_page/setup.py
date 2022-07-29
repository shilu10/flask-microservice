# Making the both of the python package as a global packages, so it can be accessed from
# anywhere inside the project.
from setuptools import setup, find_packages  
setup(name = 'server', packages = find_packages())
setup(name = 'app', packages = find_packages())