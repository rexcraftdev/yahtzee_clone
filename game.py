import random


class Game:
    def __init__(self):
        self.hand = [0, 0, 0, 0, 0]

        self.scores = {
            'aces': 0,
            'twos': 0,
            'threes': 0,
            'fours': 0,
            'fives': 0,
            'sixes': 0,
            '3_kind': 0,
            '4_kind': 0,
            'full_house': 0,
            'sm_straight': 0,
            'lg_straight': 0,
            'yahtzee': 0,
            'chance': 0
        }

        self.vals = [
                self.hand.count(1),
                self.hand.count(2),
                self.hand.count(3),
                self.hand.count(4),
                self.hand.count(5),
                self.hand.count(6)
                ]

    def get_total(self):
        return sum(self.scores.values())

    def roll_hand(self):
        for dice in range(len(self.hand)):
            self.hand[dice] = random.randint(1, 6)
        self.hand = sorted(self.hand)
        print('New hand rolled: {}'.format(self.hand))

        return self.hand

    def reroll_hand(self, values):
        for i, val in enumerate(values):
            if values[i] is not True:
                print(f'Rerolling Dice: {i}')
                self.hand[i] = random.randint(1, 6)
            self.hand = sorted(self.hand)

        return self.hand

    def get_hand(self):
        return self.hand

    def update_hand(self):
        self.vals = [
                self.hand.count(1),
                self.hand.count(2),
                self.hand.count(3),
                self.hand.count(4),
                self.hand.count(5),
                self.hand.count(6)
        ]

    def score_hand(self, cat):
        self.update_hand()

        print(f'scoring hand: {self.vals}')

        if cat == 'aces':
            self.scores['aces'] += (self.vals[0] * 1)
        elif cat == 'twos':
            self.scores['twos'] += (self.vals[1] * 2)
        elif cat == 'threes':
            self.scores['threes'] += (self.vals[2] * 3)
        elif cat == 'fours':
            self.scores['fours'] += (self.vals[3] * 4)
        elif cat == 'fives':
            self.scores['fives'] += (self.vals[4] * 5)
        elif cat == 'sixes':
            self.scores['sixes'] += (self.vals[5] * 6)
        elif cat == '3_kind':
            if 3 in self.vals:
                self.scores['3_kind'] += sum(self.hand)
        elif cat == '4_kind':
            if 4 in self.vals:
                self.scores['4_kind'] += sum(self.hand)
        elif cat == 'full_house':
            if 3 in self.vals and 2 in self.vals:
                self.scores['full_house'] += 25
        elif cat == 'sm_straight':
            if self.vals == [1, 1, 1, 1, 1, 0]:
                self.scores['sm_straight'] += 30
        elif cat == 'lg_straight':
            if self.vals == [0, 1, 1, 1, 1, 1]:
                self.scores['lg_straight'] += 40
        elif cat == 'yahtzee':
            if 5 in self.vals:
                self.scores['yahtzee'] += 50
        elif cat == 'chance':
            self.scores['chance'] += sum(self.hand)

        return self.scores
