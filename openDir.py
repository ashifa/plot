# 查找某个目录下的目标文件
import os  # 引入操作系统模块
import sys  # 用于标准输入输出
import easygui as g  # 引入图形用户界面
import all_in_one


def search(path1, name):
    Allfiles = []  # 创建队列
    Allfiles.append(path1)

    while len(Allfiles) != 0:  # 当队列中为空的时候跳出循环
        path = Allfiles.pop(0)  # 从队列中弹出首个路径
        if os.path.isdir(path):  # 判断路径是否为目录
            print(path)
            ALLFilePath = os.listdir(path)  # 若是目录，遍历将里面所有文件入队
            for line in ALLFilePath:
                newPath = path + "\\" + line  # 形成绝对路径
                Allfiles.append(newPath)
        else:  # 如果是一个文件，判断是否为目标文件
            target = os.path.basename(path)
            if target == name:
                return path
    return -1


def findexcel(path1):
    Allfiles = []  # 创建队列
    Allfiles.append(path1)
    result = []

    while len(Allfiles) != 0:  # 当队列中为空的时候跳出循环
        path = Allfiles.pop(0)  # 从队列中弹出首个路径
        if os.path.isdir(path):  # 判断路径是否为目录
            print(path)
            ALLFilePath = os.listdir(path)  # 若是目录，遍历将里面所有文件入队
            for line in ALLFilePath:
                newPath = path + "\\" + line  # 形成绝对路径
                Allfiles.append(newPath)
        else:  # 如果是一个文件，判断是否为目标文件
            target = os.path.basename(path)
            if target.endswith('xlsx'):
                result.append(path1 + "\\" + target)
    return result


path = g.diropenbox("open path", ' open path', 'C:\\Users\\user\\Desktop\\汕头整机\\汕头存档\\20181214\\')
# name = g.enterbox(msg='请输入您要查找的文件名：',default='processed_ecg.xlsx')
# answer = search(path, name)
answer = findexcel(path)
if answer == -1:
    print('no result')
else:
    for path in answer:
        all_in_one.genPdf(path)
