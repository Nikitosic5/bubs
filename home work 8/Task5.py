"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""


num_pupils = int(input())
lang_union = set()
lang_intersect = set()
for i in range(num_pupils):
    num_cur_lang = int(input())
    cur_set = {input() for j in range(num_cur_lang)}
    if i != 0:
        lang_union &= cur_set
    else:
        lang_union = cur_set
    lang_intersect |= cur_set

print(len(lang_union))
print('\n'.join(lang_union))

print(len(lang_intersect))
print('\n'.join(lang_intersect))
