import random

liczba = range(48, 57)
duza_litera = range(65, 90)
mala_litera = range(97, 122)

password = ''

pierwsza_partia = ''
druga_partia = ''
trzecia_partia = ''

for i in range(2):
    pierwsza_partia += chr(random.choice(liczba))

    druga_partia += chr(random.choice(duza_litera))

    trzecia_partia += chr(random.choice(mala_litera))

password = pierwsza_partia + druga_partia + trzecia_partia

password = ''.join(random.sample(password, len(password)))

i = 0

while i == 0:
    print("Twoje wylogowane hasło to: ", password)


       





















