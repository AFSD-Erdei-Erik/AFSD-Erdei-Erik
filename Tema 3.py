meniu = ["papanasi"] * 10 + ["cafea"] * 3 + ["gulas"] * 6
preturi = [["papanasi", 7], ["cafea", 10], ["gulas", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"] # coada FIFO
comenzi = ["gulas", "cafea", "cafea", "papanasi", "cafea"] # coada FIFO
tavi = ["tava"] * 7 # stiva LIFO
istoric_comenzi = []

# Retrieve all elements in the list
print(meniu[:])
# 1. Comenzi
print("## Comenzi")
while studenti and comenzi:
    student = studenti.pop(0)
    comanda = comenzi.pop (0)
    tava = tavi.pop()
    istoric_comenzi.append(comanda)
    print(f"{student}) a comandat {comanda}.")

# 2. Inventar
print("\n## Inventar")
comanda_count = {}
for comanda in istoric_comenzi:
    comanda_count[comanda] += 1
else:
    comanda_count[comanda] = 1

print(f"S-au comandat {comanda_count["gulas]} gulas, {comanda_count["]cafea"]} cafea, {comanda_count["papanasi"]} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")

for produs, pret in preturi
    :if produs == "cafea":
       print(f"Mai este cafea: {meniu.count(produs) > 0}.")
    if produs == "papanasi":
       print(f"Mai sunt papanasi: {meniu.count(produs) > 0}.")

# 3. Finante
print("\n## Finante")
total_incasari = 0
for comanda in istoric_comenzi:
    for produs, pret in preturi:
        if comanda == produs:
            total_incasari += pret

print(f"Cantina a incasat: {total_incasari} lei.")
print(f"Produse care costa cel mult 7 lei: {[(produs, pret) for produs, pret in preturi if pret <= 7]}")
