# frst_num = 12
# scnd_num = 1
# thrd_num = 6
# sum = frst_num + scnd_num + thrd_num

# if fres_num > scnd_num and thrd_num < schd_num:
#    max = frst_num
#    min = thrd_num
# elif schd_num > frst_num and thrd_num < frst_num:
#    max = scnd_num
#    min = frst_num
# else:
#    max = thrd_num
#    min = thrd_num
# print('Сумма:", sum, "\nМаксимум:", max, "\nМинимум:", min)
# Doesn't work



frst_num = 12
scnd_num = 1
thrd_num = 6
sum_gen = frst_num + scnd_num + thrd_num
max = max([frst_num, scnd_num, thrd_num])
min = min([frst_num, scnd_num, thrd_num])
print("Сумма:", sum_gen, "\nмаксимум:", max, "\nмаксимум:", min)
