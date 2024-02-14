# count é iterador sem fim
import itertools

c1 = itertools.count(8, 8) # não tem fim
r1 = range(8, 81, 8)

print(f'c1 -> tem __iter__? {hasattr(c1, '__iter__')}')
print(f'c1 -> tem __next__? {hasattr(c1, '__next__')}')
print(f'r1 -> tem __iter__? {hasattr(r1, '__iter__')}')
print(f'r1 -> tem __next__? {hasattr(r1, '__next__')}')

print(c1)
print(next(c1))
print(r1)

print()
print('count')
for i in c1:
    if i > 80: # para ter uma parada forçada
        break
    print(i)

print()
print('range')

for i in r1:
    print(i)