# Cucmber generator

<div align="center"><img src="https://github.com/DemonDis/bdd_generator/blob/main/images/InnoLab.png" height="150" alt="Innovation lab"></div>

### Venv (Linux/Mac)
```bash
# add venv
python3.12 -m venv .venv
# activate venv
. .venv/bin/activate
# install lib
pip3 install -r requirements.txt
# update pip
pip install --upgrade pip
```

### Venv (Windows)
```bash
# add venv
python -m venv .venv
# activate venv
.venv\Scripts\activate.bat
# install lib
pip3 install -r requirements.txt
# exit venv
deactivate
```

### Structure
```
# Создаем страницу Login
├── 📁 generator_bdd/
|   ├── 🐍 __init__.py
|   └── ...  
├── 📁 images/
|   └── InnoLab.png
├──  📋 .env
├──  📋 .gitignore
├──  📋 LICENSE
├──  📝 README_PY.md
├──  📝 README.md
├──  💾 requirements.txt
├──  🔩 setup.cfg
└──  🐍 setup.py  
```

### Public lib pip
```bash
# generate file for public
python3 setup.py sdist bdist_wheel
# public on https://pypi.org
twine upload --repository pypi dist/*
```
 
### Information
[Создание библиотеки Python: полный гайд](https://habr.com/ru/articles/760046/)  