#!/usr/bin/env python3

import argparse
from crontab import CronTab


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
    cron = CronTab(user=True)
    job = cron.new(command='echo Start-start-start')
    job.minute.every(1)
    cron.write()


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


def run_command(command_name: str):
    if command_name == 'info':
        do_info()
    elif command_name == 'start':
        do_start()
    elif command_name == 'stop':
        do_stop()
    else:
        raise TypeError(f'Unsupported command name: {str}')


if __name__ == '__main__':
    run_command(get_command_name())
