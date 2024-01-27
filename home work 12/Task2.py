"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open('example_2.txt', 'w') as f:
    f.write('но у меня не получается')
with open('example.txt', 'r') as f:
    a = f.read()
with open('example_2.txt', 'r') as f:
    b = f.read()
with open('example_3.txt', 'w') as f:
    f.write(a + ', ' +b)
