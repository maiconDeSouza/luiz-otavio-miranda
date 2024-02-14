def gen_1():
    yield 1
    yield 2
    yield 3

def gen_str():
    yield 'a'
    yield 'b'
    yield 'c'

def gen_2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6

for i in gen_2(gen_1):
    print(i)
print()
for i in gen_2(gen_str):
    print(i)