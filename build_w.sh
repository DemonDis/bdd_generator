# setuptools
pip3 install setuptools
# twine
pip3 install twine
# error: invalid command 'bdist_wheel'
pip install wheel
# generate file for public
python3 setup.py sdist bdist_wheel
# public on https://pypi.org
twine upload --repository pypi dist/*