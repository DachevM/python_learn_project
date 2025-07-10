import os
from datetime import datetime
from pathlib import Path

cwd = os.getcwd()
print("Текущая директория:", cwd)

project_root = Path(__file__).parent
print("Текущая директория:", project_root)

data_dir = project_root / "logs"
output_file = data_dir / "app.log"

data_dir.mkdir(parents=True, exist_ok=True)
if data_dir.exists():
    output_file.touch()

print("Сущ", output_file)
print("Существует?", output_file.exists())
print("Файл?", output_file.is_file())

output_file.write_text(f"Текущая дата/время: {datetime.now()}\n", encoding="utf-8")
print(output_file.read_text(encoding="utf-8"))


def create_file():
    with open("logs/app.log", "w", encoding="utf-8") as f:
        f.write(f"Текущая дата/время {datetime.now()}\n")


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content
