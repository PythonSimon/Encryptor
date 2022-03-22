# coding=utf-8
import wx


class TeacherPage(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='欢迎使用智教机构系统！',
            size=(400, 400))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(parent=self)
        # 添加垂直方向的Box布局管理器对象
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel, label='成员登录')
        self.statictext.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.LIGHT))
        # 添加静态文本到垂直Box布局管理器
        vbox.Add(self.statictext, proportion=1, flag=wx.FIXED_MINSIZE |
                                                     wx.TOP | wx.CENTER, border=70)
        fgs = wx.FlexGridSizer(2, 2, 10, 10)
        b1 = wx.StaticText(panel, label='账号:')
        b2 = wx.StaticText(panel, label='密码:')
        global t1
        t1 = wx.TextCtrl(panel)
        global t2
        t2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        fgs.AddMany([b1, (t1, 1, wx.EXPAND),
                     b2, (t2, 1, wx.EXPAND)])
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(fgs, proportion=0, flag=wx.ALL | wx.FIXED_MINSIZE, border=10)
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)
        jbox = wx.BoxSizer(wx.HORIZONTAL)
        j1 = wx.Button(parent=panel, id=1, label='返回')
        j2 = wx.Button(parent=panel, id=2, label='登录')
        jbox.Add(j1, proportion=0, flag=wx.ALL |
                                        wx.BOTTOM, border=4)
        jbox.Add(j2, proportion=0, flag=wx.ALL |
                                        wx.BOTTOM, border=4)
        j1.SetBackgroundColour('white')
        j1.SetForegroundColour('black')
        j2.SetBackgroundColour('white')
        j2.SetForegroundColour('black')
        self.Bind(wx.EVT_BUTTON, self.click_one, j1)
        self.Bind(wx.EVT_BUTTON, self.click_one, j2)
        vbox.Add(jbox, proportion=1, flag=wx.CENTER)
        kbox = wx.BoxSizer(wx.HORIZONTAL)
        k1 = wx.Button(parent=panel, pos=(267, 164), id=3, label='找回')
        k1.SetBackgroundColour('white')
        k1.SetForegroundColour('black')
        kbox.Add(k1, proportion=0, flag=wx.FIXED_MINSIZE |
                                        wx.BOTTOM, border=0)
        self.Bind(wx.EVT_BUTTON, self.click_one_two, k1)
        panel.SetSizer(vbox)
        self.Show()

        panel.Layout()

    def click_one_two(self, event):
        event_id = event.GetId()
        if event_id == 3:
            v1 = t1.GetValue()
            dlg = wx.MessageDialog(None, "密码将发送至你的邮箱!", "提示", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                # db = pymysql.connect(host="localhost", user="root", password="123456", database="myku01")
                db = DB()
                # 使用cursor()方法获取操作游标
                try:
                    with db.cursor() as cursor:
                        sql = 'select * from teacher_login_k where teacher_id = %(i)s'
                        cursor.execute(sql, {'i': v1})
                        result_set = cursor.fetchall()
                        for row in result_set:
                            teacher_pass = row[1]
                            teacher_name = row[2]
                            teacher_mail = row[3]
                        if teacher_name == '':
                            ts1 = wx.MessageDialog(None, "姓名未被录入，请联系前台!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                            if ts1.ShowModal() == wx.ID_YES:
                                ts1.Destroy()
                        else:
                            # 配置邮箱信息
                            sender = 'myxt2022@126.com'  # 发件人的地址
                            password = 'UHYSXRUVSVJDOEEP'
                            receivers = [teacher_mail]  # 收件人地址
                            # 邮件内容设置
                            rndtxt_two = '密码 ' + teacher_pass
                            message = MIMEText(rndtxt_two, 'plain', 'utf-8')
                            # 邮件标题设置
                            message['Subject'] = 'Uu优系统'
                            # 发件人信息
                            message['From'] = sender
                            # 收件人信息
                            message['To'] = receivers[0]
                            # 通过授权码,登录邮箱,并发送邮件
                            try:
                                server = smtplib.SMTP('smtp.126.com')
                                server.login(sender, password)
                                server.sendmail(sender, receivers, message.as_string())
                                server.quit()
                            except:
                                ts2 = wx.MessageDialog(None, "邮箱有误!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                                    ts2.Destroy()  # 则关闭提示框
                            else:
                                ts2 = wx.MessageDialog(None, "已发送!", "提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                                    ts2.Destroy()  # 则关闭提示框
                except:
                    ts2 = wx.MessageDialog(None, "账号不存在!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                    if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                        ts2.Destroy()  # 则关闭提示框
                finally:
                    db.close()

            else:
                dlg.Destroy()

    def click_one(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.Destroy()
            StartPage()
        else:
            v1 = t1.GetValue()
            v2 = t2.GetValue()
            # db = pymysql.connect(host="localhost", user="root", password="123456", database="myku01")
            db = DB()
            try:
                with db.cursor() as cursor:
                    sql = 'select * from teacher_login_k where teacher_id = %(i)s'
                    cursor.execute(sql, {'i': v1})
                    result_set = cursor.fetchall()
                    for row in result_set:
                        teacher_pass = row[1]
                        global teacher_name
                        teacher_name = row[2]
                        global teacher_mail
                        teacher_mail = row[3]
                if v2 == teacher_pass:
                    global teacher_v1
                    global teacher_v2
                    global teacher_v3
                    global teacher_v4
                    teacher_v1 = v1
                    teacher_v2 = v2
                    teacher_v3 = teacher_name
                    teacher_v4 = teacher_mail
                    if teacher_v3 != '':
                        self.Destroy()
                        TeacherOper()
                    else:
                        ts1 = wx.MessageDialog(None, "姓名未被录入，请联系前台!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                        if ts1.ShowModal() == wx.ID_YES:
                            ts1.Destroy()
                else:
                    ts1 = wx.MessageDialog(None, "密码输入错误!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                    if ts1.ShowModal() == wx.ID_YES:
                        ts1.Destroy()
            except:
                ts2 = wx.MessageDialog(None, "账号不存在!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                    ts2.Destroy()  # 则关闭提示框
            finally:
                db.close()
