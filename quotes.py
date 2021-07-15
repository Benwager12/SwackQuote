import random

def pull_random_quote():

    with open("quotes.txt", "r") as file:
        all_q = set(range(1, len(file.read().splitlines()) +1))

    with open("quote_history.txt", "r") as file:
        good_q = sorted(all_q - set(map(int, file.read().splitlines()[-100:])))

    random.shuffle(good_q)
    shortlist = random.sample(good_q, 50)

    random.shuffle(shortlist)
    quote = random.choice(shortlist)

    with open("quote_history.txt", "a") as file:
        file.write(f"{quote}\n")

    return quote
