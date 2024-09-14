from PIL import Image
from urllib.request import urlopen
import argparse

HEIGHT, WIDTH = (200, 200)
url = ""
#img = Image.open(urlopen(url))
def resize_and_place_img(url=None, output_path='./new_image.jpg'):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Script for downloading
                                    and reshaping image to fit appropriately
                                    into consistent dimensions""")
    parser.add_argument('url', help="URl to grab initial image from")
    parser.add_argument('output_path', help="Path for final output image")
    parser.parse_args()