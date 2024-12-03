from main import dodaj_liczby

def test_dodaj_liczby():
	assert dodaj_liczby(2, 3) == 5
	assert dodaj_liczby(-1, 1) == 0
	print("Wszystkie testy przeszły.")
	
test_dodaj_liczby()