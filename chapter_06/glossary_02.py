# 6-4. Glossary 2

glossary = {
    'variables': 'containers for storing data values.',
    'list': 'A collection of items in particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'A collection which is ordered and unchangeable.',
    'set': 'An unordered collection with no duplicate elements',
    'string': 'A sequence of characters.',
    'boolean': 'A logical data type that can only have the values true or false.',
    'loop': ' the repetitive execution of a set of instructions until a specified condition is met',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
