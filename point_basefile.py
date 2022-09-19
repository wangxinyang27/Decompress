import os


class BaseF(object):
    def __init__(self, source, target, suffix):
        self.source = source
        self.target = target
        self.suffix = suffix

    def Judgment(self):
        if not self.source.endswith(self.suffix):
            raise SourceError(
                "提供的源路径并不是指定格式的压缩包({}): {}".format(self.suffix,self.source)
            )

        # if not os.path.exists(self.target):
        #     # input("提供的目标文件不存在，是否按此路径创建目录(键入Enter)")
        #     os.mkdir(self.target)

        if not os.path.isdir(self.target):
            raise TargetError(
                "提供的目标路径并不是一个文件夹: {}".format(self.target)
            )
        # 文件夹路径是不是以"/"结尾，isdir()都会输出True
        if not self.target.endswith("/"):
            self.target += "/"
        else:
            pass

    def Decompress(self):
        pass

    def go(self):
        self.Judgment()
        self.Decompress()


# 定义几个异常
class SourceError(Exception):
    "输入压缩包路径出现异常"
    pass


class TargetError(Exception):
    "输出文件位置出现异常"
    pass
