"""
�������� ��������� ������� ����� ���������� ������������ ���� ����� ���� ������������ �� ������ off.
��������� ������ ��������� lambda-������� ��������� � ������� ����� ������� "�����".
"""
current_list = ['����', '��������', '������', '������', '�����']
new_list = list(map(lambda x: x*'�����',current_list))
print(new_list)