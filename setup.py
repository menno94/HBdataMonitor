from setuptools import setup

setup(name='inspectietoolHB',
      version='0.3',
      description='Tool to visualize HB SQLite databases',
      url='https://github.com/menno94/inspectietoolHB',
      author='Menno de ridder',
      author_email='menno.deridder@deltares.nl',
	  long_description=open('README.md').read(),
	  long_description_content_type='text/markdown',
      license='MIT',
      packages=['inspectietoolHB'],
	  install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'sqlite',
		],
	python_requires='>=3, <4',
      zip_safe=False)