from __future__ import annotations
import argparse

def app() -> None:
    parser = argparse.ArgumentParser(
        prog="hello",
        description="Say hello from a clean Python CLI starter.",
    )
    parser.add_argument("--name", "-n", default="World", help="Who to greet")
    args = parser.parse_args()

    print(f"Hello, {args.name}! 🎉")

if __name__ == "__main__":
    app()
