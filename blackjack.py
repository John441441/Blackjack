import random



class Cards:

    card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']


class Gamer:

    card = []


    def two_cards(self):
        count = 2
        while count > 0:
            self.card.append(random.choice(Cards.card))
            count -= 1
        print('Ваши карты: {}'.format(self.card))
        return self.card

    def new_card(self):
        while True:
            answer = input('Вы хотите взять ещё одну карту? ').lower()
            if answer == 'да':
                self.card.append(random.choice(Cards.card))
                print('Ваши карты: {}'.format(self.card))
            else:
                break

    def quantity_point(self):
        point = 0
        for i in self.card:
            if isinstance(i, int):
                point += int(i)
            elif i == 'Валет' or i == 'Дама' or i == 'Король':
                point += 10
            elif point <= 21:
                point += 11
            else:
                point += 1
        print('\nВаши карты: {}'.format(self.card))
        print('Сумарное количество очков игрока: {}'.format(point))
        if point > 21:
            print('Игра окончена!')
            return point
        return point


class Dealer:

    card = []


    def two_cards(self):
        count = 2
        while count > 0:
            self.card.append(random.choice(Cards.card))
            count -= 1

    def new_card(self):
        while True:
            answer = random.randint(0, 1)
            if answer == 0:
                self.card.append(random.choice(Cards.card))
                return self.card
            else:
                break

    def quantity_point(self):
        point = 0
        for i in self.card:
            if isinstance(i, int):
                point += int(i)
            elif i == 'Валет' or i == 'Дама' or i == 'Король':
                point += 10
            elif point <= 21:
                point += 11
            else:
                point += 1
        print('Карты дилера: {}'.format(self.card))
        print('Сумарное количество очков дилера: {}'.format(point))
        return point




g1 = Gamer()
g1.two_cards()
g1.new_card()
d1 = Dealer()
d1.two_cards()
d1.new_card()
r1 = g1.quantity_point()
r2 = d1.quantity_point()




if r2 < r1 <= 21 or r2 > 21:
    print('Победил игрок!')
elif r1 < r2 <= 21 or r1 > 21:
    print('Победил дилер!')
else:
    print('Ничья')


