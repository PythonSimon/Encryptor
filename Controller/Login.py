# coding=utf-8

from wx import *

from Base import BaseFrame
from Cryptor import CryptorFrame
from Service.Login import checkName, checkPassword

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
