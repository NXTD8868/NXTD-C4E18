
person={
        'name':'duong',
        'job':'student',     #value of key and value can be any date type
        'age':17
        }#dict
print(person['name'])
#r
for key in person:
    print(f'{key}: {person[key]}')
#c
person['height'] = 171
for key in person:
    print(f'{key}: {person[key]}')
#u
person['height'] =172
for key in person:
    print(f'{key}: {person[key]}')
#d
del person['height']
print(person)
#check if key exists:
if 'name' in person:
    print(person['name'])