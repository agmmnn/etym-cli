from etym_cli.cli import main
import argparse

# parse arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "word",
    type=str,
    nargs="*",
    help="<word>",
)
ap.add_argument(
    "-p", "--plain", action="store_true", default=False, help="plain text output"
)
args = ap.parse_args()


def cli():
    if "".join(args.word) != "":
        main("".join(args.word), args.plain)
    else:
        print("No word given.")


if __name__ == "__main__":
    cli()
