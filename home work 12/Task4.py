"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и  проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
"""
def analyze_file(filename):
    word_count = {}
    max_count = 0
    max_words = []
    with open(filename, 'r') as file:
        for line in file:
            # Разделение строки на слова и удаление пробелов и знаков препинания
            words = line.lower().split()
            words = [w.strip('.,!?') for w in words]

            for word in words:
                # Подсчет количества встречающихся слов
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

                # Обновление максимального количества и списка слов
                if word_count[word] > max_count:
                    max_count = word_count[word]
                    max_words = [word]
                elif word_count[word] == max_count:
                    max_words.append(word)

    return max_words
filename = input("Введите имя файла для обработки: ")
most_common_words = analyze_file(filename)

if len(most_common_words) == 1:
    print("Наиболее часто встречающееся слово в файле:", most_common_words[0])
else:
    print("Наиболее часто встречающиеся слова в файле:", ", ".join(most_common_words))