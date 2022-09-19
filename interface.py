import tkinter.messagebox
from tkinter import *
from point_basefile import SourceError, TargetError
import importlib
import datetime


class Interface(object):
    def __init__(self):
        # ----------创建界面--------------
        self.root = Tk()
        self.root.title('Decompress')
        self.root.geometry('720x480')
        self.lb = Label(self.root)
        self.lb.pack()
        self.t1 = None
        self.t2 = None
        self.mode = None
        # ----------界面设置--------------
        self.create_label()
        self.create_var()
        self.create_button()
        self.create_options()
        # ----------获取时间--------------
        style = '%Y-%m-%d %H:%M:%S'
        self.now = datetime.datetime.now().strftime(style)
        # ----------事件循环--------------
        self.root.mainloop()


    def create_label(self):
        lb1 = Label(self.root, text='The path of compressed package',
                    font=('华文新魏', 10),
                    padx=120,
                    width=20,
                    height=2,
                    relief=SUNKEN)
        lb1.place(relx=0.10, rely=0.43)

        lb2 = Label(self.root, text='The path of save directory',
                    font=('华文新魏', 10),
                    padx=120,
                    width=20,
                    height=2,
                    relief=SUNKEN)
        lb2.place(relx=0.10, rely=0.63)

    def create_options(self):
        self.t1 = Entry(self.root)
        self.t1.place(relx=0.1, rely=0.5, relwidth=0.7, relheight=0.06)

        self.t2 = Entry(self.root)
        self.t2.place(relx=0.1, rely=0.7, relwidth=0.7, relheight=0.06)

    def create_var(self):
        var = IntVar()

        rd1 = Radiobutton(self.root, text=".tar",
                          variable=var,value=0,font=('华文新魏', 12), command=self.setmode1)
        rd1.place(relx=0.1, rely=0.1)

        rd2 = Radiobutton(self.root,text=".gz",
                          variable=var,value=1,font=('华文新魏', 12), command=self.setmode2)
        rd2.place(relx=0.1, rely=0.2)

        rd3 = Radiobutton(self.root,text=".zip",
                          variable=var,value=2,font=('华文新魏', 12), command=self.setmode3)
        rd3.place(relx=0.1, rely=0.3)

    def create_button(self):
        btn = Button(self.root, text="Decompress", command=self.gone)
        btn.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

    # command带的函数不能有参数？
    def setmode1(self):
        self.mode = ".tar"

    def setmode2(self):
        self.mode = ".gz"

    def setmode3(self):
        self.mode = ".zip"

    @staticmethod
    def raiseError(m):
        tkinter.messagebox.showinfo('Error!', m)

    @staticmethod
    def success(m):
        tkinter.messagebox.showinfo('Success', m)

    def gone(self):
        opt = [self.mode, self.t1.get(), self.t2.get()]
        # print(opt)
        label = {".gz": "gzfile",
                 ".tar": "tarfile",
                 ".zip": "zipfile"}
        # 选择被解压缩文件的类型
        if self.mode is None:
            self.raiseError("请选择被解压缩文件的类型")
            return 0
        module_name = "point_" + label.get(self.mode)
        # 导入相应模块
        module = importlib.import_module(module_name)
        # 建议输入输出路径是否合法
        try:
            module.DECOMPRESS(self.t1.get(), self.t2.get(), self.mode).go()
            self.success("解压缩成功")
        except SourceError:
            self.raiseError("输入压缩包的路径无效")
            return 0
        except TargetError:
            self.raiseError("输出文件位置无效")
            return 0

    # /home/wxy/桌面/n02085936.tar
    # /home/wxy/桌面/dataset


if __name__ == '__main__':
    # 初始化一个界面
    Interface()

