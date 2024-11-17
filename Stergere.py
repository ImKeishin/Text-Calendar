from Cautare import search

def delete(events):
    index = search(events)
    if index == -1:
        print("Stergere esuata !\n")
    else:
        print("Esti sigur(a) ? D/N")
        c = 'A'
        while c not in "DN":
            c = input(">>>")
            if c == 'D':
                events.pop(index)
                print("Stegere efectuata !\n")
            elif c == 'N':
                print("Stergere anulata !\n")
            else:
                print("Comanda necunoscuta, incercati din nou !\n")