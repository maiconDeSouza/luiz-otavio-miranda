name = 'Dante Parrudo Kiko III'
new_name = ''
index = 0

while index < len(name):
    letter = name[index]
    if letter == ' ':
        index += 1
        new_name += '* '
    else:
        index += 1
        new_name += f'*{letter}'
    if index == len(name):
        new_name += '*'

print(new_name)