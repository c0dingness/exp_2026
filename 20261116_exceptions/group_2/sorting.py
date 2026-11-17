animals = [
    'ze',
    'bee',
    'dog',
    'cat',
    'zebra',
    'elephant']
animals_clone = animals.copy()

print(animals)
animals.sort(reverse=True)
print(animals)

result = animals.sort()  # in place
print(animals)
print(result)

sorted_animals = sorted(animals_clone)
print(sorted_animals)

print('***')
animals = [
    'ze',
    'bee',
    'dog',
    'cat',
    'zebra',
    'elephant']

animals.sort()
print(animals)
animals.sort(key=lambda x: len(x))
print(animals)


