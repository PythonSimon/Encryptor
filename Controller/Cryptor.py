# coding=utf-8

from wx import *

from Base import BaseFrame
from Service.Decryptor import decrypt
from Service.Encryptor import encrypt


class CryptorFrame(BaseFrame):
    
    def __init__(self):
        super(CryptorFrame, self).__init__((1000, 710), "身份验证", backgroundColor="AQUAMARINE")
