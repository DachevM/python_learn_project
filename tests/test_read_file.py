from app.playground import read_file


def test_read_file_success(tmp_path):
    file = tmp_path / "temp.txt"
    content = "Hello, pytest!"
    file.write_text(content, encoding="utf-8")

    result = read_file(str(file))
    assert result == content


def test_read_file_not_found(tmp_path, capsys):
    missing = tmp_path / "no.txt"
    result = read_file(str(missing))

    captured = capsys.readouterr()
    assert result is None
    assert "Ошибка чтения файла" in captured.out
