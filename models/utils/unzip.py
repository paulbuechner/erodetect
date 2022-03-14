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
        "--path",
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

    # Unzip all files in given dir
    for file in files:
        if file.endswith(".zip"):
            filePath = f"{path}/{file}"
            zip_file = zipfile.ZipFile(filePath)

            for names in zip_file.namelist():
                zip_file.extract(names, f"{args.to}/Temp")
            zip_file.close()

            # Copy train, valid and test images to train, valid and test dir
            copy_files(f"{args.to}/Temp/train/images", f"{args.to}/train/images")
            copy_files(f"{args.to}/Temp/train/labels", f"{args.to}/train/labels")
            copy_files(f"{args.to}/Temp/test/images", f"{args.to}/test/images")
            copy_files(f"{args.to}/Temp/test/labels", f"{args.to}/test/labels")
            copy_files(f"{args.to}/Temp/valid/images", f"{args.to}/valid/images")
            copy_files(f"{args.to}/Temp/valid/labels", f"{args.to}/valid/labels")

            # Copy data.yaml
            shutil.copy(f"{args.to}/Temp/data.yaml", f"{args.to}/data.yaml")

            print(f"{file} unzipped")

