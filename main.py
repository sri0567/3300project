import json
import sys
from jsonHandler import JSONHandler

def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 main.py input.json")

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        data = json.load(f)

    result = JSONHandler(data).run()
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()