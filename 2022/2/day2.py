# file_name = 'example.txt'
file_name = 'input.txt'

# Part One

points = {
    'r': 1,
    'p': 2,
    's': 3
}


def hand(input):
    match input:
        case 'A' | 'X':
            return 'r'
        case 'B' | 'Y':
            return 'p'
        case 'C' | 'Z':
            return 's'


def fight(opp_hand, my_hand):
    print(f"opp: {opp_hand}, me: {my_hand}")

    opp_points = 0
    my_points = 0

    # Points for hands
    opp_points += points[opp_hand]
    my_points += points[my_hand]

    if opp_hand == my_hand:
        opp_points += 3
        my_points += 3
    else:
        match [opp_hand, my_hand]:
            case ['r', 's'] | ['p', 'r'] | ['s', 'p']:
                opp_points += 6
            case ['r', 'p'] | ['p', 's'] | ['s', 'r']:
                my_points += 6
    return [opp_points, my_points]


with open(file_name) as f:
    lines = f.read().splitlines()

my_total_score = 0

for line in lines:
    line_split = line.split(' ')
    opp = line_split[0]
    me = line_split[1]
    result = fight(hand(opp), hand(me))
    # print(result)
    my_total_score += result[1]

print(f"\nPart One: {my_total_score}\n")

# Answer: 13565


# Part Two

cues = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}


def cue_hand(opp_hand):
    # Return all possible responses, depending on desired outcome
    match opp_hand:
        case 'r':
            win = 'p'
            draw = 'r'
            lose = 's'
        case 'p':
            win = 's'
            draw = 'p'
            lose = 'r'
        case 's':
            win = 'r'
            draw = 's'
            lose = 'p'
    return {
        'win': win,
        'draw': draw,
        'lose': lose
    }


with open(file_name) as f:
    lines = f.read().splitlines()

my_total_score = 0

for line in lines:
    line_split = line.split(' ')
    opp = line_split[0]
    me = line_split[1]
    opp_hand = hand(opp)
    my_hand = cue_hand(opp_hand)[cues[me]]
    print(cues[me])
    result = fight(opp_hand, my_hand)
    print(result)
    my_total_score += result[1]

print(f"\nPart Two: {my_total_score}\n")

# Answer: 12424
