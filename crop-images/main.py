from PIL import Image
import glob

#ファイルパス
path = './src/*.jpg'

file_list = glob.glob(path)

#初期化
i = 1

for file in file_list:
    img = Image.open('./src/test_' + str(i) + '.jpg')

    #左端のx座標, 上端のy座標, 右端のx座標, 下端のy座標
    box = (0, 0, 128, 128)

    im_crop = img.crop(box)
    im_crop.save('./src/test_fix' + str(i) + '.jpg' , quality=95)

    i += 1
