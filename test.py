from requests import get, post, delete

# print(get('http://127.0.0.1:8080/api/jobs').json())
#
# print(get('http://127.0.0.1:8080/api/jobs/10').json())
# print(get('http://127.0.0.1:8080/api/jobs/999').json())
# # print(get('http://127.0.0.1:8080/api/jobs/q').json())
#
# print(post('http://127.0.0.1:8080/api/jobs', json={}).json())  # пустой запрос
#
# print(post('http://127.0.0.1:8080/api/jobs',
#            json={'job': 'Работа'}).json())  # не все поля указаны в запросе
#
# print(post('http://127.0.0.1:8080/api/jobs',
#            json={'job': 'Работа',
#                  'id': 8,
#                  'team_leader': 3,
#                  'collaborators': '2, 3, 4'}).json())  # id 8 существует

# print(post('http://127.0.0.1:8080/api/jobs',
#           json={'team_leader': 2,
#                 'job': 'Написание программ',
#                 'collaborators': '3, 4'}).json())
# print(post('http://127.0.0.1:8080/api/jobs',
#          json={'team_leader': 2,
#                 'job': 'Написание программ',
#                'collaborators': '3, 4',
#                 'work_size': 36,
#                 'is_finished': False}).json())

# print(delete('http://127.0.0.1:8080/api/jobs/999').json())  # новости с id = 999 нет в базе
# print(delete('http://127.0.0.1:8080/api/jobs/q').json())  # id строковое, а должно быть числом целым
# print(delete('http://127.0.0.1:8080/api/jobs/11').json())  # корректное удаление
#
# print(get('http://127.0.0.1:8080/api/jobs').json())

print(post('http://127.0.0.1:8080/api/jobs/10', json={}).json())  # пустой запрос
print(post('http://127.0.0.1:8080/api/jobs/10',
           json={'job': 'Работа'}).json())  # не все поля указаны в запросе
print(post('http://127.0.0.1:8080/api/jobs/9',
           json={'id': 9,
                 'team_leader': 2,
                 'job': 'Написание программ 12',
                 'collaborators': '3, 4, 6'}).json())  # корректный запрос
print(get('http://127.0.0.1:8080/api/jobs').json())
