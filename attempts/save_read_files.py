import os
import shutil
from constants import INPUT_PATH, OUTPUT_PATH

def read_md_files():
    if not os.path.exists(INPUT_PATH):
        raise Exception(f"The input path '{INPUT_PATH}' does not exist.")

    md_files = []
    for file in os.listdir(INPUT_PATH):
        if file.endswith(".md"):
            md_files.append(file)

    return md_files


def save_md_files(md_files):
    if not os.path.exists(OUTPUT_PATH):
        raise Exception(f"The output path '{OUTPUT_PATH}' does not exist.")

    for file in md_files:
        input_path = os.path.join(INPUT_PATH, file)
        output_filename = file[:-3] + "_en.md"
        output_path = os.path.join(OUTPUT_PATH, output_filename)

        if os.path.exists(output_path):
            os.remove(output_path)

        shutil.copy(input_path, output_path)
        print(f"Transled '{file}' to '{output_filename}' in '{OUTPUT_PATH}'")

if __name__ == "__main__":
    md_files = read_md_files()
    save_md_files(md_files)