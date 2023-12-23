from PIL import Image

def main():
    # Відкрийте зображення
    img = Image.open("C:/Users/leonid/Desktop/image_3.jpg")

    # Виведіть початкові розміри зображення
    print("Початкові розміри зображення:", img.size)

    # Змініть розміри зображення на 148 x 85 пікселів
    img = img.thumbnail((148, 85), Image.LANCZOS)

    # Виведіть змінені розміри зображення
    print("Змінені розміри:", img.size)

    # Покажіть зображення
    img.show()


if __name__ == "__main__":
    main()
