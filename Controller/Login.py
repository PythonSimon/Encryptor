# coding=utf-8

from wx import *

from Base import BaseFrame


class LoginFrame(BaseFrame):

    def __init__(self):
        super(LoginFrame, self).__init__((400, 200), "身份验证", backgroundColor="AQUAMARINE")

        self.warning = False

        self.main()

    def main(self):
        defaultFont = Font(15, SCRIPT, NORMAL, NORMAL, False)

        sizer = FlexGridSizer(3, 2, 10, 10)

        nameText = StaticText(self.panel, label="真实姓名")
        nameCtrl = TextCtrl(self.panel)
        passwordText = StaticText(self.panel, label="密码")
        passwordCtrl = TextCtrl(self.panel)

        cancel = Button(self.panel, label="取消")
        enter = Button(self.panel, label="进入")

        nameText.SetFont(defaultFont)
        nameCtrl.SetFont(defaultFont)
        passwordText.SetFont(defaultFont)
        passwordCtrl.SetFont(defaultFont)
        cancel.SetFont(defaultFont)
        enter.SetFont(defaultFont)

        sizer.AddGrowableRow(0, 3)
        sizer.AddGrowableRow(1, 3)
        sizer.AddGrowableRow(2, 4)
        sizer.AddGrowableCol(0, 2)
        sizer.AddGrowableCol(1, 3)

        sizer.Add(nameText, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(nameCtrl, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(passwordText, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(passwordCtrl, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(cancel, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)
        sizer.Add(enter, 0, flag=FIXED_MINSIZE | ALIGN_CENTER, border=10)

        self.panel.SetSizer(sizer)
        self.panel.Layout()
