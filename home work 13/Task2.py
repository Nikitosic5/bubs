"""
������� sorted ��������� � �������� ��������������� ��������� key(������ �������� ������������).
� ������� lambda-������� ������������ ���� ������ �������� �� ������
"""
grades = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
    {'name': 'Aaron', 'final': 98}]
sorted_list = sorted(grades, key=lambda x:(x['name']))
print(sorted_list)