users: list[dict] = [
    {'name': 'Jakub', 'surname': 'Orłowski', 'posts': 13},
    {'name': 'Janek', 'surname': 'Mielec', 'posts': 20},
    {'name': 'Maciej', 'surname': 'Przybytek', 'posts': 45},
    {'name': 'Bartosz', 'surname': 'Pietrasik', 'posts': 60},
    {'name': 'Tymoteusz', 'surname': 'Miszczak', 'posts': 21},
    {'name': 'Mateusz', 'surname': 'Matysiak', 'posts': 33},]


def read(users:list[dict])-> None:
    for user in users[1:]:
        print(f'Twój znajomy {user['name']} opublikował: {user["posts"]} ')
read(users)