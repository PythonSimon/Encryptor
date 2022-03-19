# coding=utf-8

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


def decrypt(ciphertext):

    # 获取 Unicode 列表
    cipherUnicode = [ord(character) for character in ciphertext[2:]]

    # 获取密码本、密钥
    codebookKey = ciphertext[1]
    digitKey = ciphertext[0]
    secretKey = codebooks[codebookKey][digits[digitKey]]

    # 解密
    plainList = [chr(unicode - int(secretKey)) for unicode in cipherUnicode]
    plaintext = "".join(plainList)

    return plaintext
