#!/usr/bin/env python3
"""Reproduce the demo's SAM pass on any photo. Stdlib only.

Usage:
    cp .env.example .env   # then put your key in .env (never committed)
    python3 scripts/describe_scene.py photo.jpg "loose screw"
    # ...or META_API_KEY=<yours> python3 scripts/describe_scene.py photo.jpg "loose screw"

Prints JSON: {"concept", "size": [w, h], "boxes": [[x1,y1,x2,y2], ...]}.
Boxes are raw SAM output -- overlay-verify before trusting them, exactly as
the demo does (see docs/scene/describe-result.md for the magnet rejection).

Needs a Meta API key with sam-3.1 access. Never prints the key.
"""
import base64
import json
import os
import re
import struct
import sys
import urllib.request

META_URL = "https://api.meta.ai/v1/responses"
BOX_RE = re.compile(r"<\\|box;x1=(\d+);y1=(\d+);x2=(\d+);y2=(\d+);")


def jpeg_size(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG")
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return [w, h]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        (length,) = struct.unpack(">H", data[i + 2:i + 4])
        i += 2 + length
    raise ValueError("no SOF marker found")


def load_dotenv():
    try:
        with open(".env") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    except OSError:
        pass


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: describe_scene.py photo.jpg \"concept\"")
    photo, concept = sys.argv[1], sys.argv[2]
    load_dotenv()
    key = os.environ.get("META_API_KEY", "")
    if not key or not all(33 <= ord(c) <= 126 for c in key):
        sys.exit("set META_API_KEY to your Meta API key")
    with open(photo, "rb") as f:
        body = f.read()
    size = jpeg_size(photo)
    payload = {
        "model": "sam-3.1",
        "stream": False,
        "metadata": {"mask_encoding": "one_bit"},
        "input": [
            {
                "type": "message",
                "role": "user",
                "content": [
                    {"type": "input_text", "text": concept},
                    {
                        "type": "input_image",
                        "image_url": "data:image/jpeg;base64," + base64.b64encode(body).decode("ascii"),
                    },
                ],
            }
        ],
    }
    req = urllib.request.Request(
        META_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + key},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=110) as resp:
        result = json.load(resp)
    text = json.dumps(result)
    boxes = [[int(a), int(b), int(c), int(d)] for a, b, c, d in BOX_RE.findall(text)]
    print(json.dumps({"concept": concept, "size": size, "boxes": boxes}, indent=1))


if __name__ == "__main__":
    main()
