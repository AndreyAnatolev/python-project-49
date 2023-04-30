from random import randint


n = randint(1, 20)
m = randint(1, 7)
progression = []
index_random = randint(1, 9)
for i in range(10):
    n += m
    progression.append(str(n))
answer_correct = progression[index_random]
progression.pop(index_random)
progression.insert(index_random, '..')
print(*progression)
