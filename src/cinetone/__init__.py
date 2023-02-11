import imageio as iio
import argparse
from PIL import Image   
import numpy as np
import os

def main():
    parser = argparse.ArgumentParser(prog = 'cinetone',description = '',epilog = '')
    parser.add_argument("video_file",help="Path to the video file to be decoded")
    args = parser.parse_args()

    if not os.path.isfile(args.video_file):
        print("Given path is not a file!")
        return

    pix_list = []
    rowcnt   = 0
    colscnt  = 0

    for frame in iio.imiter(args.video_file):

        if rowcnt == 0 or colscnt == 0:
            rowcnt  = frame.shape[0]
            colscnt = frame.shape[1]

        img = Image.fromarray(frame)
        pix_list.append(img.resize((1, 1), resample=0).getpixel((0,0)))
    
    im = Image.new(mode="RGB",size=(len(pix_list),1))
    im.putdata(pix_list)
    im = im.resize((500,200))
    im.show()

    

main()