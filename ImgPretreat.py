# 将原始图片转换成需要的大小，并将其保存
# ========================================================================================
import os
from PIL import Image

# 原始图片的存储位置
orig_picture = './marvel_heroes'

# 生成图片的存储位置
gen_picture = './marvel_preprogress'

# 需要的识别类型
classes = {'BlackPanther', 'DoctorStrange','IronMan','ScarletWitch','SpiderMan', 'Thor'}


for index, name in enumerate(classes):
    class_path = orig_picture + "/" + name + "/"
    gen_pic_path=gen_picture+"/"+name+"/"
    for img_name in os.listdir(class_path):
        img_path = class_path + img_name
        img = Image.open(img_path)
        img = img.resize((64, 64))  # 设置需要转换的图片大小
        if img.mode != 'RGB':
            img = img.convert('RGB')
        if not os.path.exists(gen_pic_path):
            os.makedirs(gen_pic_path)
        img.save(gen_pic_path+"/"+img_name)
