from setuptools import setup

setup(name='inspectietoolHB',
      version='0.1',
      description='Tool to visualize HB SQLite databases',
      url='https://github.com/menno94/inspectietoolHB',
      author='Menno de ridder',
      author_email='menno-deridder@hotmail.com',
	  long_description=open('README.rst').read(),
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