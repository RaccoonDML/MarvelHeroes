# 看看你是哪个超级英雄！
[本项目参考模型](https://github.com/waitingfordark/flower_world)
- 这是一个基于Tensorflow的CNN模型，现在可以识别六个超级英雄分别是：
- 'BlackPanther', 'DoctorStrange','IronMan','ScarletWitch','SpiderMan','Thor'
- 欢迎大家补充

## Require
1. Python3.5+
2. tensorflow
3. wxPython（不使用UI界面暂时不需要这个库）

## Quick start
- git clone这个项目
- 导入你喜欢的IDE如pycharm，或者你喜欢的编辑器如Atom。
- train.py中的训练样本读入路径和模型存储路径可以自行修改
    train_dir = './marvel_preprogress'  # 训练样本的读入路径
    logs_train_dir = './model_save'  # logs存储路径
- 运行train.py开始训练。
- 训练完成后，修改test.py中的`logs_train_dir = './model_save'`为你的目录。
- 运行test.py或者gui.py查看结果。

## Expand train data
- 在marvel_heroes文件夹对应的文件夹下保存相应的英雄图片
- 运行ImgPretreat.py将训练图片进行预处理，生成的图片位于marvel_preprogress中相应的文件夹
- 修改train.py中相关参数进行重新训练
