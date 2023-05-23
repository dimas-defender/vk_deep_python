from random import randint
from faker import Faker


N = 10000
M = 100

file = open("data.json", "w")
fake = Faker()

for i in range(N // 2):
    file.write("{")
    for j in range(M):
        file.write(f'"{fake.word()}": "{fake.word()}"')
        if j < M - 1:
            file.write(", ")
    file.write("}\n")

for i in range(N // 2):
    file.write("{")
    for j in range(M):
        file.write(f'"{fake.word()}": {randint(100, 10000)}')
        if j < M - 1:
            file.write(", ")
    file.write("}\n")

file.close()