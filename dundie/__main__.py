import argparse


def load(filepath):
    """Loads data from file to database"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found {e}")


def main():

    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use with caution!",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="the subcommand to run",
        choices=("load", "show", "send"),
        default="help"
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="file path to load from",
        default=None
    )
    args = parser.parse_args()


    globals()[args.subcommand](args.filepath)


if __name__ == "__main__":
    main()
