"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
feedback = input("место,исполнитель: (off - завершить):")
while feedback != "off":
    print("Спасибо за информацию")
    feedback = input("место,исполнитель: (off - завершить):")

