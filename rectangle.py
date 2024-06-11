def draw_rectangle(width, height, char):
    char = char[0]  # Ensure only the first character is used
    for _ in range(height):
        print(char * width)

if __name__ == "__main__":
    width = int(input("Breite: "))
    height = int(input("Höhe: "))
    char = input("Zeichen: ")
    draw_rectangle(width, height, char)
