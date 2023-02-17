import os
import csv


def main():
    folder = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(folder, 'output.txt'), 'w') as f:
        f.write(f'ROOT-FOLDER: {os.path.abspath(folder)}:\n')

        for file in os.listdir(folder):
            f.write(f'    {file}\n')

        sub_indent = '      '
        for root, dirs, files in os.walk(folder):
            current_indent = (sub_indent * (root.count(os.sep) - folder.count(os.sep) + 1))

            f.write("\n")
            f.write(
                f"{'':{len(current_indent)}}DIR-STEPS FROM ROOT: {root.count(os.sep) - folder.count(os.sep)}"
                f"\n{current_indent}CURRENT FOLDER: {root}\n")

            file_list = []
            for file in files:
                file_list.append(file)
            if not dirs:
                f.write(f"\n{current_indent}DIRECTORIES: \n")
                f.write(f"{current_indent}      --NO DIRECTORIES LOCATED--\n")
            else:
                f.write(f"\n{current_indent}DIRECTORIES: {dirs}")

            if not files:
                f.write(f"\n{current_indent}FILES: \n")
                f.write(f"{current_indent}      ------------------------------\n")
                f.write(f"{current_indent}      --NO FILES LOCATED--\n")
                f.write(f"{current_indent}      ------------------------------\n")

            else:
                f.write(f"\n{current_indent}FILES: \n")
                f.write(f"{current_indent}      ------------------------------\n")

                for file in file_list:
                    f.write(f"{current_indent}      >{file}\n")
                f.write(f"{current_indent}      ------------------------------\n")


if __name__ == '__main__':
    main()
