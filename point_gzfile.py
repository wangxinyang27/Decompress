import gzip
from point_basefile import BaseF


class DECOMPRESS(BaseF):

    def Decompress(self):
        f_name = self.source.replace(".gz", "")
        # 获取文件的名称，去掉
        g_file = gzip.GzipFile(self.source)
        # 创建gzip对象
        with open(f_name, 'w+') as f:
            f.write(g_file.read())
            g_file.close()
            # 关闭gzip对象

