from PIL import Image


def main():
    # Откройте исходное изображение
    img = Image.open("image.jpg")

    # Выведите исходное изображение
    img.show()

    # Измените размер изображения на 148 x 85 пикселей
    img = img.thumbnail((148, 85), Image.BICUBIC)

    # Выведите измененное изображение
    img.show()

    # Сохраните измененное изображение
    img.save((r"image_1.jpg"))


if __name__ == "__main__":
    main()



   

