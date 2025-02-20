from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

def readme():
  with open('README_PY.md', 'r') as f:
    return f.read()

setup(
  name='generator_cucumber',
  version='0.0.2',
  author='Dmitry Shibikin',
  author_email='dmitry.shibikin@yandex.ru',
  description='Generation .feature file',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/DemonDis/bdd_generator',
  packages=find_packages(),
  install_requires=REQUIREMENTS,
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='python cucmber generator',
  project_urls={
    'Documentation': 'https://github.com/DemonDis/bdd_generator'
  },
  python_requires='>=3.8'
)