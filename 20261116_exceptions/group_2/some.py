s: str = ' Bla-bla;  Ko-ko '

print(s.lower())


class Host:
    name: str


my_list = ['web-p', 'wiki-t', 'gw-01-p']
my_list_as_str = ', '.join(my_list)
print(my_list)
print(my_list_as_str)

text = 'today i am not going to work'
print(text.split())
print(s.split('; '))

print([x.strip() for x in s.split('; ')])

print(s.strip())

s1 = 'word'
s2 = 'ko-ko'

s3 = s1 + ' ' + s2
s4 = f'{s1} {s2}'
