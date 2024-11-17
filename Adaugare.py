from datetime import datetime
from Event import Event

def add(events):
    name = input("Titlu eveniment: ")
    s = input("Cand va incepe evenimentul (YYYY-MM-DD HH:MM): ")
    e = input("Cand se va termina evenimentul (YYYY-MM-DD HH:MM): ")
    st = datetime(int(s[:4]), int(s[5:7]), int(s[8:10]), int(s[11:13]), int(s[14:16]))
    en = datetime(int(e[:4]), int(e[5:7]), int(e[8:10]), int(e[11:13]), int(e[14:16]))
    events.append(Event(name, st, en))
    print("Adaugare efectuata !\n")