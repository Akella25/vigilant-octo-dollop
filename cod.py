# run `pip install pillow` before
# make sure you have `requests` lib installed
# use https://pillow.readthedocs.io/en/stable/handbook/tutorial.html for reference

from PIL import Image
import requests
import os

URL = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"


def load_image(url):
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(os.path.join(os.getcwd(), "img1.jpg"))


def print_imaged_data(file):
    image = Image.open(file)
    print(image.size, image.mode)


def is_square_image(file):
    image = Image.open(file)
    return not image.size[0] != image.size[1]


def create_thumbnail(file):
    # TODO: handle all errors on thumbnail creation
    if not os.path.isfile(file):
        raise FileNotFoundError("File not exist")
    else:
        thumbnail_size = (200, 200)
        image = Image.open(file)
        image.thumbnail(thumbnail_size)
        image.save("thumbnail.jpg", "JPEG")


def is_thumbnail(file):
    thumbnail_size = [200, 200]
    image = Image.open(file)
    return image.size == thumbnail_size


def rotate_image(file, degrees):
    image = Image.open(file)
    rotated = image.rotate(degrees, expand=True)
    rotated.save("rotated.jpg")


def flip_image(file, direction):
    directions = {"LR": Image.FLIP_LEFT_RIGHT, "TB": Image.FLIP_TOP_BOTTOM}
    image = Image.open(file)
    out = image.transpose(directions[direction])
    out.save('flipped.jpg')


def copy_images_to_dir(dirname):
    '''Copies all images from current folder into subfolder'''

    for file in os.listdir():
        if file.endswith(".jpg"):
            image = Image.open(file)
            image.save(os.path.join(os.getcwd(), dirname, image.filename))


def delete_images(file_name):
    for file in os.listdir():
        if file.endswith(".jpg"):
            if file == file_name:
                os.remove(file_name)
                return f"File {file_name} removed"
            else:
                return f"File {file_name} isn't found"


# TODO: create a function that will save rectangle area from given image to the separate file
# with name 'rectangle.jpg'. Coordinates of rectangle have to be passed as tuple of 4 integers

def create_rectangle(file_name, tmp_tuple):
    image = Image.open(file_name)
    out = image.crop(tmp_tuple)
    out.save("rectangle.jpg", quality=95)


# if __name__ == "__main__":
#     create_rectangle("img1.jpg", (1000, 1750, 3000, 2500))
#     load_image(URL)
#     print_imaged_data("img1.jpg")
#     print(is_square_image("img1.jpg"))
#     create_thumbnail("img2.jpg")
#     is_thumbnail("thumbnail.jpg")
#     rotate_image("img1.jpg", 90)
#     flip_image("img1.jpg", 'TB')
#     copy_images_to_dir("images")
#     print(delete_images("img1.jpg"))
#     print("Done!")


from PIL import Image
import requests
import threading
import os

URL1 = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"
URL2 = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
URL3 = "https://media.wired.co.uk/photos/60c8730fa81eb7f50b44037e/3:2/w_3329,h_2219,c_limit/1521-WIRED-Cat.jpeg"
URL4 = "https://st3.depositphotos.com/1186248/14934/i/1600/depositphotos_149344592-stock-photo-open-sign-on." \
       "-a-window.jpg"
URL5 = "https://st2.depositphotos.com/3837271/5468/i/950/depositphotos_54688255-stock-photo-less-is-more-sign.jpg"


def load_image(url, save_image_name):
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(os.path.join(os.getcwd(), save_image_name))


thr1 = threading.Thread(target=load_image, args=(URL1, "imageURL1.png",))
thr2 = threading.Thread(target=load_image, args=(URL2, "imageURL2.jpg",))
thr3 = threading.Thread(target=load_image, args=(URL3, "imageURL3.jpg",))
thr4 = threading.Thread(target=load_image, args=(URL4, "imageURL4.jpg",))
thr5 = threading.Thread(target=load_image, args=(URL5, "imageURL5.jpg",))

thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr5.start()
