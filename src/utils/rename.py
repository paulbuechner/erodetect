import os
import argparse


if __name__ == "__main__":
    cwd = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=str,
        default=cwd,
        help="dir path in which files should be renamed",
    )
    parser.add_argument(
        "--filetype", type=str, default="jpg", help="set file ending (default: .jpg)"
    )

    args = parser.parse_args()

    path = args.path
    files = os.listdir(path)

    # rename files
    for index, file in enumerate(files):
        os.rename(
            os.path.join(path, file),
            os.path.join(path, "".join([str(index), args.filetype])),
        )
