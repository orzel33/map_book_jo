

from tkinter import *
import requests
from bs4 import BeautifulSoup
import tkintermapview
import psycopg2

db_params=psycopg2.connect(
    user="postgres",database="postgres",host="localhost",port="5432",password="geoinformatyka"
)

users=[]
class User:
    def __init__(self, name, surname, posts, location, coords):
        self.imie = name
        self.nazwisko = surname
        self.posty = posts
        self.miejscowosc = location
        self.coords= coords
        self.marker= map_widget.set_marker(float(self.coords.split(' ')[1][0:-1]), self.coords.split(' ')[0][6:], text=f"{self.imie}")

def get_coords(location):
    adres_url = f'https://pl.wikipedia.org/wiki/{location}'
    response = requests.get(adres_url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    # print  (response_html)
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    print([latitude, longitude])
    return ([latitude, longitude])

def dodaj_uzytkownika():
    name=entry_imie.get()
    surname=entry_nazwisko.get()
    posts=entry_posty.get()
    location=entry_miejscowosc.get()
    user= User(name, surname, posts, location)
    users.append(user)


    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_imie.focus()

    longitude, latitude = get_coords(location)
    cursor=db_params.cursor()
    sql=f"INSERT INTO public.users(name, surname, posts, location, coords) VALUES('{name}', '{surname}',{posts}, '{location}', 'SRID=4326;POINT({latitude} {longitude})');"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()
    print(user.imie)
    lista_uzytkownikow()
def lista_uzytkownikow():
    listbox_lista_obiektow.delete(0, END)
    for user in users:
        user.marker.delete()
    cursor = db_params.cursor()
    sql = f"SELECT id,name,surname,posts,location,st_astext(coords) FROM public.users"
    cursor.execute(sql)
    users_db = cursor.fetchall()
    cursor.close()
    for idx, user in enumerate(users_db):
        listbox_lista_obiektow.insert(idx, f'{user}')
        user = User(user [1],user [2], user[3], user[4], user[5])
        users.append(user)

def pokaz_szczegoly_uzytkownika():
    i=listbox_lista_obiektow.index(ACTIVE)
    print(i)
    imie=users[i].imie
    nazwisko=users[i].nazwisko
    posty=users[i].posty
    miejscowosc=users[i].miejscowosc
    map_widget.set_position(users[i].coords[0],users[i].coords[1])
    map_widget.set_zoom(15)

    label_imie_szczegoly_wartosc.config(text=imie)
    label_nazwisko_szczegoly_wartosc.config(text=nazwisko)
    label_posty_szczegoly_wartosc.config(text=posty)
    label_miejscowosc_szczegoly_wartosc.config(text=miejscowosc)

def usun_uzytkownika():
    i=listbox_lista_obiektow.index(ACTIVE)
    cursor=db_params.cursor()
    sql=f"DELETE FROM public.users WHERE name='{users[i].imie}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()
    users[i].marker.delete()
    users.pop(i)
    lista_uzytkownikow()

def edytuj_uzytkownika():
    i=listbox_lista_obiektow.index(ACTIVE)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)

    entry_imie.insert(0, users[i].imie)
    entry_nazwisko.insert(0, users[i].nazwisko)
    entry_posty.insert(0, users[i].posty)
    entry_miejscowosc.insert(0, users[i].miejscowosc)
    button_dodaj_uzytkownika.config(text="Zapisz zmiany",command=lambda:aktualizuj_uzytkownika(i))

def aktualizuj_uzytkownika(i):
    users[i].imie=entry_imie.get()
    users[i].nazwisko=entry_nazwisko.get()
    users[i].posty=entry_posty.get()
    users[i].miejscowosc=entry_miejscowosc.get()
    users[i].coords= get_coords(users[i].miejscowosc)
    users[i].marker.delete()
    users[i].marker = map_widget.set_marker(users[i].coords[0], users[i].coords[1], text=f"{users[i].imie}")
    cursor = db_params.cursor()
    sql = f"UPDATE public.users SET name='{users[i].imie}', surname='{users[i].nazwisko}', posts='{users[i].posty}', location='{users[i].miejscowosc}', coords='SRID=4326;POINT({users[i].coords[1]} {users[i].coords[0]})' WHERE name='{users[i].name}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)

    button_dodaj_uzytkownika.config(text='Dodaj uzytkownika',command=dodaj_uzytkownika)



root=Tk()
root.geometry('800x700')
root.title('Map Book')


ramka_lista_uzytkownikow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektu=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2, padx=50, pady=20)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_uzytkownikow, text='Lista znajomych:')
listbox_lista_obiektow=Listbox(ramka_lista_uzytkownikow,width=30)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow, text='Pokaż szczegóły',command=pokaz_szczegoly_uzytkownika)
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow, text='Usuń',command=usun_uzytkownika)
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow, text='Edytuj',command=edytuj_uzytkownika)

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_uzytkownika.grid(row=2, column=1)
button_edytuj_uzytkownika.grid(row=2, column=2)

# ramka_formulaz

label_formularz=Label(ramka_formularz,text='Formularz edycji dodawania')
label_imie=Label(ramka_formularz,text='Imię:')
label_nazwisko=Label(ramka_formularz,text='Nazwisko:')
label_posty=Label(ramka_formularz,text='Posty:')
label_miejscowosc=Label(ramka_formularz,text='Miejscowość:')
entry_imie=Entry(ramka_formularz)
entry_nazwisko=Entry(ramka_formularz,width=30)
entry_posty=Entry(ramka_formularz)
entry_miejscowosc=Entry(ramka_formularz)

label_formularz.grid(row=0, column=0, columnspan=3)
label_imie.grid(row=1, column=0,sticky=W)
label_nazwisko.grid(row=2, column=0,sticky=W)
label_posty.grid(row=3, column=0,sticky=W)
label_miejscowosc.grid(row=4, column=0,sticky=W)
entry_imie.grid(row=1, column=1, sticky=W)
entry_nazwisko.grid(row=2, column=1, sticky=W)
entry_posty.grid(row=3, column=1, sticky=W)
entry_miejscowosc.grid(row=4, column=1, sticky=W)

button_dodaj_uzytkownika=Button(ramka_formularz, text='Dodaj użytkownika',command=dodaj_uzytkownika)
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

# ramka szczegóły obiektu
label_opis_obiektu=Label(ramka_szczegoly_obiektu, text='Szczegóły obiektu')
label_imie_szczegoly=Label(ramka_szczegoly_obiektu, text='Imie:')
label_imie_szczegoly_wartosc=Label(ramka_szczegoly_obiektu, text='...',width=10)
label_nazwisko_szczegoly=Label(ramka_szczegoly_obiektu, text='Nazwisko:')
label_nazwisko_szczegoly_wartosc=Label(ramka_szczegoly_obiektu, text='...',width=10)
label_posty_szczegoly=Label(ramka_szczegoly_obiektu, text='Posty:')
label_posty_szczegoly_wartosc=Label(ramka_szczegoly_obiektu, text='...',width=10)
label_miejscowosc_szczegoly=Label(ramka_szczegoly_obiektu, text='Miejscowość:')
label_miejscowosc_szczegoly_wartosc=Label(ramka_szczegoly_obiektu, text='...',width=10)

label_opis_obiektu.grid(row=0, column=0,sticky=W)
label_imie_szczegoly.grid(row=1, column=0)
label_imie_szczegoly_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly.grid(row=1, column=2)
label_nazwisko_szczegoly_wartosc.grid(row=1, column=3)
label_posty_szczegoly.grid(row=1, column=4)
label_posty_szczegoly_wartosc.grid(row=1, column=5)
label_miejscowosc_szczegoly.grid(row=1, column=6)
label_miejscowosc_szczegoly_wartosc.grid(row=1, column=7)






map_widget=tkintermapview.TkinterMapView(ramka_szczegoly_obiektu,width=700,height=400)
map_widget.grid(row=2, column=0, columnspan=8)
map_widget.set_position(52.21, 21.0)
map_widget.set_zoom(5)



root.mainloop()