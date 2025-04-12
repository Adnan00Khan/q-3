import random

def get_random_quote():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

if __name__ == "__main__":
    print("Your random quote:")
    print(get_random_quote())