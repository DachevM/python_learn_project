import os
from fs_demo.fs_example import create_file, read_file


def test_create_and_read_file(tmp_path):
    logs_dir = tmp_path / "logs"
    logs_dir.mkdir()

    os.chdir(tmp_path)

    create_file()
    content = read_file(str(logs_dir / "app.log"))
    assert "Текущая дата/время" in content
