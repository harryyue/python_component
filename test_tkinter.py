# coding:utf-8

from tkinter import *
from tkinter import ttk  
import pywifi
from pywifi import const
import time
import tkinter.filedialog
import tkinter.messagebox

class MY_GUI():
  def __init__(self,init_window_name):
    self.init_window_name = init_window_name

    #密码文件路径
    self.get_value = StringVar()

    #获取破解wifi账号
    self.get_wifi_value = StringVar()

    #获取wifi密码
    self.get_wifimm_value = StringVar()
    
    self.filename = StringVar()

    

  #设置窗口
  def set_init_window(self):
    self.init_window_name.title("WIFI破解工具")
    self.init_window_name.geometry('+500+200')

    labelframe = LabelFrame(width=400, height=200,text="配置")
    labelframe.grid(column=0, row=0, padx=10, pady=10)

    self.search = Button(labelframe,text="搜索附近WiFi").grid(column=0,row=0)

    self.pojie = Button(labelframe,text="开始破解").grid(column=1,row=0)

    self.label = Label(labelframe,text="目录路径：").grid(column=0,row=1)

    self.path = Entry(labelframe,width=12,textvariable = self.get_value).grid(column=1,row=1)

    self.file = Button(labelframe,text="添加密码文件目录").grid(column=2,row=1)

    self.wifi_text = Label(labelframe,text="WiFi账号：").grid(column=0,row=2)

    self.wifi_input = Entry(labelframe,width=12,textvariable = self.get_wifi_value).grid(column=1,row=2)

    self.wifi_mm_text = Label(labelframe,text="WiFi密码：").grid(column=2,row=2)

    self.wifi_mm_input = Entry(labelframe,width=10,textvariable = self.get_wifimm_value).grid(column=3,row=2,sticky=W)

    self.wifi_labelframe = LabelFrame(text="wifi列表")
    self.wifi_labelframe.grid(column=0, row=3,columnspan=4,sticky=NSEW)


    # 定义树形结构与滚动条
    self.wifi_tree = ttk.Treeview(self.wifi_labelframe,show="headings",columns=("a", "b", "c", "d"))    
    self.vbar = ttk.Scrollbar(self.wifi_labelframe, orient=VERTICAL, command=self.wifi_tree.yview)       
    self.wifi_tree.configure(yscrollcommand=self.vbar.set)

    # 表格的标题
    self.wifi_tree.column("a", width=50, anchor="center")
    self.wifi_tree.column("b", width=100, anchor="center")
    self.wifi_tree.column("c", width=100, anchor="center")
    self.wifi_tree.column("d", width=100, anchor="center")

    self.wifi_tree.heading("a", text="WiFiID")
    self.wifi_tree.heading("b", text="SSID")
    self.wifi_tree.heading("c", text="BSSID")
    self.wifi_tree.heading("d", text="signal")

    self.wifi_tree.grid(row=4,column=0,sticky=NSEW)
    self.wifi_tree.bind("<Double-1>",self.onDBClick)
    self.vbar.grid(row=4,column=1,sticky=NS)

    self.get_value.set(self.filename)

  #Treeview绑定事件
  def onDBClick(self,event):
    self.sels= event.widget.selection()
    self.get_wifi_value.set(self.wifi_tree.item(self.sels,"values")[1])
    #print("you clicked on",self.wifi_tree.item(self.sels,"values")[1])


def gui_start():
  init_window = Tk()
  ui = MY_GUI(init_window)
  print(ui)
  ui.set_init_window()
  #ui.scans_wifi_list()

  init_window.mainloop()

gui_start()
