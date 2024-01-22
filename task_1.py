import argparse
import os
import shutil
import sys


def print_error(message, exit=True):
    print(f"Помилка: {message}")
    if exit:
        sys.exit(1)


def empty_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir", type=str, help="Шлях до вихідної дерикторії")
    parser.add_argument(
        "dist_dir",
        type=str,
        nargs="?",
        default="dist",
        help="Шлях до дерикторії призначення (за замовчуванням: dist)",
    )
    return parser.parse_args()


def copy_files(src, dest):
    for root, dirs, files in os.walk(src):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1][1:]
            if ext == "":
                ext = "_unknown"
            if ext:
                dest_dir = os.path.join(dest, ext)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy(file_path, dest_dir)


def main():
    args = parse_args()
    src_dir = args.src_dir
    dist_dir = args.dist_dir

    if not os.path.exists(src_dir):
        print_error(f"Директорія з вихідними файлами '{src_dir}' не існує.")
        return

    if os.path.exists(dist_dir):
        empty_folder(dist_dir)

    try:
        copy_files(src_dir, dist_dir)
        print(f"Файли успішно скопійовані")
    except Exception as e:
        print("Сталася помилка при копіюванні: " + str(e))


if __name__ == "__main__":
    main()

# приклад використання: python task_1.py src