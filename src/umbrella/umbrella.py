#!/usr/bin/env python3

import argparse
import logging
import path_utils
from command_provider import CommandProvider

log_path = f'{path_utils.datadir()}/main.log'
logging.basicConfig(filename=log_path)
logger = logging.getLogger(__name__)


def get_command_name() -> str:
    arg_name: str = 'command'
    parser = argparse.ArgumentParser()
    parser.add_argument(
        arg_name,
        choices=["info", "start", "stop"]
    )
    return vars(parser.parse_args()).get(arg_name)


def run_command(command_name: str):
    command_provider = CommandProvider()
    if command_name == 'info':
        command_provider.do_info()
    elif command_name == 'start':
        command_provider.do_start()
    elif command_name == 'stop':
        command_provider.do_stop()
    else:
        raise TypeError(f'Unsupported command name: {str}')


if __name__ == '__main__':
    logger.info("Umbrella run")
    run_command(get_command_name())
