from random import choice
from pprint import pprint


pprint(choice(list(list({line.split('*,')[1] for line in open("./all_leet_code_questions_submitted.txt").readlines()}))))