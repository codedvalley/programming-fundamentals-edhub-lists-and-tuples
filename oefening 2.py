# ==========================================
# Opdracht 2:
# In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen: 1, 1, 2, 3, 5, 8 enzovoorts
# De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. Implementeer de functie ‘fibonacci’ die een lijst als parameter meekrijgt.
# Voer de volgende opdrachten uit:
# - Maak een variabele aan genaamd 'fibonacci_start_reeks' en geef  die de eerste twee elementen van de Fibonacci reeks.
# - Maak een functie genaamd fibonacci die de fibonacci_reeks uitbreidt met een nieuw element.
# - Roep de functie 5 keer aan (Bijvoorbeeld met een for-loop).
# - Print de waarde van de fibonacci_reeks
#
# Verwachte uitkomst:   [1, 1, 2, 3, 5, 8, 13]
# ==========================================
fibonacci_start_reeks = [1, 1]

def fibonacci(fibonacci_reeks):
    nieuw_getal = fibonacci_reeks[-1] + fibonacci_reeks[-2]
    fibonacci_reeks.append(nieuw_getal)

for i in range(5):
    fibonacci(fibonacci_start_reeks)

print(fibonacci_start_reeks)





# Maak een functie verdubbel(x) die een getal verdubbelt en het resultaat teruggeeft.
# Voorbeeld:
#
# print(verdubbel(7))
#
#
# moet 14 tonen.

def verdubbel(x):
    return (x * 2)
x = 7

print(verdubbel(x))
