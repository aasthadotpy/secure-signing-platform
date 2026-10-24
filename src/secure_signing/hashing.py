import hashlib
from pathlib import Path

CHUNK_SIZE = 1024 * 1024

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with open(path, "rb") as file: # "rb" is reading in Binary mode
        while True:
            chunk = file.read(CHUNK_SIZE)

            if not chunk: #reached EOF, i.e, 0 bytes
                break

            digest.update(chunk)

    return digest.hexdigest()

if __name__ == "__main__":
    path = Path("hello.txt")
    print(sha256_file(path))