# coding=utf-8

from Service.Decryptor import decrypt
from Service.Encryptor import encrypt

print("\033[1;32m请输入要加密的文字：")
plaintext = input()
print(f"\033[1;32m加密成功！密文为：\033[1;36m{encrypt(plaintext)}")

print("\033[1;32m情输入要解密的文字：")
ciphertext = input()
print(f"\033[1;32m解密成功！明文为：\033[1;36m{decrypt(ciphertext)}")
