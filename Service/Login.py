# coding=utf-8

names = [
    "胡梓萌",
    "石尚雨霏",
    "张子彤",
    "刘栌瑶",
    "王一冰",
    "宋宪一",
    "高萧涵",
    "史乙茜",
    "孙嘉霖",
    "刘宇洋",
    "王怡然",
    "耿仁东",
    "刘思为",
    "崔栢鸣",
    "桂乃真",
    "于枫怡",
    "矫卉轩", 
    "贺琳涵",
    "贺琳淇",
    "刘晨熙",
    "王浩博",
    "苏嘉欣",
    "金屹",
    "孙奕赫",
    "董延诚",
    "吕俊呈",
    "孙竞阳"
]
passwords = [6150, 5061, "yang", "wang"]


def checkName(name):
    return name in names


def checkPassword(password):
    return password in passwords
