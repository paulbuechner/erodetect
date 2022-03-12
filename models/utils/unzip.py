import os
import argparse
import zipfile

# Unzip all files in given dir into specifed dir and process it's content
if __name__ == "__main__":
    cwd = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from",
        type=str,
        default=cwd,
        help="dir path containing the zip files (default: current working dir)",
    )
    parser.add_argument(
        "--to",
        type=str,
        default=cwd,
        help="dir path to unzip to (default: current working dir)",
    )
    parser.add_argument(
        "--filetype", type=str, default="zip", help="set archive type (default: zip)"
    )

    args = parser.parse_args()

    path = args.path
    files = os.listdir(path)

    for file in files:
        if file.endswith(".zip"):
            filePath = path + "/" + file
            zip_file = zipfile.ZipFile(filePath)
            for names in zip_file.namelist():
                zip_file.extract(names, path)
            zip_file.close()
