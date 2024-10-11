# a. Używając funkcji służącej do wysyłania danych na standardowe wyjście (kilka wywołań).
print("Imię: Arkadiusz")
print("Nazwisko: Wzorek")
print("Wiek: 19")
print("Ulubiona potrawa: Pizza")
print("Ulubione zwierzę: Kot")
print("Wynik dzielenia 5 przez 7 bez dokładności: {}".format(5 / 7))
print("Wynik dzielenia 5 przez 7 z dokładnością do 1 cyfry po przecinku: {:.1f}".format(5 / 7)) # c.
print("Wynik dzielenia 5 przez 7 z dokładnością do 3 cyfr po przecinku: {:.3f}".format(5 / 7)) # c.
print("Wynik dzielenia 5 przez 7 z dokładnością do 5 cyfr po przecinku: {:.5f}".format(5 / 7)) # c.
print("Wynik dzielenia 5 przez 7 z dokładnością do 10 cyfr po przecinku: {:.10f}".format(5 / 7)) # c.

print()

# b. Używając funkcji służącej do wysyłania danych na standardowe wyjście (jedno wywołanie).
print("Imię: Arkadiusz\nNazwisko: Wzorek\nWiek: 19\nUlubiona potrawa: Pizza\nUlubione zwierzę: Kot\n"
      "Wynik dzielenia 5 przez 7 bez dokładności: {}\n"
      "Wynik dzielenia 5 przez 7 z dokładnością do 1 cyfry po przecinku: {:.1f}\n" # c.
      "Wynik dzielenia 5 przez 7 z dokładnością do 3 cyfr po przecinku: {:.3f}\n" # c.
      "Wynik dzielenia 5 przez 7 z dokładnością do 5 cyfr po przecinku: {:.5f}\n" # c.
      "Wynik dzielenia 5 przez 7 z dokładnością do 10 cyfr po przecinku: {:.10f}".format(5 / 7, 5 / 7, 5 / 7, 5 / 7, 5 / 7)) # c.