from random import choice
from pprint import pprint


f = open("./all_leet_code_questions_submitted.txt")

pbms = {line.split('*,')[1] for line in f.readlines()}

pprint(choice(list(pbms)))