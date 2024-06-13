from utils.crude import read, create_user, search_user, remove, update,db_params, add_user, read_db,remove_user_db,update_db
from models.data import users


if __name__ == '__main__':

    print(f'Witaj {users[0]["name"]}! ')
    while True:
        print('Menu:')
        print('0.Zakończ program')
        print('1.Pokaż co u znajomych: ')
        print('2.Dodaj znajomego: ')
        print('3.Wyszukaj znajomego: ')
        print('4.Usuń znajmoego: ')
        print('5.Uaktualnij znajomego')
        menu_option:str=input('Wybierz dostępną funckję z menu: ')
        if menu_option=='0':
            break
        if menu_option == '1':
           read_db(db_params)

        if menu_option == '2':
            create_user(db_params)
        if menu_option == '3':
            search_user(users)
        if menu_option == '4':
            remove_user_db(db_params)
        if menu_option =='5':
              update_db(db_params)
