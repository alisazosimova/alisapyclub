"""

## Игра _секретный Санта_
Требуется написать класс для реализации стратегии 
распеределения игроков.
Класс должен реализовать два публичных метода: 
`submit` & `commit` и один "служебный" метод `_shuffle`

## Интерфейс класса
`submit` принимает как аргумент email участника, 
который хочет принять участие в игре. Его email 
сохраняется в список участников.
`commit` принимает как аргумент email уачстника, 
который зарегистрирован и хочет узнать кому ему 
следует дарить подарок. 
Нельзя дарить подарок самому себе. 
Нельзя передавать email незарегистрированного игрока. 
В обоих некорректных случаях, нужно вызывать ошибку 
`ValueError` (задание _со звездочкой_)

```
class StrategyDraft:
  def submit(self, email):
    pass
  def commit(self, email):
    pass
```

## Стратегия №1
Все участники сначала заявляются (100 раз вызывается 
метод `submit`); 
после происходит _мешанина_ и каждому участнику 
назначется другой участник 
для поздравления (вызывается служебный метод `_shuffle`); 
после все участники приходят и узнают кому 
нужно вручать подарки (100 раз вызывается метод `commit`)


set - переписать lucky
random.choice 

"""
import random
from pprint import pprint

def lucky(a_list, skip_list):
    """
    >>> lucky([1, 2, 3], [1, 3])
    2
    >>> lucky([1, 2, 3], [2])
    1
    """
    for item in a_list:
        if item in skip_list:
            continue
        return item

class Email:
    def __init__(self):
        self.list_of_participants = []
        self.shuffled_list = []
        self.pairs = {}
        

    def submit(self, email):
        return self.list_of_participants.append(email)

    def shuffle(self):
        self.shuffled_list = list(self.list_of_participants)
        random.shuffle(self.shuffled_list)

        
    def make_pairs(self):       
        for email in self.list_of_participants:
            lucky_bastard = lucky(self.shuffled_list, [email])
            self.shuffled_list.remove(lucky_bastard)
            self.pairs[email] = lucky_bastard
        # pprint(self.pairs)

        
    def commit(self, email):
        print(self.pairs[email])
        return self.pairs[email]


    def __repr__(self):
        return 'pairs: ' + str(self.pairs)

        



em = Email()
em.submit("1email@test.com")
em.submit("2email@test.com")
em.submit("3email@test.com")
em.submit("4email@test.com")
em.submit("5email@test.com")
em.submit("6email@test.com")
em.submit("7email@test.com")
em.submit("8email@test.com")
em.shuffle()
print(em)
# pprint(em.shuffled_list)




#em.make_pairs()
#em.commit("1email@test.com")
#em.commit("2email@test.com")

#pprint(list(em.make_pairs()))







import ipdb; ipdb.set_trace()







