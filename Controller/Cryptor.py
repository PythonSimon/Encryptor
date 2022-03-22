# coding=utf-8

from wx import *

from Base import BaseFrame
from Service.Decryptor import decrypt
from Service.Encryptor import encrypt

ENCRYPT = 1


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
        self.left()
        self.right()

    def left(self):
        fontStyle = lambda size: Font(size, SCRIPT, NORMAL, NORMAL, False)

        sizer = BoxSizer(HORIZONTAL)

        encryptButton = StaticText(self.leftPanel, id=ENCRYPT, label="加密")
        inputText = StaticText(self.leftPanel, label="明文")
        inputCtrl = TextCtrl(self.leftPanel, style=TE_MULTILINE)
        outputText = StaticText(self.leftPanel, label="密文")
        outputCtrl = TextCtrl(self.leftPanel, style=TE_MULTILINE | TE_READONLY)

        encryptButton.SetFont(fontStyle(20))
        inputText.SetFont(fontStyle(15))
        inputCtrl.SetFont(fontStyle(13))
        outputText.SetFont(fontStyle(15))
        outputCtrl.SetFont(fontStyle(13))

        sizer.Add(encryptButton)

    def right(self):
        pass

    def encrypt(self, event):
        pass

    def decrypt(self, event):
        pass
