import re
print(''.join(re.findall(r'[\d+]+', input())))
import re
print(*re.findall(r'[\d+]+', input()), sep='')
