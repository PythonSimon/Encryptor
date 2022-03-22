# coding=utf-8

from wx import *

from Base import BaseFrame
from Service.Decryptor import decrypt
from Service.Encryptor import encrypt


class CryptorFrame(BaseFrame):
    
    def __init__(self):
        super(CryptorFrame, self).__init__(
            (1000, 710),
            "加密工具",
            closingWarning="确定退出聊天加密工具？",
            kind="split-v",
            backgroundColor="AQUAMARINE"
        )

        self.main()

    def main(self):
        pass
