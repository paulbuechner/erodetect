import os
import argparse
import zipfile
import shutil


def copy_files(src, dest):
    src_files = os.listdir(src)

    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            if not os.path.exists(dest):
                os.makedirs(dest)

            shutil.copy(full_file_name, dest)


# Unzip all files in given dir into specifed dir and process it's content
if __name__ == "__main__":
    cwd = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src",
        type=str,
        default=cwd,
        help="dir path containing the zip files (default: current working dir)",
    )
    parser.add_argument(
        "--dest",
        type=str,
        default=cwd,
        help="dir path to unzip to (default: current working dir)",
    )
    parser.add_argument(
        "--filetype", type=str, default="zip", help="set archive type (default: zip)"
    )

    args = parser.parse_args()

    src, dest = args.src, args.dest
    files = os.listdir(src)

    # Unzip all files in given dir
    for file in files:
        if file.endswith(".zip"):
            filePath = f"{src}/{file}"
            zip_file = zipfile.ZipFile(filePath)

            for names in zip_file.namelist():
                zip_file.extract(names, f"{args.dest}/Temp")
            zip_file.close()

            # Copy train, valid and test images to train, valid and test dir
            copy_files(f"{dest}/Temp/train/images", f"{dest}/train/images")
            copy_files(f"{dest}/Temp/train/labels", f"{dest}/train/labels")
            copy_files(f"{dest}/Temp/test/images", f"{dest}/test/images")
            copy_files(f"{dest}/Temp/test/labels", f"{dest}/test/labels")
            copy_files(f"{dest}/Temp/valid/images", f"{dest}/valid/images")
            copy_files(f"{dest}/Temp/valid/labels", f"{dest}/valid/labels")

            # Copy data.yaml
            shutil.copy(f"{dest}/Temp/data.yaml", f"{dest}/data.yaml")

            print(f"{file} unzipped")
