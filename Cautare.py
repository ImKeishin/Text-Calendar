def search(events):
    name = input("Titlu eveniment: ")
    position = 0
    ev = []
    for e in events:
        if e.title == name:
            ev.append((e, position))
        position += 1
    if len(ev) == 0:
        print("Niciun eveniment gasit !\n")
        return -1
    else:
        print("Selecteaza evenimentul din cele disponibile:\n")
        index_list = range(1, len(ev) + 1)
        for i in index_list:
            print(f"{i}: {ev[i - 1][0].start}  ->  {ev[i - 1][0].end}")
        while True:
            index = int(input(">>>"))
            if index in index_list:
                return ev[index - 1][1]
            else:
                print("Pozitie incorecta, incercati din nou !\n")