from tkinter import *


root = Tk() #wywołanie okna rootowego
root.geometry('800x700')
root.title('Map Book')


ramka_lista_uzytkownikow= Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0)

#ramka_lista_obiektow
label_lista_obiektow= Label(ramka_lista_uzytkownikow, text='Lista znajomych:')
listbox_lista_obiektow= Listbox(ramka_lista_uzytkownikow,width=40)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow,text='Pokaż szczegóły')
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow,text='Usuń')
button_edytuj_uzytkownika=Button (ramka_lista_uzytkownikow,text='Edytuj')

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_uzytkownika.grid(row=2, column=1)
button_edytuj_uzytkownika.grid(row=2, column=2)

#ramka z formularzem
label_formularz=Label(ramka_formularz, text='Formularz edycji i dodawania: ')
label_imie= Label(ramka_formularz, text='Imię:')
label_nazwisko= Label(ramka_formularz, text='Nazwisko:')
label_posty=Label(ramka_formularz, text='Posty:')
label_miejscowosc=Label(ramka_formularz, text='Miejscowość:')
entry_imie=Entry(ramka_formularz)
entry_miejscowosc=Entry(ramka_formularz)
entry_nazwisko=Entry(ramka_formularz)
entry_posty=Entry(ramka_formularz)


label_formularz.grid(row=0, column=0, columnspan=3)
label_imie.grid(row=1, column=0,sticky=W)
label_nazwisko.grid(row=2, column=0,sticky=W)
label_posty.grid(row=3, column=0,sticky=W)
label_miejscowosc.grid(row=4, column=0,sticky=W)
entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)
entry_miejscowosc.grid(row=4, column=1)


button_dodaj_uzytkownika=Button(ramka_formularz, text='Dodaj uzytkownika')
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

#ramka szczegóły obiektu
label_opis_obiektu=Label(ramka_szczegoly_obiektow, text='Szczegóły obiektu:')





label_opis_obiektu.grid(row=0, column=0, sticky=W)






root.mainloop()
