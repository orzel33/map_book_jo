
def read(users:list[dict])-> None:
    for user in users[1:]:
        print(f'Twój znajomy {user['name']} opublikował: {user["posts"]} ')

def create_user(users:list[dict])->None:
    name: str = input('podaj imie użytkownika: ')
    surname: str = input('podaj nazwisko użytkownika: ')
    posts: str = int(input('podaj liczbę postów: '))
    user: dict = {'name': name, 'surname': surname, 'posts': posts}
    users.append(user)


