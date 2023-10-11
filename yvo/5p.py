frst_num = int(input('Введите первое число:'))
scnd_num = int(input('Введите второе число:'))
if frst_num > scnd_num:
    len_btwn_nms = frst_num - scnd_num
else:
    len_btwn_nms = scnd_num - frst_num
print("Разница между введенными числами равна:", len_btwn_nms, "!")
