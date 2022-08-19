import csv
import io
import shutil


def test_case1():
    with open("test1.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["col1-val1", "col2-val1", "col3-val1"])


def test_case2():
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter=",")
    writer.writerow(["col1-val1", "col2-val1", "col3-val1"])

    with open("test2.csv", "w", encoding="utf-8-sig", newline="") as file:
        buffer.seek(0)
        shutil.copyfileobj(buffer, file)
