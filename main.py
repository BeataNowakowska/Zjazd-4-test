jednosci = [
    "zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem",
    "dziewięć"
]

nastki = [
    "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście",
    "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"
]

dziesiatki = [
    "", "", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt",
    "sześćdziesisiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewiędziesiąt"
]


def zamien_jedna(liczba):
    wynik = ""
    if liczba < 0:
        wynik = "minus "
        liczba = abs(liczba)

    if liczba > 19:
        wynik += dziesiatki[liczba // 10] + " "
        if liczba % 10 != 0:
            wynik += jednosci[liczba % 10]
    else:
        if liczba > 9:
            wynik += nastki[liczba % 10]
        else:
            wynik += jednosci[liczba]


def sprawdz_zakres_i_zamien_jedna_liczbe():
    print("Podaj liczbę do zamiany")
    liczba = int(input())
    if liczba <= -100 or liczba >= 100:
        print("Poza zakresem")
    else:
        print(zamien_jedna(liczba))


def zamieniaj_w_petli():
    repeat = True
    while repeat:
        sprawdz_zakres_i_zamien_jedna_liczbe()
        print("\nKonwertujemy następną?")
        repeat = input() in ["t", "T", "tak", "Tak", "TAK", "ok"]
        print("-------------------------------------")


zamieniaj_w_petli()
