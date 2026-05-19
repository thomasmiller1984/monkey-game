import random
import time

print("🐒 Willkommen, druже, в Banana-Spiel!")
print("Du musst schnell drücken: a, s oder d, ja?")
print("У тебе є 10 шансів. Los geht's, поїхали!\n")

keys = ['a', 's', 'd']
score = 0

for i in range(10):
    banana = random.choice(keys)
    print(f"Banane kommt runter! Schnell drücken: {banana} !!!")

    start_time = time.time()
    user_input = input("Dein move, Bruder: ")
    reaction_time = time.time() - start_time

    if user_input == banana and reaction_time < 2:
        print("🍌 Gut gemacht, gefangen! Молодець!\n")
        score += 1
    else:
        print("❌ Nein nein... du bist zu langsam oder falsch 😢\n")

print(f"Spiel ist fertig, ja. Dein score: {score}/10")

if score == 10:
    print("🐒 Affe ist sehr glücklich! Du bist Banana-Meister!!!")
elif score > 5:
    print("🙂 Nicht schlecht, Affe sagt danke.")
else:
    print("😢 Affe hat Hunger... wo sind Banane...")
