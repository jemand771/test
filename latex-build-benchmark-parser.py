import sys

from tabulate import tabulate


def main():
    results = sorted(sys.stdin.read().splitlines())
    header = ["tag"]
    lines = {}
    for r in results:
        tag, *args, elapsed = r.split(",")
        args = "-".join(args)
        lines.setdefault(tag, [])
        lines[tag].append(elapsed)
        if args not in header:
            header.append(args)
    lines = [[k, *v] for k, v in lines.items()]
    print(tabulate(lines, headers=header, tablefmt="pretty"))


if __name__ == "__main__":
    main()
