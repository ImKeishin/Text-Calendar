from datetime import datetime

def view(events, mode):
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    found = False
    if mode == 0:
        for e in events:
            if e.start.year == year and e.start.month == month and e.start.day == day:
                e.print()
                found = True
    elif mode == 1:
        for e in events:
            if e.start.year == year and e.start.month == month:
                e.print()
                found = True
    elif mode == 2:
        for e in events:
            if e.start.year == year:
                e.print()
                found = True
    else:
        print("\nIntrodu intervalul dorit:\n")
        s = input("Inceput (YYYY-MM-DD HH:MM): ")
        e = input("Final (YYYY-MM-DD HH:MM): ")
        st = datetime(int(s[:4]), int(s[5:7]), int(s[8:10]), int(s[11:13]), int(s[14:16]))
        end = datetime(int(e[:4]), int(e[5:7]), int(e[8:10]), int(e[11:13]), int(e[14:16]))
        found = False
        for e in events:
            if e.inBounds(st, end):
                e.print()
                found = True
    if not found:
        print("Niciun eveniment gasit !\n")
    c = input("\n\nApasa orice tasta pentru a termina aceasta actiune !")
