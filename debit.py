from PIL import Image
import os

def debit_image(dir_path, bit):
    for i in os.walk(dir_path):
        if len(i[2]) != 0:
    #        print(i)
            basename: str = os.path.basename(i[0])
            os.makedirs("debit_images/" + basename, exist_ok=True)
            for j in range(len(i[2])):
                name_ext_pair = os.path.splitext(i[2][j])
    #            print(name_ext_pair)
                if name_ext_pair[1] == ".jpg" or name_ext_pair[1] == ".png":
                    directory: str = i[0] + "/" + i[2][j]
    #                print(directory)
                    im = Image.open(directory)
                    im_debit = im.quantize(bit)
                    im_debit.save("debit_images/"+ basename + "/" + name_ext_pair[0] + "_debit" + name_ext_pair[1])

if __name__ == "__main__":
    path: str = "images/"
    a = int(input("bit深度 < 256 推奨/64 : "))
    debit_image(path, a)