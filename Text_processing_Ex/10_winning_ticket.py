winning_symbols = ["@", "#", "$", "^"]


def is_not_valid(ticket):
    if len(ticket) != 20:
        print("invalid ticket")
        return True
    return False


def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol in ticket:
            if ticket.count(winning_symbol) == 20:
                print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
                return True
    return False


def is_winning_ticket(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for winning_symbol in winning_symbols:
        if winning_symbol * 9 in left_half and winning_symbol * 9 in right_half:
            print(f'ticket "{ticket}" - 9{winning_symbol}')
            return True
        elif winning_symbol * 8 in left_half and winning_symbol * 8 in right_half:
            print(f'ticket "{ticket}" - 8{winning_symbol}')
            return True
        elif winning_symbol * 7 in left_half and winning_symbol * 7 in right_half:
            print(f'ticket "{ticket}" - 7{winning_symbol}')
            return True
        elif winning_symbol * 6 in left_half and winning_symbol * 6 in right_half:
            print(f'ticket "{ticket}" - 6{winning_symbol}')
            return True
    return False


tickets = [ticket.strip() for ticket in input().split(",")]

for ticket in tickets:
    if is_not_valid(ticket):
        pass
    elif is_jackpot(ticket):
        pass
    elif is_winning_ticket(ticket):
        pass
    else:
        print(f'ticket "{ticket}" - no match')

