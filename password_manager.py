from cryptography.fernet import Fernet


# import json
def load_key():
    with open("key.key", "rb") as f:
        keys = f.read()
    return keys


master_pwd = input("Master password: ").strip()

key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    # manager = {}
    # manager[user] = passw
    with open("pass.txt", "r") as file:
        for line in file.readlines():
            try:
                data = line.rstrip()
                # data.replace(": ", ":").replace(" :", ":")
                user, passw = data.split(":")
                print(f"{user}: {fer.decrypt(passw.encode()).decode()}")  # key comes encoded in bytes hence decode
            except ValueError:
                print("Unable to parse")


def add():
    counter = 0
    user_count = int(input("how many: "))

    while user_count > counter:

        user = input("User: ").strip()
        pwd = input("Password: ").strip()

        if counter < 1:
            mode_select = "w"
        else:
            mode_select = "a+"

        try:
            with open("pass.txt", mode_select) as file:
                file.write(f"{user}:{fer.encrypt(pwd.encode()).decode()}\n")
                counter += 1

        except (FileExistsError, FileNotFoundError):
            print("File error")


while True:
    mode = input("Add or View: ").strip().lower()

    if mode == "q":
        break

    elif mode == "view":
        view()
        # break

    elif mode == "add":
        add()


    else:
        print("Invalid mode.")
        continue

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

"""

# get key in encoded bytes form and .decode() to remove 'b' tag -> encrypt message by .encrypt("msg".encode(), key)
# then Fernet(key).decrypt(encrypted.text) -> encoded msg which needs to be decoded
