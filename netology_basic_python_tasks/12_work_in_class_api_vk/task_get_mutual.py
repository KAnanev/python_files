import requests

TOKEN = ''

source_user = 577250478
target_user = 355405083
list_users = []


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return str(f'https://vk.com/id{self.user_id}')

    def __and__(self, other):
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params={
                'access_token': TOKEN,
                'source_uid': other.user_id,
                'target_uid': other.user_id,
                'v': '5.103'
            }
        )

        for i in response.json()['response']:
            user = User(i)
            list_users.append(user)
        [print(i) for i in list_users]


edzo = User(source_user)
kati = User(target_user)

edzo & kati

# print(edzo)
# print(list_users[0])

