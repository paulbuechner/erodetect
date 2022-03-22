import yaml
import ast
import os
import argparse

# python ./utils/create_names_file.py --path ./data/erodetect

if __name__ == "__main__":
    cwd = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", type=str, default=cwd, help="dir path containing names data"
    )
    parser.add_argument(
        "--filename",
        type=str,
        default="data.yaml",
        help="file containing the names data. default: (data.yaml)",
    )

    args = parser.parse_args()

    path: str = args.path
    file: str = args.filename

    # create names file for model
    with open(os.path.join(path, file), "r") as stream:
        names = str(yaml.safe_load(stream)["names"])

    namesFile = open(os.path.join(path, file.replace(".yaml", ".names")), "w+")
    names = ast.literal_eval(names)
    for name in names:
        namesFile.write(name + "\n")
    namesFile.close()
