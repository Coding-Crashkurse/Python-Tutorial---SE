import fastapi
from fastapi import FastAPI
from fastapi import FastAPI as F
from fastapi import *


from main_package.b import my_b
from main_package.a import my_a, my_a2

my_b()

my_a()
my_a2()
