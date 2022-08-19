import time

from filelock import FileLock

file_path = "test.txt"
lock_path = "test.txt.lock"


def test_case():
    lock = FileLock(lock_path, timeout=10)

    with lock:
        with open(file_path, "a") as f:
            f.write("I hate it when he does that.")
            time.sleep(15)
