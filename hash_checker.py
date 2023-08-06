import hashlib
from os.path import exists, getsize, isfile
from platform import system
from subprocess import run

history = ""


def clear_history():
    global history
    history = ""


def clear_terminal():
    os = system()
    command = "cls" if os == "Windows" else "clear"
    run(command, shell=True)


def convert_file_size(file_size: int) -> str:
    file_size /= 1024
    if file_size < 1000:
        return "{:.2f} KB".format(file_size)
    file_size /= 1024
    if file_size < 1000:
        return "{:.2f} MB".format(file_size)
    file_size /= 1024
    if file_size < 1000:
        return "{:.2f} GB".format(file_size)
    file_size /= 1024
    if file_size < 1000:
        return "{:.2f} TB".format(file_size)


def print_file_info(file_path: str) -> None:
    print("-" * 50)
    print(
        "File Name:",
        file_path.split("\\")[-1]
        if system() == "Windows"
        else file_path.split("/")[-1],
    )
    print("File Size:", convert_file_size((getsize(file_path))))
    print("File Path:", file_path)
    global history
    if history:
        print(history)
    print("-" * 50)


def hash_file(file_path, hash_algo):
    hash_object = hashlib.new(hash_algo)
    with open(file_path, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            hash_object.update(chunk)
    result = hash_object.hexdigest()
    return result


def print_string_info(input_string: str):
    print("-" * 50)
    print(f"Input String: {input_string}\nLenght: {len(input_string)}")
    global history
    if history:
        print(history)
    print("-" * 50)


def hash_string(input_string, hash_algo):
    hash_object = hashlib.new(hash_algo)
    hash_object.update(input_string.encode("utf-8"))
    result = hash_object.hexdigest()
    return result


def main():
    # get a list of availible hashing algorithms
    available_algorithms = sorted(list(hashlib.algorithms_available))
    options = "\n0. Main Menu"
    for index, algo in enumerate(available_algorithms):
        options += f"\n{index+1}. {algo}"
    try:
        clear_terminal()
        hash_algo = None
        is_file = True
        file_apth = input("Drag and drop the file: ")
        if not (exists(file_apth) and isfile(file_apth)):
            is_file = False
        while True:
            # this while loop implements the second window (file or string hash check)
            clear_terminal()
            if is_file:
                print_file_info(file_apth)
            else:
                print_string_info(file_apth)
            print(options)
            hash_option = int(input("\n> ")) - 1
            if hash_option == -1:
                clear_history()
                main()
            elif hash_option in range(len(available_algorithms)):
                hash_algo = available_algorithms[hash_option]
            else:
                continue
            try:
                if is_file:
                    result = hash_file(file_apth, hash_algo)
                else:
                    result = hash_string(file_apth, hash_algo)
                print(result)
                global history
                history += f"\n{hash_algo}: {result}"
                input("\nPress any key to continue...")
            except FileNotFoundError:
                input("\nFile was not found!\nPress any key to continue...")
                clear_history()
                break
    except KeyboardInterrupt:
        print("Exiting the program...")
        exit()


if __name__ == "__main__":
    main()
