from PIL import Image
from urllib.request import urlopen
import argparse

NEW_DIMENSIONS = (200, 200)
url = ""
#img = Image.open(urlopen(url))
def resize_and_place_img(url, output_path='new_image.jpg'):
    img = Image.open(urlopen(url))
    img.resize(NEW_DIMENSIONS)
    img.save(f"../frontend/images/{output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Script for downloading
                                    and reshaping image to fit appropriately
                                    into consistent dimensions""")
    parser.add_argument('url', help="URl to grab initial image from")
    parser.add_argument('output_path', help="Path for final output image")
    args = parser.parse_args()

    resize_and_place_img(args.url, args.output_path)