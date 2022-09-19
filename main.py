# _*_ coding: utf-8 _*_
import argparse
import importlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--mode', type=str, required=True, default="tarfile",
                    help="gzfile, tarfile, zipfile"
    )
    parser.add_argument(
        '--source_path', type=str, required=True, help="The path to the compressed package"
    )
    parser.add_argument(
        '--target_path', type=str, required=True, help="The path to target directory"
    )
    opt, _ = parser.parse_known_args()

    label = {"gzfile": ".gz",
             "tarfile": ".tar",
             "zipfile": ".zip"}

    module_name = "point_" + opt.mode
    module = importlib.import_module(module_name)
    module.DECOMPRESS(opt.source_path, opt.target_path, label[opt.mode]).go()
