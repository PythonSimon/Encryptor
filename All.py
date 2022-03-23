# coding=utf-8

import sys

from random import *
from wx import *

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
    "孙竞阳",
    "Fennick"
]
passwords = ["6150", "5061", "yang", "wang"]


def checkName(name):
    return name in names


def checkPassword(password):
    return password in passwords


class BaseFrame(Frame):

    def __init__(self, size, title, closingWarning="确认关闭？", kind="default", backgroundColor="GREY"):
        super(BaseFrame, self).__init__(parent=None, title=title, size=size, style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX)

        self.closingWarning = closingWarning
        self.warning = True

        if kind == "default":
            self.panel = Panel(parent=self)
        elif kind == "split-v":
            self.splitter = SplitterWindow(self, style=SP_3DSASH)
            self.leftPanel = Panel(self.splitter)
            self.rightPanel = Panel(self.splitter)
            self.splitter.SplitVertically(self.leftPanel, self.rightPanel, int(self.GetSize()[0] / 2))
            self.splitter.SetMinimumPaneSize(int(self.GetSize()[0] / 10))
        elif kind == "split-h":
            self.splitter = SplitterWindow(self, style=SP_3DSASH)
            self.topPanel = Panel(self.splitter)
            self.bottomPanel = Panel(self.splitter)
            self.splitter.SplitHorizontally(self.topPanel, self.bottomPanel, int(self.GetSize()[1] / 2))
            self.splitter.SetMinimumPaneSize(int(self.GetSize()[1] / 10))

        icon = Icon(r"Icon.png", BITMAP_TYPE_PNG)

        self.Center()
        self.SetBackgroundColour(backgroundColor)
        self.SetIcon(icon)

        self.Bind(EVT_CLOSE, self.on_close)

    def on_close(self, event):
        if self.warning:
            warnMd = MessageDialog(None, self.closingWarning, caption="提示", style=YES_NO | ICON_EXCLAMATION)

            if warnMd.ShowModal() == ID_YES:
                self.Destroy()
                sys.exit(0)
            else:
                warnMd.Destroy()
        else:
            self.Destroy()
            sys.exit(0)

    def close(self, event=None):
        self.Destroy()
        sys.exit(0)


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


CANCEL = 0
ENTER = 1


class LoginFrame(BaseFrame):

    def __init__(self):
        super(LoginFrame, self).__init__((400, 200), "身份验证", backgroundColor="AQUAMARINE")

        self.warning = False

        self.main()

    def main(self):
        global nameCtrl, passwordCtrl

        defaultFont = Font(15, SCRIPT, NORMAL, NORMAL, False)

        sizer = FlexGridSizer(3, 2, 10, 10)

        sizer.AddGrowableRow(0, 3)
        sizer.AddGrowableRow(1, 3)
        sizer.AddGrowableRow(2, 4)
        sizer.AddGrowableCol(0, 2)
        sizer.AddGrowableCol(1, 3)

        nameText = StaticText(self.panel, label="真实姓名")
        nameCtrl = TextCtrl(self.panel)
        passwordText = StaticText(self.panel, label="密码")
        passwordCtrl = TextCtrl(self.panel, style=TE_PASSWORD)

        cancel = Button(self.panel, id=CANCEL, label="取消")
        enter = Button(self.panel, id=ENTER, label="进入")

        nameText.SetFont(defaultFont)
        nameCtrl.SetFont(defaultFont)
        passwordText.SetFont(defaultFont)
        passwordCtrl.SetFont(defaultFont)
        cancel.SetFont(defaultFont)
        enter.SetFont(defaultFont)

        sizer.Add(nameText, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(nameCtrl, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(passwordText, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(passwordCtrl, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(cancel, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(enter, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)

        self.panel.SetSizer(sizer)

        self.Bind(EVT_BUTTON, handler=self.close, id=CANCEL)
        self.Bind(EVT_BUTTON, handler=self.enter, id=ENTER)

        self.panel.Layout()

    def enter(self, event):
        name = nameCtrl.GetValue()
        password = passwordCtrl.GetValue()

        if checkName(name) and checkPassword(password):
            self.Hide()
            CryptorFrame().Show()
        else:
            if name == "杨蕴巧":
                error = MessageDialog(parent=None, message="程序出错，请将下列字串反馈至<8178778@qq.com>:\n"
                                                           "    SyntaxError: ';' missed")
                error.ShowModal()
                print("""TraceBack:
    <line 69>, in <Main.py>
    def function(**args, );
SyntaxError with Due to like ':;'""")
                self.Close()
            else:
                error = MessageDialog(parent=None, message="密码或用户名错误！", caption="错误", style=OK | ICON_ERROR)
                error.ShowModal()


class MyApp(App):

    def OnInit(self):
        frame = LoginFrame()
        frame.Show()

        return True

    def OnExit(self):
        return 0


if __name__ == "__main__":
    app = MyApp()

    app.MainLoop()
