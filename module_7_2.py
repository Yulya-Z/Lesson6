from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    str_num = 0
    str_byte = file.seek(0)
    for string in strings:
        file.write(string + '\n')
        str_num += 1
        strings_position[str_num, str_byte] = string
        str_byte = file.tell()
    file.close()
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

