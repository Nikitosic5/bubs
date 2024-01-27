def is_divisible_by_6(number):
    lst_str_digits = list(str(abs(number)))
    lst_digits = list(map(int, lst_str_digits))
    sum_digits = sum(lst_digits)
    if (sum_digits % 3 == 0) and (lst_digits[-1] % 2 == 0):
        return f'Число {number} делится на 6'
    else:
        return f'Число {number} неделимо на 6'