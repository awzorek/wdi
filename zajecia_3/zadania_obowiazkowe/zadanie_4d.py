# d. zmienne
name = "Arkadiusz"
lastname = "Wzorek"
age = 19
favorite_food = "Pizza"
favorite_animal = "Kot"
div_res = 5 / 7

# a. Używając kilku wywołań funkcji print
print("Imię:", name)
print("lastname:", lastname)
print("age:", age)
print("Ulubiona potrawa:", favorite_food)
print("Ulubione zwierzę:", favorite_animal)
print("Wynik dzielenia 5 przez 7 bez dokładności:", div_res)
print("Wynik dzielenia 5 przez 7 z dokładnością do 1 cyfry po przecinku: {:.1f}".format(div_res)) # c.
print("Wynik dzielenia 5 przez 7 z dokładnością do 3 cyfr po przecinku: {:.3f}".format(div_res)) # c.
print("Wynik dzielenia 5 przez 7 z dokładnością do 5 cyfr po przecinku: {:.5f}".format(div_res)) # c.
print("Wynik dzielenia 5 przez 7 z dokładnością do 10 cyfr po przecinku: {:.10f}".format(div_res)) # c.

print()

# b. Używając jednego wywołania funkcji print
print("Imię: {}\nNazwisko: {}\nWiek: {}\nUlubiona potrawa: {}\nUlubione zwierzę: {}\n"
      "Wynik dzielenia 5 przez 7 bez dokładności: {}\n"
      "Wynik dzielenia 5 przez 7 z dokładnością do 1 cyfry po przecinku: {:.1f}\n" # c.
      "Wynik dzielenia 5 przez 7 z dokładnością do 3 cyfr po przecinku: {:.3f}\n" # c.
      "Wynik dzielenia 5 przez 7 z dokładnością do 5 cyfr po przecinku: {:.5f}\n" # c.
      "Wynik dzielenia 5 przez 7 z dokładnością do 10 cyfr po przecinku: {:.10f}".format(  # c.
          name, lastname, age, favorite_food, favorite_animal,
          div_res, div_res, div_res, div_res, div_res))