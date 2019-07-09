from PIL import image

def load_img(image_file):
    return Image.open(image_file)

def show_img(image_file):
    return_file.show(title=None)

def save_img(Image_file, newfile):
    image_file.save(newfile, "JPEG")

def main():
    img = load_img("bruh.jpg")
    show_img(img)
    save_img(img, "Okay")

def obamicon():
    darkblue = (0,51,76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)


main()
