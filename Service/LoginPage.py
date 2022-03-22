# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:44:17 2022

@author: Fennick
"""

import wx
import pymysql
import smtplib
from email.mime.text import MIMEText
import random

class LoginPage(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title='欢迎使用Uu优系统！',
                         size=(400,400))
        self.Centre()   #设置窗口居中
        panel = wx.Panel(parent=self)
        #添加垂直方向的Box布局管理器对象
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel,label='注册')
                                
        #添加静态文本到垂直Box布局管理器
        vbox.Add(self.statictext,proportion=1,flag=wx.FIXED_MINSIZE | 
                  wx.TOP | wx.CENTER,border=70)
        fgs = wx.FlexGridSizer(5,2,10,10)
        b1 = wx.StaticText(panel,label='账号:')
        b2 = wx.StaticText(panel,label='密码:')
        b3 = wx.StaticText(panel,label='密码:')
        b4 = wx.StaticText(panel,label='邮箱:')
        b5 = wx.StaticText(panel,label='验证码:')
        global t1
        global t2
        global t3
        global t4
        global t5
        t1 = wx.TextCtrl(panel)
        t2 = wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        t3 = wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        t4 = wx.TextCtrl(panel)
        t5 = wx.TextCtrl(panel)
        fgs.AddMany([b1,(t1,1,wx.EXPAND),
                     b2,(t2,1,wx.EXPAND),
                     b3,(t3,1,wx.EXPAND),
                     b4,(t4,1,wx.EXPAND),
                     b5,(t5,1,wx.EXPAND)])
        fgs.AddGrowableRow(0,1)
        fgs.AddGrowableRow(1,1)
        fgs.AddGrowableRow(2,1)
        fgs.AddGrowableRow(3,1)
        fgs.AddGrowableRow(4,1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(fgs,proportion=0,flag=wx.ALL | wx.FIXED_MINSIZE,border=10)
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        statictext = wx.StaticText(panel,label='选择：')
        radio1 = wx.RadioButton(panel,1,'前台')
        radio2 = wx.RadioButton(panel,2,'成员')
        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio1_click,id=1,id2=2)
        hbox2.Add(statictext,1,flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE,border=5)
        hbox2.Add(radio1,1,flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox2.Add(radio2,1,flag=wx.ALL | wx.FIXED_MINSIZE)
        
        vbox.Add(hbox,proportion=1,flag=wx.CENTER)
        vbox.Add(hbox2,proportion=1,flag=wx.CENTER)
        panel.SetSizer(vbox)
        jbox = wx.BoxSizer(wx.HORIZONTAL)
        j1 = wx.Button(parent=panel,id=1,label='返回')
        j2 = wx.Button(parent=panel,id=2,label='注册')
        jbox.Add(j1,proportion=0,flag=wx.FIXED_MINSIZE | 
                 wx.BOTTOM ,border=2)
        jbox.Add(j2,proportion=0,flag=wx.FIXED_MINSIZE | 
                 wx.BOTTOM ,border=2)
        
        self.Bind(wx.EVT_BUTTON,self.click_one,j1)
        self.Bind(wx.EVT_BUTTON,self.click_one,j2)
        vbox.Add(jbox,proportion=1,flag=wx.CENTER)
        kbox = wx.BoxSizer(wx.HORIZONTAL)
        k1 = wx.Button(parent=panel,pos=(275,202),id=1,label='获取')
        kbox.Add(k1,proportion=0,flag=wx.FIXED_MINSIZE | 
                 wx.BOTTOM ,border=2)
        self.Bind(wx.EVT_BUTTON,self.click_one_two,k1)
        panel.SetSizer(vbox)
        self.Show()
    def on_radio1_click(self,event):
        rb = event.GetEventObject()
        global cb
        cb = rb.GetLabel()
    def click_one_two(self,event):
        event_id = event.GetId()
        if event_id == 1:
            v4=t4.GetValue()
            txt_list = []
            global rndtxt
            global rndtxt_two
            # 数字
            txt_list.extend(chr(random.randint(48,57)))
            # 数字
            txt_list.extend(chr(random.randint(48,57)))
            # 数字
            txt_list.extend(chr(random.randint(48,57)))
            # 数字
            txt_list.extend(chr(random.randint(48,57)))
            # 数字
            txt_list.extend(chr(random.randint(48,57)))
            # 数字
            txt_list.extend(chr(random.randint(48,57)))
            rndtxt = ''.join(txt_list)
            #配置邮箱信息
            sender = 'myxt2022@126.com' #发件人的地址
            password = 'UHYSXRUVSVJDOEEP'
            receivers = [v4] #收件人地址
            #邮件内容设置
            rndtxt_two = '验证码 '+rndtxt
            message = MIMEText(rndtxt_two,'plain','utf-8')
            #邮件标题设置
            message['Subject'] = '来自Uu优系统' 
            #发件人信息
            message['From'] = sender
            #收件人信息     
            message['To'] = receivers[0]  
            #通过授权码,登录邮箱,并发送邮件
            try:
                server = smtplib.SMTP('smtp.126.com')
                server.login(sender,password)
                server.sendmail(sender, receivers, message.as_string())
                server.quit()
            except:
                ts2 = wx.MessageDialog(None, "输入邮箱有误!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                    ts2.Destroy()  # 则关闭提示框
            

    def click_one(self,event):
        event_id = event.GetId()
        if event_id == 1:
            self.Destroy()
            # StartPage()
        else:
            v1=t1.GetValue()
            v2=t2.GetValue()
            v3=t3.GetValue()
            v5=t5.GetValue()
            if v1=='boss':
                ts1 = wx.MessageDialog(None, "账号已存在!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                if ts1.ShowModal() == wx.ID_YES:
                    ts1.Destroy()
            else:
                try:
                    if cb == '前台':
                            if v5 == rndtxt:
                                if v2 == v3:
                                    global admin_id
                                    admin_id=[]
                                    dv = pymysql.connect(host="localhost", user="root", password="123456", database="myku01")
                                    # 使用cursor()方法获取操作游标
                                    try:
                                        with dv.cursor() as cursor:
                                            sql_dv ='select * from admin_login_k'
                                            cursor.execute(sql_dv)
                                            result_set = cursor.fetchall()
                                            for row in result_set:
                                                admin_id.append(row[0])
                                    except:
                                        ts1 = wx.MessageDialog(None, "服务器连接失败!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                        if ts1.ShowModal() == wx.ID_YES:
                                            ts1.Destroy()
                                    finally:
                                        dv.close()
                                
                                    if v1 in admin_id:
                                        ts1 = wx.MessageDialog(None, "账号已存在!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                        if ts1.ShowModal() == wx.ID_YES:
                                            ts1.Destroy()
                                    else:
                                        dv = pymysql.connect(host="localhost", user="root", password="123456", database="myku01")
                                        # 使用cursor()方法获取操作游标
                                        try:
                                            with dv.cursor() as cursor:
                                                sql_dv = 'insert into admin_login_k(admin_id,admin_pass) values (%s,%s)'
                                                cursor.execute(sql_dv,(v1,v2))
                                                dv.commit()
                                        except:
                                            ts1 = wx.MessageDialog(None, "注册失败!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                            if ts1.ShowModal() == wx.ID_YES:
                                                ts1.Destroy()
                                        else:
                                            ts2 = wx.MessageDialog(None, "注册成功!", "提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                            if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                                                ts2.Destroy()  # 则关闭提示框
                                            self.Destroy()
                                            # AdminPage()
                                        finally:
                                            dv.close()
                                            # self.Destroy()
                                            # AdminPage()
                                    
                                else:
                                    ts1 = wx.MessageDialog(None, "两次输入密码不同!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                    if ts1.ShowModal() == wx.ID_YES:
                                        ts1.Destroy()
                            else:
                                ts1 = wx.MessageDialog(None, "验证码错误!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                if ts1.ShowModal() == wx.ID_YES:
                                    ts1.Destroy()

                    elif cb == '成员':
                            if v5 == rndtxt:
                                if v2 == v3:
                                    global teacher_id
                                    teacher_id=[]
                                    dv = pymysql.connect(host="localhost", user="root", password="123456", database="myku01")
                                    # 使用cursor()方法获取操作游标
                                    try:
                                        with dv.cursor() as cursor:
                                            sql_dv ='select * from teacher_login_k'
                                            cursor.execute(sql_dv)
                                            result_set = cursor.fetchall()
                                            for row in result_set:
                                                teacher_id.append(row[0])
                                    except:
                                        ts1 = wx.MessageDialog(None, "服务器连接失败!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                        if ts1.ShowModal() == wx.ID_YES:
                                            ts1.Destroy()
                                    finally:
                                        dv.close()
                                
                                    if v1 in teacher_id:
                                        ts1 = wx.MessageDialog(None, "账号已存在!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                        if ts1.ShowModal() == wx.ID_YES:
                                            ts1.Destroy()
                                    else:
                                        dv = pymysql.connect(host="localhost", user="root", password="123456", database="myku01")
                                        # 使用cursor()方法获取操作游标
                                        try:
                                            with dv.cursor() as cursor:
                                                sql_dv = 'insert into teacher_login_k(teacher_id,teacher_pass) values (%s,%s)'
                                                cursor.execute(sql_dv,(v1,v2))
                                                dv.commit()
                                        except:
                                            ts1 = wx.MessageDialog(None, "注册失败!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                            if ts1.ShowModal() == wx.ID_YES:
                                                ts1.Destroy()
                                        else:
                                            ts2 = wx.MessageDialog(None, "注册成功!", "提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                            if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                                                ts2.Destroy()  # 则关闭提示框
                                            self.Destroy()
                                            # TeacherPage()
                                        finally:
                                            dv.close()
                                            # self.Destroy()
                                            # TeacherPage()
                                else:
                                    ts1 = wx.MessageDialog(None, "两次输入密码不同!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                    if ts1.ShowModal() == wx.ID_YES:
                                        ts1.Destroy()
                            else:
                                ts1 = wx.MessageDialog(None, "验证码错误!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                                if ts1.ShowModal() == wx.ID_YES:
                                    ts1.Destroy()
    
                except:
                    ts2 = wx.MessageDialog(None, "请选择注册类型!", "错误提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
                    if ts2.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                        ts2.Destroy()  # 则关闭提示框
                finally:
                    pass

class App(wx.App):
    def OnInit(self):
        #创建窗口对象
        frame = LoginPage()
        frame.Show()
        return True
    def OnExit(self):
        return False
if __name__ == '__main__':
    app = App()
    app.MainLoop()