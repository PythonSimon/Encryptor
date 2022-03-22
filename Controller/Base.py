# coding=utf-8

import sys

from wx import *


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
            self.splitter.SplitVertically(self.leftPanel, self.rightPanel, self.GetSize()[0] / 2)
            self.splitter.SetMinimumPaneSize(self.GetSize()[0] / 10)
        elif kind == "split-h":
            self.splitter = SplitterWindow(self, style=SP_3DSASH)
            self.topPanel = Panel(self.splitter)
            self.bottomPanel = Panel(self.splitter)
            self.splitter.SplitHorizontally(self.topPanel, self.bottomPanel, self.GetSize()[1] / 2)
            self.splitter.SetMinimumPaneSize(self.GetSize()[1] / 10)

        icon = Icon(r"Resource\Icon.png", BITMAP_TYPE_PNG)

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
