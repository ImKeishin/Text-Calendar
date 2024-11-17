from colorama import init, Back, Fore
from os import system
from time import sleep

import datetime
import calendar

from Vizualizare import view
from Adaugare import add
from Editare import edit
from Stergere import delete
from Cautare import search

if __name__ == "__main__":
    luni = ("IANUARIE", "FEBRUARIE", "MARTIE", "APRILIE", "MAI", "IUNIE", "IULIE", "AUGUST", "SEPTEMBRIE", "OCTOMBRIE", "NOIEMBRIE", "DECEMBRIE")
    events = []

    cal = calendar.TextCalendar(calendar.MONDAY)
    curr_day = datetime.date.today()
    curr_month = cal.formatmonth(curr_day.year, curr_day.month)
    init(autoreset=True)
    mode = 1  # 0 - day 1 - month 2 - year

    while True:
        system("cls")
        print(curr_month.split(str(curr_day.day))[0], end='')
        print(Back.WHITE + Fore.BLACK + str(curr_day.day), end='')
        print(curr_month.split(str(curr_day.day))[1])
        print("\n       MENIU\n")
        print(Back.BLUE + Fore.BLACK + "1. Vizualizeaza evenimente" + " " +
              Back.GREEN + Fore.BLACK + "2. Adauga eveniment" + " " +
              Back.MAGENTA + Fore.BLACK + "3. Editeaza eveniment" + " " +
              Back.RED + Fore.BLACK + "4. Stergere eveniment" + " " +
              Back.YELLOW + Fore.BLACK + "5. Schimba mod vizualizare" + " " +
              Back.CYAN + Fore.BLACK + "6. Cautare eveniment")
        choice = int(input("\n-> "))
        print("\n\n")
        if choice == 1:
            print("\n       VIZUALIZARE EVENIMENTE", end=' ')
            if mode == 0:
                print(f"(ZI, {curr_day.day})\n")
            elif mode == 1:
                print(f"(LUNA, {luni[curr_day.month - 1]})\n")
            elif mode == 2:
                print(f"(AN, {curr_day.year})\n")
            else:
                print("(PERSONALIZAT)\n")
            if len(events) == 0:
                print("Nu aveti evenimente adaugate !\n")
                sleep(2)
            else:
                view(events, mode)
        elif choice == 2:
            print("\n       ADAUGARE EVENIMENT\n")
            add(events)
            sleep(3)
        elif choice == 3:
            print("\n       EDITARE EVENIMENT\n")
            edit(events)
            sleep(3)
        elif choice == 4:
            print("\n       STERGERE EVENIMENT\n")
            delete(events)
            sleep(3)
        elif choice == 5:
            print("\n       SCHIMBARE MOD\n")
            mode = int(input("0 - Zi\n1 - Luna\n2 - An\n3 - Personalizat\n>>>"))
        elif choice == 6:
            print("\n       CAUTARE EVENIMENT")
            search(events)
            sleep(2)
        else:
            print("\nComanda necunoscuta, incearca din nou !\n")
            sleep(2)