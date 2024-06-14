#!/usr/bin/python3

import os
import argparse


def count_words(file):
    with open(file, "r") as f:
        words = f.read().split()
    return len(words)


def read_lines(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return len(lines)


def count_bytes(file):
    byte_size = os.stat(file).st_size
    return byte_size


def count_chars(file):
    with open(file, "r") as f:
        chars = f.read().strip(" ").strip("\n")
    return len(chars)


def wc(file):
    lines = read_lines(file)
    words = count_words(file)
    chars = count_chars(file)
    return lines, words, chars


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="file to count")
    parser.add_argument("-l", "--lines", help="count lines", action="store_true")
    parser.add_argument(
        "-c", "--chars", help="count number of bytes", action="store_true"
    )
    parser.add_argument(
        "-w", "--words", help="count number of words", action="store_true"
    )

    parser.add_argument(
        "-m" "--characters", help="count number of characters", action="store_true"
    )

    args = parser.parse_args()
    commands = []
    if args.lines:
        words = read_lines(args.file)
        commands.append(words)

    if args.chars:
        chars = count_bytes(args.file)
        commands.append(chars)

    if args.words:
        words = count_words(args.file)
        commands.append(words)

    if args.m__characters:
        chars = count_chars(args.file)
        commands.append(chars)

    print(" ".join(map(str, commands)) + " " + args.file)


if __name__ == "__main__":
    main()
