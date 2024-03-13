from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/5').json())
# print(get('http://localhost:8080/api/v2/users/52').json())  # нет пользователя
# # print(get('http://localhost:8080/api/v2/users/q').json())  # не число
#
# print(post('http://localhost:8080/api/v2/users').json())  # нет словаря
# print(post('http://localhost:8080/api/v2/users', json={'name': 'Sonya'}).json())  # не все поля
# print(post('http://localhost:8080/api/v2/users', json={'name': 'Sonya', 'position': 'junior programmer',
#                                                        'surname': 'Wolf', 'age': 17, 'address': 'module_3',
#                                                        'speciality': 'computer sciences',
#                                                        'hashed_password': 'wolf', 'email': 'wolf@mars.org'}).json())
#
# print(delete('http://localhost:8080/api/v2/users/999').json())  # id = 999 нет в базе
# # print(delete('http://localhost:8080/api/v2/users/10').json())
