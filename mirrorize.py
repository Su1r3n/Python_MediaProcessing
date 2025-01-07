import os
from PIL import Image, ImageOps
import math

def mirror_image(dir_path):
    for i in os.walk(dir_path):
        if len(i[2]) != 0:
    #        print(i)
            basename: str = os.path.basename(i[0])
            os.makedirs("mirrorized_images/" + basename, exist_ok=True)
            for j in range(len(i[2])):
                name_ext_pair = os.path.splitext(i[2][j])
    #            print(name_ext_pair)
                if name_ext_pair[1] == ".jpg" or name_ext_pair[1] == ".png" or name_ext_pair[1] == ".PNG"or name_ext_pair[1] == ".JPG":
                    directory: str = i[0] + "/" + i[2][j]
    #                print(directory)
                    im = Image.open(directory)
                    im_mirror = ImageOps.mirror(im)
                    im_mirror.save("mirrorized_images/"+ basename + "/" + name_ext_pair[0] + "_mirror" + name_ext_pair[1])
                if name_ext_pair[1] == ".txt" or name_ext_pair[1] == ".TXT": #YOLO形式のテキストの左右情報を反転させるやつ
                    directory: str = i[0] + "/" + i[2][j]
                    path_write = 'mirrorized_images/' + basename + '/' + name_ext_pair[0] + '_mirror.txt'
                    g = open(path_write, "w")
                    f = open(directory, "r")
                    for s_line in f:
                        tags = s_line.split()
                        write: str = ""
                        for k in range(len(tags)):
                            if k != 0:
                                write = write + " "
                            match k:
                                case 1:
                                    tags[1] = str(math.floor((1 - float(tags[1])) * 10000000 ) / 10000000)
                                case _:
                                    pass
                            write = write + str(tags[k])
                        g.write(write + "\n")
                    g.close()
                    f.close()

if __name__ == "__main__":
    path: str = "debit_images/"
    mirror_image(path)