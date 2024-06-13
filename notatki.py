users: list[dict] = [
    {'name': 'Jakub', 'surname': 'Orłowski', 'posts': 13},
    {'name': 'Janek', 'surname': 'Mielec', 'posts': 20},
    {'name': 'Maciej', 'surname': 'Przybytek', 'posts': 45},
    {'name': 'Bartosz', 'surname': 'Pietrasik', 'posts': 60},
    {'name': 'Tymoteusz', 'surname': 'Miszczak', 'posts': 21},
    {'name': 'Mateusz', 'surname': 'Matysiak', 'posts': 33},
    {'name': 'Paweł', 'surname': 'Paszkowski', 'posts': 9},
]




import requests
from bs4 import BeautifulSoup
import psycopg2

db_params=psycopg2.connect(
    user="postgres",database="postgres",host="localhost",port="5432",password="geoinformatyka"
)

def get_coordinates(nazwa_miejscowosci)->list:

    url:str=f'https://pl.wikipedia.org/wiki/{nazwa_miejscowosci}'
    response=requests.get(url)
    # print(response.text)
    response_html=BeautifulSoup(response.text,'html.parser')
    # print(response_html)
    response_html_lat:list=response_html.select('.latitude')[1].text.replace(',','.')
    response_html_lng:list=response_html.select('.longitude')[1].text.replace(',','.')
    print (response_html_lat)
    print (response_html_lng)
    return [response_html_lat,response_html_lng]

# get_coordinates()

def create_user(db_params)-> None:

    name: str = input("Enter your name: ")
    surname: str = input("Enter your surname: ")
    posts: int = int(input("Enter your number of posts: "))
    location: str = input("Enter your location: ")
    new_user: dict = {'name': name, 'surname': surname, 'posts': posts, 'location': location}
    longitude,latitude=get_coordinates(location)
    cursor=db_params.cursor()
    sql=f"INSERT INTO public.users(name, surname, posts, location, cords) VALUES('{name}', '{surname}',{posts}, '{location}', 'SRID=4326;POINT({latitude} {longitude})');"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()


create_user(db_params)


def read_db(db_params)-> None:
    cursor=db_params.cursor()
    sql=f"SELECT * FROM public.users"
    cursor.execute(sql)
    users=cursor.fetchall()
    cursor.close()
    for user in users:
        print(user)

read_db(db_params)
def remove_user_db(db_params)-> None:
    cursor=db_params.cursor()
    sql=f"DELETE FROM public.users WHERE name='{input('Kogo usunąć?')}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()
remove_user_db(db_params)