import zipfile
from point_basefile import BaseF


class DECOMPRESS(BaseF):

    def Decompress(self):
        zip_file = zipfile.ZipFile(self.source)
        print("999")
        for names in zip_file.namelist():
            zip_file.extract(names, self.target)
        zip_file.close()