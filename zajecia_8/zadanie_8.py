def read_file(file_name):
    try:
        with open(file_name, encoding="utf-8") as file:
            words = file.read().split()
        return words
    except FileNotFoundError:
        print(f"Błąd: Plik {file_name} nie został znaleziony.")
        exit()
    except IOError as e:
        print(f"Błąd: Nie można odczytać pliku {file_name}. Szczegóły: {e}")
        exit()
    except Exception as e:
        print(f"Nieoczekiwany błąd podczas odczytu pliku {file_name}. Szczegóły: {e}")
        exit()

def write_file(file_name, words):
    try:
        # Zapis do pliku - maksymalnie 7 słów w kolejnych linijkach
        with open(file_name, "w", encoding="utf-8") as file:
            for i in range(0, len(words), 7):
                file.write(" ".join(words[i:i+7]) + "\n")
    except IOError as e:
        print(f"Błąd: Nie można zapisać pliku {file_name}. Szczegóły: {e}")
        exit()
    except Exception as e:
        print(f"Nieoczekiwany błąd podczas zapisu pliku {file_name}. Szczegóły: {e}")
        exit()

# Dodawanie plików
def add_files(file_a, file_b, file_c):
    words_a = read_file(file_a)
    words_b = read_file(file_b)
    unique_a = [word for word in words_a if word not in words_b]
    unique_b = [word for word in words_b if word not in words_a]
    common = sorted(set(words_a) & set(words_b))
    result = []
    for i in range(max(len(unique_a), len(unique_b))):
        if i < len(unique_a):
            result.append(unique_a[i])
        if i < len(unique_b):
            result.append(unique_b[i])
    result.extend(common)
    write_file(file_c, result)

# Odejmowanie plików
def subtract_files(file_a, file_b, file_c):
    words_a = read_file(file_a)
    words_b = read_file(file_b)
    unique_words = [word for word in words_a if word not in words_b]
    write_file(file_c, unique_words)

# Mnożenie plików
def multiply_files(file_a, file_b, file_c):
    words_a = read_file(file_a)
    words_b = read_file(file_b)
    common = sorted(set(words_a) & set(words_b))
    result = [word for word in common for _ in range(7)]
    write_file(file_c, result)

file_a = "A.txt"
file_b = "B.txt"
file_c_add = "C_dodawanie.txt"
file_c_subtract = "C_odejmowanie.txt"
file_c_multiply = "C_mnozenie.txt"

add_files(file_a, file_b, file_c_add)
subtract_files(file_a, file_b, file_c_subtract)
multiply_files(file_a, file_b, file_c_multiply)