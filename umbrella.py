#!/usr/bin/env python3

import argparse
from argparse import ArgumentParser, Namespace
from typing import Dict, Any


def do_info() -> None:
    """
    Invoke Info command
    """
    print(f"Command Info")


def do_start() -> None:
    """
    Invoke Start command
    """
    print(f"Command Start")


def do_stop() -> None:
    """
    Invoke Stop command
    """
    print(f"Command Stop")


def get_command_name() -> str:
    arg_name: str = 'command'
    parser = argparse.ArgumentParser()
    parser.add_argument(
        arg_name,
        choices=["info", "start", "stop"]
    )
    return vars(parser.parse_args()).get(arg_name)


if __name__ == '__main__':
    print(get_command_name())
