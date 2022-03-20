# coding=utf-8

import sys

from wx import *


class BaseFrame(Frame):

    def __init__(self, size, title, closingWarning="确认关闭？", kind="default", panels=None, background_color="GREY"):
        super(BaseFrame, self).__init__(parent=None, title=title, size=size, style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX)

        self.closingWarning = closingWarning
        self.warning = True

        if kind == "default":
            self.panel = Panel(parent=self)
        elif kind == "split-v":
            self.splitter = SplitterWindow(self, style=SP_3DSASH)
            self.left_panel = panels[0]
            self.right_panel = panels[1]
            self.splitter.SplitVertically(self.left_panel, self.right_panel, self.GetSize()[0] / 5 * 3)
            self.splitter.SetMinimumPaneSize(self.GetSize()[0] / 10)
        elif kind == "split-h":
            self.splitter = SplitterWindow(self, style=SP_3DSASH)
            self.top_panel = panels[0]
            self.bottom_panel = panels[1]
            self.splitter.SplitHorizontally(self.top_panel, self.bottom_panel, self.GetSize()[1] / 5 * 3)
            self.splitter.SetMinimumPaneSize(self.GetSize()[1] / 10)

        icon = Icon(r"Resource\Icon.jpg", BITMAP_TYPE_JPEG)

        self.Center()
        self.SetBackgroundColour(background_color)
        self.SetIcon(icon)

        self.Bind(EVT_CLOSE, self.on_close)

    def on_close(self, event):
        if self.warning:
            warn_md = MessageDialog(None, self.closingWarning, caption="提示", style=YES_NO | ICON_EXCLAMATION)

            if warn_md.ShowModal() == ID_YES:
                self.Destroy()
                sys.exit(0)
            else:
                warn_md.Destroy()

    def close(self, event=None):
        self.Destroy()
        sys.exit(0)
