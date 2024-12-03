def powitanie(imie):
	print(f"Cześć, {imie}!")

def dodaj_liczby(a, b):
	return a + b

if __name__ == "__main__":
	imie = input("Podaj swoje imię: ")
	powitanie(imie)

	a = int(input("Podaj pierwszą liczbę: "))
	b = int(input("Podaj drugą liczbę: "))

	wynik = dodaj_liczby(a, b)
	print(f"Wynik dodawania {a} i {b} to: {wynik}")