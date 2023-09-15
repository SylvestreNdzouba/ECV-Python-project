print("/n")

int
str
float
bool

age = int(input("Quel est votre age ?"))
print(f"Vous avez {age}ans")
print(2023 - age)

annee_str = str(2023)
print(type(annee_str))
print(int(annee_str[-2:]))

int(str(annee_str)[-2:])