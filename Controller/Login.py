# coding=utf-8

from wx import *

from Base import BaseFrame


class LoginFrame(BaseFrame):

    def __init__(self):
        super(LoginFrame, self).__init__((200, 100), "身份验证")

        self.warning = False

        self.main()

    def main(self):
        sizer = FlexGridSizer(3, 2, 10, 10)

        nameText = StaticText(self.panel, label="真实姓名")
        nameCtrl = TextCtrl(self.panel)
        passwordText = StaticText(self.panel, labal="密码")
        passwordCtrl = TextCtrl(self.panel)

        cancel = Button(self.panel, label="取消")
        ok = Button(self.panel, label="进入工具")

        sizer.AddGrowableRow(0, 3)
        sizer.AddGrowableRow(1, 3)
        sizer.AddGrowableRow(2, 4)
        sizer.AddGrowableCol(0, 2)
        sizer.AddGrowableCol(1, 3)

        sizer.AddMany([
            nameText, (nameCtrl, 1, SHAPED),
            passwordText, (passwordCtrl, 1, SHAPED),
            (cancel, 1, SHAPED), (ok, 1, SHAPED)
        ])

        self.panel.SetSizer(sizer)
        self.panel.Layout()
