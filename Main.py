# coding=utf-8

from wx import *

from Controller.Login import LoginFrame


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
