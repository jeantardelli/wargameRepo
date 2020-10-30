import setuptools

with open('README', 'r') as f:
    readme = f.read()

setuptools.setup(
    name='gamepkg-jean',
    version='2.0.3',
    packages=['wargame'],
    url='https://pypi.org/project/gamepkg-jean/',
    license='LICENSE.txt',
    description='game pkg real',
    long_description=readme,
    author='jeancarlo',
    author_email='jeantardelli@gmail.com',
    python_requires='>=3',
    )
