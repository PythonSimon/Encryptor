# coding=utf-8

from wx import *

from Base import BaseFrame
from Service.Decryptor import decrypt
from Service.Encryptor import encrypt

ENCRYPT = 1
DECRYPT = 2


class CryptorFrame(BaseFrame):
    
    def __init__(self):
        super(CryptorFrame, self).__init__(
            (500, 355),
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
        global inputCtrlL, outputCtrlL

        fontStyle = lambda size: Font(size, SCRIPT, NORMAL, NORMAL, False)

        sizer = FlexGridSizer(6, 1, 0, 0)

        sizer.AddGrowableCol(0, 0)
        sizer.AddGrowableRow(0, 4)
        sizer.AddGrowableRow(1, 2)
        sizer.AddGrowableRow(2, 6)
        sizer.AddGrowableRow(3, 2)
        sizer.AddGrowableRow(4, 6)
        sizer.AddGrowableRow(5, 3)

        title = StaticText(self.leftPanel, label="加密器")
        inputText = StaticText(self.leftPanel, label="明文")
        inputCtrlL = TextCtrl(self.leftPanel, style=TE_MULTILINE)
        outputText = StaticText(self.leftPanel, label="密文")
        outputCtrlL = TextCtrl(self.leftPanel, style=TE_MULTILINE | TE_READONLY)
        encryptButton = Button(self.leftPanel, id=ENCRYPT, label="加密")

        title.SetFont(fontStyle(25))
        inputText.SetFont(fontStyle(15))
        inputCtrlL.SetFont(fontStyle(12))
        outputText.SetFont(fontStyle(15))
        outputCtrlL.SetFont(fontStyle(12))
        encryptButton.SetFont(fontStyle(19))

        sizer.Add(title, 0, flag=ALIGN_CENTER, border=10)
        sizer.Add(inputText, 0, flag=ALIGN_CENTER)
        sizer.Add(inputCtrlL, 0, flag=ALIGN_CENTER_HORIZONTAL)
        sizer.Add(outputText, 0, flag=ALIGN_CENTER)
        sizer.Add(outputCtrlL, 0, flag=ALIGN_CENTER_HORIZONTAL)
        sizer.Add(encryptButton, 0, flag=ALIGN_CENTER_HORIZONTAL)

        self.leftPanel.SetSizer(sizer)

        self.Bind(EVT_BUTTON, handler=self.encrypt, id=ENCRYPT)

        self.leftPanel.Layout()

    def right(self):
        global inputCtrlR, outputCtrlR

        fontStyle = lambda size: Font(size, SCRIPT, NORMAL, NORMAL, False)

        sizer = FlexGridSizer(6, 1, 0, 0)

        sizer.AddGrowableCol(0, 0)
        sizer.AddGrowableRow(0, 4)
        sizer.AddGrowableRow(1, 2)
        sizer.AddGrowableRow(2, 6)
        sizer.AddGrowableRow(3, 2)
        sizer.AddGrowableRow(4, 6)
        sizer.AddGrowableRow(5, 3)

        title = StaticText(self.rightPanel, label="解密器")
        inputText = StaticText(self.rightPanel, label="密文")
        inputCtrlR = TextCtrl(self.rightPanel, style=TE_MULTILINE)
        outputText = StaticText(self.rightPanel, label="明文")
        outputCtrlR = TextCtrl(self.rightPanel, style=TE_MULTILINE | TE_READONLY)
        encryptButton = Button(self.rightPanel, id=DECRYPT, label="解密")

        title.SetFont(fontStyle(25))
        inputText.SetFont(fontStyle(15))
        inputCtrlR.SetFont(fontStyle(12))
        outputText.SetFont(fontStyle(15))
        outputCtrlR.SetFont(fontStyle(12))
        encryptButton.SetFont(fontStyle(19))

        sizer.Add(title, 0, flag=ALIGN_CENTER, border=10)
        sizer.Add(inputText, 0, flag=ALIGN_CENTER)
        sizer.Add(inputCtrlR, 0, flag=ALIGN_CENTER_HORIZONTAL)
        sizer.Add(outputText, 0, flag=ALIGN_CENTER)
        sizer.Add(outputCtrlR, 0, flag=ALIGN_CENTER_HORIZONTAL)
        sizer.Add(encryptButton, 0, flag=ALIGN_CENTER_HORIZONTAL)

        self.rightPanel.SetSizer(sizer)

        self.Bind(EVT_BUTTON, handler=self.decrypt, id=DECRYPT)

        self.rightPanel.Layout()

    def encrypt(self, event):
        plaintext = inputCtrlL.GetValue()
        ciphertext = encrypt(plaintext)
        outputCtrlL.SetValue(ciphertext)

    def decrypt(self, event):
        ciphertext = inputCtrlR.GetValue()
        plaintext = decrypt(ciphertext)
        outputCtrlR.SetValue(plaintext)
