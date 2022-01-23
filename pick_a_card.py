import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []
random.shuffle(diamonds)
while True:
    user = input("Press enter to pick a card, or Q then enter to quit: ")
    if user == "Q" :
        break
    else: 
        random_card = random.choice(diamonds)
        diamonds.remove(random_card)
        hand.append(random_card)
        print("Remaining cards: " ,diamonds)
        print("Your Hand: " ,hand)
    if not diamonds:
        print("There are no more cards to pick. ",hand)
        break
   
 
