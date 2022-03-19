# coding=utf-8

from random import *

codebooks = {
    "p": "3141592653",
    "e": "2718281828",
    "s": "1414213562",
    "r": "5467558585",
    "t": "8345829387"
}

digits = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
}


def encrypt(plaintext: str):

    # 获取 Unicode 列表
    plainUnicode = [ord(character) for character in plaintext]

    # 选取密码本、密钥
    codebookKey = choice(list(codebooks.keys()))
    digitKey = choice(list(digits.keys()))
    secretKey = codebooks[codebookKey][digits[digitKey]]

    # 加密
    cipherList = [chr(unicode + int(secretKey)) for unicode in plainUnicode]
    ciphertext = digitKey + codebookKey + "".join(cipherList)

    return ciphertext
