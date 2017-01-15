#Ques9_1.py
#coding=GBK
import wx       #导入wxpython包
class Frame0(wx.Frame):
    def _init_(self,superior):
        #创建frame对象
        wx.Frame._init_(self,parent=superior,title=u'第一个窗体',size=(300,300))
        #创建一个wx.Panel（面板）实例以容纳框架上的所有内容
        panel=wx.Panel(self)
        #把响应鼠标移动事件wx.EVT_MOTION绑定到函数OnMove
        panel.Bind(wx.EVY_MOTION,self.OnMove)
        #在panel上放置静态文本框，以显示“Pos”提示信息
        wx.StaticText(parent=panel,label="Pos:",pos=(10,20))
        #在panel上放置文本框，用来输出信息
        self.posCtrl = wx.TextCtrl(parent=panel,pos=(40,20))


    def OnMove(self,event):
        #获取鼠标的位置
        pos = event.GetPosition()
        #将鼠标位置在文本框中显示出来
        self.posCtrl.SetValue("%s, %s"%(pos.x,pos.y))



#主程序
if _name_ == '_main_':
    app = wx.App()
    frame = Frame0(None)
    frame.show(True)
    app.MainLoop()
