from address import Address
from mailing import Mailing

mailing = Mailing(to_address=Address("100200", "г.Энск", "ул.Прямая", "д.5", "кв.2"),
                  from_address=Address("200400", "г.Уйск", "ул.Кривая", "д.53", "кв.124"),
                  cost=100.2,
                  track="7654532")

print(mailing)
