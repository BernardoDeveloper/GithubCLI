import PIL.Image

ASCII_CHARACTERS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width=100):
    width, heigth = image.size
    ratio = heigth / width
    new_height = int(new_width * ratio)

    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join([ASCII_CHARACTERS[pixel//25] for pixel in pixels])

def convert_image_to_ascii(path, new_width=100):
    # path = "image.jpg"
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is a not valid path")

    new_image_data = pixels_to_ascii(grayify(resize(image)))

    pixel_count = len(new_image_data)
    return "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))