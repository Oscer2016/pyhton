#Ques9_1.py
#coding=GBK
import wx       #����wxpython��
class Frame0(wx.Frame):
    def _init_(self,superior):
        #����frame����
        wx.Frame._init_(self,parent=superior,title=u'��һ������',size=(300,300))
        #����һ��wx.Panel����壩ʵ�������ɿ���ϵ���������
        panel=wx.Panel(self)
        #����Ӧ����ƶ��¼�wx.EVT_MOTION�󶨵�����OnMove
        panel.Bind(wx.EVY_MOTION,self.OnMove)
        #��panel�Ϸ��þ�̬�ı�������ʾ��Pos����ʾ��Ϣ
        wx.StaticText(parent=panel,label="Pos:",pos=(10,20))
        #��panel�Ϸ����ı������������Ϣ
        self.posCtrl = wx.TextCtrl(parent=panel,pos=(40,20))


    def OnMove(self,event):
        #��ȡ����λ��
        pos = event.GetPosition()
        #�����λ�����ı�������ʾ����
        self.posCtrl.SetValue("%s, %s"%(pos.x,pos.y))



#������
if _name_ == '_main_':
    app = wx.App()
    frame = Frame0(None)
    frame.show(True)
    app.MainLoop()
