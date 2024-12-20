import random

def play_game():
    nombre_mystere = random.randint(1, 100)
    atempt_number = 7

    while atempt_number > 0:
        print(f"Il vous reste {atempt_number} essais.")
        
        # Condition for invalid input (non-numeric input)
        guess = input("Devine le nombre mystère : ")
        if not guess.isdigit():
            print("Le terme saisi est invalide !")
            continue

        guess = int(guess)

        # Check if the guess is correct
        if guess > nombre_mystere:
            print("Trop grand !")
        elif guess < nombre_mystere:
            print("Trop petit !")
        elif guess == nombre_mystere:
            break

        atempt_number -= 1

    # Display the result
    if guess == nombre_mystere:
        print(f"Bravo ! Vous avez trouvé le nombre mystère en {7 - atempt_number} essais.")
    else:
        print(f"Vous avez échoué. Le nombre mystère était {nombre_mystere}.")

# Main loop
while True:
    play_game()

    # Ask if the user wants to continue
    continuer = input("Voulez-vous continuer (o/n) : ")
    if continuer.lower() != "o":
        break

print("À bientôt !")
print("-" * 100)
