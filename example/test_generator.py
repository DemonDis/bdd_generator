import sys

sys.path.append('..')  # ".." означает один уровень вверх по дереву директорий
from generator_bdd.generator import Person

person = Person("Di", 25)

person.say_hello()