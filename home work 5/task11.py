subjects = list()
subject = input("Введи игру(0-остановить ввод):").lower()

while subject != "0":
    if subject in subjects:
        print("Этот игра уже записана")
    else:
        subjects.append(subject)
    subject = input("Введи игра(0-остановить ввод):").lower()

subjects.sort()
print(subjects)