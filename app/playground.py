def read_file(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"Ошибка чтения файла: {e}")
        return None


read_file("data.json")

fruits = ["apple", "banana", "cherry"]
fruits_length = [len(x) for x in fruits]


def create_file():
    with open("fruits.txt", "w", encoding="utf-8") as f:
        for fruit in fruits:
            f.write(f"{fruit}\n")
    with open("fruits.txt", "r", encoding="utf-8") as f:
        print(f.read())


create_file()
