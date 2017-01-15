#Exp9_1.py
#coding=utf-8
#步骤1：
import wx           #导入wx模块

#步骤2：
class Framel(wx.Frame):     #程序的框架类继承于wx.Frame类
    def _init_(self,superior):
        wx.Frame._init_(self,parent=surperior,title="My Window" ,pos=(100,200),size=(400,200))

#步骤3：
#主程序
if _name_ == '_main_':
    app = wx.App()          #建立应用程序对象
    frame=Framel(None)      #建立框架类对象
    frame.Show(True)        #显示框架
app.MainLoop()              #建立事件循环
