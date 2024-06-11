import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 0
    guess = None

    while guess != secret_number:
        guess = int(input(f"{attempts + 1}. Versuch: Was ist die Geheimzahl? "))
        attempts += 1
        if guess < secret_number:
            print("Die eingegebene Zahl ist zu klein")
        elif guess > secret_number:
            print("Die eingegebene Zahl ist zu groß")

    print(f"Gratulation! Das Geheimnis {secret_number} wurde nach {attempts} Versuchen erraten.")

if __name__ == "__main__":
    guess_number()
