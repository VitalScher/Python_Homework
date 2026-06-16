from adress import Adress
from mailing import Mailing

mailing = Mailing(to_adress = Adress("100200", "Энск", "ул. Прямая", "д.5", "кв.2"),
                  from_adress = Adress("200400", "Уйск", "ул. Кривая", "д.53", "кв.124"),
                  cost = 100.2, 
                  track = "7654532")

print(mailing)