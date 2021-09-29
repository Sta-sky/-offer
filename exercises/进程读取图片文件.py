"""
多进程读取图片文件

"""

from multiprocessing import Process
import os,time

filename = 'D:\\desktop_background\\desktop_c\\li.jpg'
filenames = '.\\dali_top.jpg'
filenamess = '.\\dali_but.jpg'
img_size = os.path.getsize(filename)
print(os.path.getsize(filenamess))

def read_img():
    fw = open(filename,'rb')
    top_size = img_size // 2
    print(top_size)
    print(img_size)

    with open(filenames,'wb') as f:
        f.write(fw.read(top_size))
    fw.close()

def reads_img():
    fw = open(filename,'rb')
    #移动 文件偏移量  到中间位置  从头0开始 i、移动到2/1处
    fw.seek(img_size//2,0)
    # print(os.path.getsize('.\\dali_but.jpg'))
    with open(filenamess,'wb') as f:
        f.write(fw.read())


    f.close()
    fw.close()



if __name__ == '__main__':
    pro = [read_img,reads_img]

    join_ = []
    for i in pro:
        p = Process(target=i)
        join_.append(p)
        p.start()

    for i in join_:
        i.join()

