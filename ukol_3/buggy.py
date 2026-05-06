def prumer(seznam):
    soucet = 0
    for cislo in seznam:
        soucet = soucet + cislo
    return soucet / len(seznam)

def median(seznam):
    serazeny = sorted(seznam)
    n = len(serazeny)
    if n % 2 == 0:
        return (serazeny[n//2 - 1] + serazeny[n//2]) / 2
    else:
        return serazeny[n//2]

def statistiky(data):
    print(f"Průměr: {prumer(data)}")
    print(f"Medián: {median(data)}")
    print(f"Minimum: {min(data)}")
    print(f"Maximum: {max(data)}")
    print(f"Rozsah: {max(data) - min(data)}")

cisla = [4, 7, 2, 9, 1, 5, 8, 3, 6]
statistiky(cisla)