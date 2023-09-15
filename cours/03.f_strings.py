# f-string

mot = "world!"

chaine = "hello " + mot

print(chaine)

python_version = 3.11

fstring = f"hello {mot}, python {python_version + 0.1}"

print(fstring)

habitants = 7_753_000_000
superficie = 149_000_000

print(f"Nb habitants par km²: {round(habitants/superficie, 1)}")