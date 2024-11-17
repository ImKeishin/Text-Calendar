from Cautare import search
from datetime import datetime

def edit(events):
    index = search(events)
    if index == -1:
        print("Editare esuata !\n")
    else:
        print("Ce doresti sa editezi ?")
        c = 'A'
        while c not in "TIF":
            c = input("Titlul(T), Inceputul(I), Finalul(F)\n>>>")
            if c == 'T':
                name = input("Titlu nou: ")
                events[index].title = name
            elif c == 'I':
                s = input("Inceput nou (YYYY-MM-DD HH:MM): ")
                st = datetime(int(s[:4]), int(s[5:7]), int(s[8:10]), int(s[11:13]), int(s[14:16]))
                events[index].start = st
                events[index].duration = events[index].end - events[index].start
            elif c == 'F':
                f = input("Final nou (YYYY-MM-DD HH:MM): ")
                fin = datetime(int(f[:4]), int(f[5:7]), int(f[8:10]), int(f[11:13]), int(f[14:16]))
                events[index].end = fin
                events[index].duration = events[index].end - events[index].start
            else:
                print("Comanda necunoscuta, incercati din nou !\n")
            print("Editare efectuata !\n")