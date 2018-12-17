from setuptools import setup

setup(name='beheertoolHB',
      version='0.5.1',
      description='Tool to visualize HB SQLite databases',
      url='https://github.com/menno94/beheertoolHB',
      author='Menno de ridder',
      author_email='menno.deridder@deltares.nl',
	  long_description=open('README.md').read(),
	  long_description_content_type='text/markdown',
      license='MIT',
      packages=['beheertoolHB'],
	  python_requires='>=3, <4',
      zip_safe=False)