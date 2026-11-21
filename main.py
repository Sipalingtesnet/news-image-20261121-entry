#!/usr/bin/env python3
"""Copy the generated entry.png to the output location, verifying its hash."""
import hashlib
import os
import shutil
import sys

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(REPO_DIR, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_hash = sha256(SRC)
    dst_hash = sha256(dst)
    if src_hash != dst_hash:
        print("ERROR: hash mismatch", file=sys.stderr)
        return 1
    print(src_hash)
    return 0


if __name__ == "__main__":
    sys.exit(main())