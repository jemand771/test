import sys

from tabulate import tabulate


def main():
    results = sorted(sys.stdin.read().splitlines())
    header = ["tag"]
    lines = {}
    for r in results:
        tag, *args, elapsed = r.split(",")
        args = text_header(args)
        lines.setdefault(tag, [])
        lines[tag].append(elapsed)
        if args not in header:
            header.append(args)
    lines = [[k, *v] for k, v in lines.items()]
    print(tabulate(lines, headers=header, tablefmt="pretty"))


def text_header(args):
    
    return ",".join(x for x, control in zip(["diff-pdf", "synctex", "pythontex"], args) if control == "true")


if __name__ == "__main__":
    main()
