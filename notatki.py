users: list[dict] = [
    {'name': 'Jakub', 'surname': 'Orłowski', 'posts': 13},
    {'name': 'Janek', 'surname': 'Mielec', 'posts': 20},
    {'name': 'Maciej', 'surname': 'Przybytek', 'posts': 45},
    {'name': 'Bartosz', 'surname': 'Pietrasik', 'posts': 60},
    {'name': 'Tymoteusz', 'surname': 'Miszczak', 'posts': 21},
    {'name': 'Mateusz', 'surname': 'Matysiak', 'posts': 33},
    {'name': 'Paweł', 'surname': 'Paszkowski', 'posts': 9},
]


def remove(users: list[dict]) -> None:
    user_name: str = input('Kogo szukasz?: ')
    for user in users[1:]:
         if user['name'] == user_name:
             users.remove(user)
remove(users)
print(users)
