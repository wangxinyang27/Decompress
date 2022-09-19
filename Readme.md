# Decompress


English Version

### Function:
Unzip the files in the compressed package to the specified folder. Generally, direct unzipping will generate a folder with the same name, and then the files you want are stored in this folder, but sometimes this is not what we want. For example, a dataset needs 10,000 images, and you download 100 compressed packages, each with 100 images. If you extract these 100 compressed packages to the directory where the dataset is located, the dataset directory should be 100 directories instead of 10,000 images (maybe it really works, but I didn't know that at the time....)

We provide three ways to decompress the compressed package: .tar, .gz, .zip

Only three parameters are required: the compression method, the absolute path of the compressed package, and the destination folder

If the file names in the compressed package appear the same and are decompressed to the same directory, overwriting may occur

### Execute our code:
#### .zip
```bash
python main.py --mode zipfile --source_path ".zip" --target_path "directory"
```
Replace ".zip" with the path to the compressed package and "directory" with the destination path

#### .gz
```bash
python main.py --mode gzfile --source_path ".gz" --target_path "directory"
```
".gz" is replaced with the path of the compressed package, "directory" is replaced with the target path

(Actually this has not been verified, because there is no ready-made .gz compressed package...)

#### .tar
```bash
python main.py --mode tarfile --source_path ".tar" --target_path "directory"
```
Replace ".tar" with the path to the tarball and "directory" with the target path

.

.

.

.

Update by chance

Refer to the article [python 解压的几种方法](https://blog.csdn.net/sinat_38682860/article/details/107861367?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166356981316782390532279%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166356981316782390532279&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-107861367-null-null.142^v47^pc_rank_34_2,201^v3^control&utm_term=python%20%E8%A7%A3%E5%8E%8B&spm=1018.2226.3001.4187)

.

.

.

.

.


中文版

### 功能：
把压缩包里面的文件解压到指定的文件夹，一般直接解压会生成一个同名
文件夹，然后你想要的文件存放在这个文件夹中，但有时候这种情况并不是我们想要的
。比如一个数据集需要10000张图，你下载来的压缩包有100个，每个压缩包有100张图片，
如果你把这100个压缩包提取到数据集所在目录，那么数据集目录中应该是100个目录，而不是
10000张图片(可能真能实现，但我当时不知道....)

我们提供了三种压缩包的解压方式：.tar, .gz, .zip

只需要三个参数：压缩的方式，压缩包的绝对路径，目标文件夹

如果压缩包里面的文件名出现一致，并解压到同一个目录下，可能会出现覆盖

### 执行我们的代码：

#### .zip 
```bash
python main.py --mode zipfile  --source_path ".zip"  --target_path "directory"
```
".zip" 替换为压缩包的路径，"directory" 替换为目标路径


#### .gz
```bash
python main.py --mode gzfile  --source_path ".gz"  --target_path "directory"
```
".gz" 替换为压缩包的路径，"directory" 替换为目标路径

(实际上这个还没验证过，因为没有找到现成的.gz的压缩包......)


#### .tar
```bash
python main.py --mode tarfile  --source_path ".tar"  --target_path "directory"
```
".tar" 替换为压缩包的路径，"directory" 替换为目标路径

.

.

.

.



随缘更新

参考文章[python 解压的几种方法](https://blog.csdn.net/sinat_38682860/article/details/107861367?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166356981316782390532279%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166356981316782390532279&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-107861367-null-null.142^v47^pc_rank_34_2,201^v3^control&utm_term=python%20%E8%A7%A3%E5%8E%8B&spm=1018.2226.3001.4187)
