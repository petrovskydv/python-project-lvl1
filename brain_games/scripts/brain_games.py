#!/usr/bin/env python
from brain_games.cli import get_name


def main():
    print('Welcome to the Brain Games!')
    name = get_name()
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
