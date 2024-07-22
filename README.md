# Cucmber generator

<div align="center"><img src="https://github.com/DemonDis/bdd_generator/blob/main/images/InnoLab.png" height="150" alt="Innovation lab"></div>

### Venv
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

### Structure
```
# Создаем страницу Login
├── 📁 generator_bdd/
|   ├── 🐍 __init__.py
|   └── ...  
├── 📁 images/
|   └── InnoLab.png
├──  
└── ...   
```

### Public lib pip
```bash
# generate file for public
python3 setup.py sdist bdist_wheel
# public on https://pypi.org
twine upload --repository pypi dist/*
```

 https://pypi.org/manage/project/GeneratorBdd/releases/#delete_release-modal-1
 https://habr.com/ru/articles/760046/