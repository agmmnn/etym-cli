from etym_cli.cli import main
import argparse

__version__ = "0.0.3"

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
ap.add_argument(
    "-t", "--trend", action="store_true", default=False, help="returns trending words"
)
ap.add_argument(
    "-f",
    "--fuzzy",
    action="store_true",
    default=False,
    help="returns fuzzy search results",
)
ap.add_argument("-v", "--version", action="version", version="%(prog)s v" + __version__)
args = ap.parse_args()


def cli():
    word = "".join(args.word)
    if word != "":
        main(word, args.plain, args.trend, args.fuzzy)
    elif args.trend:
        main(word, args.plain, args.trend, args.fuzzy)
    elif args.fuzzy:
        main(word, args.plain, args.trend, args.fuzzy)
    else:
        print("No word given.")


if __name__ == "__main__":
    cli()
