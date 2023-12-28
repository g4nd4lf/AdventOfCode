def royal(card: str):
    return 'TJQKA'.index(card) + 10


def royal2(card: str):
    return 'TQKA'.index(card) + 10 if card != 'J' else 0


def get_rank_joker(sorted_cards):
    rank = None
    match sorted_cards:
        case [1, 1, 1, 1, 99] | [1, 1, 1, 99, 99] | [1, 1, 99, 99, 99] | [1, 99, 99, 99, 99] | [99, 99, 99, 99, 99]:
            rank = 6  # five of a kind
        case [1, 1, 1, 2, 99] | [1, 2, 2, 2, 99] | [1, 1, 2, 99, 99] | [1, 2, 2, 99, 99] | [1, 2, 99, 99, 99]:
            rank = 5  # four of a kind
        case [1, 1, 2, 2, 99]:
            rank = 4  # full house
        case [1, 1, 2, 3, 99] | [1, 2, 2, 3, 99] | [1, 2, 3, 3, 99] | [1, 2, 3, 99, 99]:
            rank = 3  # three of a kind
        case [1, 2, 3, 4, 99]:
            rank = 1  # one pair
    return rank


def get_rank(sorted_cards):
    rank = None
    match sorted_cards:
        case [1, 1, 1, 1, 1]:
            rank = 6
        case [1, 1, 1, 1, 2] | [1, 2, 2, 2, 2]:
            rank = 5
        case [1, 1, 1, 2, 2] | [1, 1, 2, 2, 2]:
            rank = 4
        case [1, 1, 1, 2, 3] | [1, 2, 2, 2, 3] | [1, 2, 3, 3, 3]:
            rank = 3
        case [1, 1, 2, 2, 3] | [1, 2, 2, 3, 3] | [1, 1, 2, 3, 3]:
            rank = 2
        case [1, 1, 2, 3, 4] | [1, 2, 2, 3, 4] | [1, 2, 3, 3, 4] | [1, 2, 3, 4, 4]:
            rank = 1
        case [1, 2, 3, 4, 5]:
            rank = 0
    return rank


class Hand:
    def __init__(self, cards: str, part2=False):
        self.cards = [int(card) if card.isdigit() else royal(card) if not part2 else royal2(card) for card in cards]
        self.part2 = part2

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)

    def rank(self):
        sorted_cards = sorted(self.cards)

        current = None
        count = 0
        for i in range(len(sorted_cards)):
            if sorted_cards[i] != current:
                count += 1
                current = sorted_cards[i]
            sorted_cards[i] = count

        rank = get_rank(sorted_cards)

        return rank

    def rank2(self):
        sorted_cards = sorted([card if card else 99 for card in self.cards])

        current = None
        count = 0
        for i in range(len(sorted_cards)):
            if sorted_cards[i] != current:
                count += 1
                current = sorted_cards[i]
            sorted_cards[i] = count if sorted_cards[i] != 99 else 99

        if 99 not in sorted_cards:
            rank = get_rank(sorted_cards)
        else:
            rank = get_rank_joker(sorted_cards)

        return rank

    def __lt__(self, other: 'Hand'):
        self_rank, other_rank = (self.rank(), other.rank()) if not self.part2 else (self.rank2(), other.rank2())

        if self_rank == other_rank:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                return self.cards[i] < other.cards[i]
        else:
            return self_rank < other_rank


def main(file, part2):
    
    with open(file) as f:
        hands = []
        for line in map(str.strip, f.readlines()):
            hands.append((Hand(line.split()[0], part2), int(line.split()[1])))

    hands.sort(key=lambda h: h[0])

    ret = 0
    for i in range(len(hands)):
        print(f'{i + 1} - hand: {hands[i][0]}, bid: {hands[i][1]}')
        ret += (1 + i) * hands[i][1]

    return ret


if __name__ == '__main__':
    print(main('input.txt', False))

    print(main('sample.txt', True))