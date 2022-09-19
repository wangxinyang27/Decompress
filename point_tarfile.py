import tarfile
from point_basefile import BaseF


class DECOMPRESS(BaseF):

    def Decompress(self):
        tar = tarfile.open(self.source)
        names = tar.getnames()
        for name in names:
            tar.extract(name, self.target)
