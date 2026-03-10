from pathlib import Path
import sys

required_paths = [
    "README.md",
    "docs",
    "data",
    "notebooks",
    "adf",
    "screenshots"
]

missing = []

for path in required_paths:
    if not Path(path).exists():
        missing.append(path)

if missing:
    print("Missing required project items:")
    for item in missing:
        print(f"- {item}")
    sys.exit(1)

print("All required project files and folders exist.")