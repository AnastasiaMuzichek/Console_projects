import requests
import json


HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://sullygnome.com/channel/lirik',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8'
}
NAME_JSON = 'result.json'


def generate_list_emails():
    list_emails = []
    for i in range(100):
        list_emails.append(f'some.email.{i}@mail.ru')
    return list_emails


print('\nВыполнение задания\n')

emails = generate_list_emails()
result = {'results': []}

for email in emails:
    payload = {'email': email}
    request = requests.get('https://account.mail.ru/api/v1/golang/user/password/support', headers=HEADERS, params=payload)
    answer = json.loads(request.text)

    if 'email' in answer:
        answer = {'email': email, 'status': 'exist', 'id': answer['body']['id'], 'last_mod': answer['last_modified']}
    else:
        answer = {'email': email, 'status': answer['body']['email']['error']}
    result['results'].append(answer)

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)
    json_file.close()

exit(0)
