def overTel(tel):
  cislice = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
  platne = True
  tel = tel.replace(" ", "")

  """Overuji, jestli je predvolba ceska, ale zaroven nechci, 
  aby prijal napriklad cislo 420 777 067 666 - bez pluska na zacatku"""
  if tel[0:4] != '+420' and len(tel) > 9:
    platne = False
  else:
    tel = tel.replace("+", "")

  for i in tel:
    if i not in cislice:
      platne = False

  if len(tel) not in {9, 12}:
    platne = False

  return platne


def smsPrice(sms):

  cena = (len(sms) // 180) * 3
  if (len(sms) % 180) > 0:
    cena += 3

  return cena


tel = input("Zadejte telefonní číslo: ")
platne = overTel(tel)

if platne:
  print(f"Číslo {tel} je platne")
  sms = input("Můžete zadat textovou zprávu: ")
  cena = smsPrice(sms)
  print(f"Za tuto zprávu zaplatíte {cena} Kč.")
else:
  print(f"Cislo {tel} je neplatné, nebo zahraniční, a s tím já pracovat neumím.")