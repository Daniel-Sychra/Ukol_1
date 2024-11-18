"""
Ukol_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Sychra
email: daniel.sychra@gmail.com
"""

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = [
    '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


def login():
    username = input("Zadejte uživatelské jméno: ")
    password = input("Zadejte heslo: ")
    if username in users and users[username] == password:
        print(f"Ahoj, {username}! Vítejte zpět.")
        return True
    else:
        print("Neplatné přihlašovací údaje. Program bude ukončen.")
        return False


def select_text():
    print("Vyberte text k analýze (1, 2, 3):")
    try:
        choice = int(input())
        if 1 <= choice <= 3:
            return TEXTS[choice - 1]
        else:
            print("Neplatný výběr. Program bude ukončen.")
            return None
    except ValueError:
        print("Neplatný vstup. Program bude ukončen.")
        return None


def analyze_text(text):
    words = text.split()
    word_count = len(words)
    title_case_count = sum(1 for word in words if word.istitle())
    upper_case_count = sum(1 for word in words if word.isupper())
    lower_case_count = sum(1 for word in words if word.islower())
    number_count = sum(1 for word in words if word.isdigit())
    number_sum = sum(int(word) for word in words if word.isdigit())

    print(f"Počet slov: {word_count}")
    print(f"Počet slov začínajících velkým písmenem: {title_case_count}")
    print(f"Počet slov psaných velkými písmeny: {upper_case_count}")
    print(f"Počet slov psaných malými písmeny: {lower_case_count}")
    print(f"Počet čísel: {number_count}")
    print(f"Suma všech čísel: {number_sum}")

    
    word_lengths = [len(word) for word in words]
    length_freq = {length: word_lengths.count(length) for length in set(word_lengths)}

    print("\nČetnost délek slov:")
    for length, freq in sorted(length_freq.items()):
        print(f"{length}: {'*' * freq}")


if login():
    text = select_text()
    if text:
        analyze_text(text)
