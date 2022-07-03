import argparse
from collections import namedtuple
from typing import Optional


def parse(argv: Optional[list[str]]) -> tuple[namedtuple, list[str]]:
    """parse command line arguments
    Args:
        argv (list[str]): command-line arguments
    Returns:
        argparse.Namespace: parsed objects with attributes
    """
    parser = argparse.ArgumentParser(description='command-line parser')
    parser.add_argument('--verbose', action='store_true',
                        default=False, help='DEBUG logging level')
    parser.add_argument('--apiserver_token', required=True,
                        help='ApiServer token')
    parser.add_argument('--apiserver_host', required=False,
                        help='ApiServer host', default="https://localhost")
    parser.add_argument('--apiserver_port', required=False,
                        help='ApiServer port', default="4443")
    parser.add_argument('--adminserver_token',
                        required=True, help='AdminServer token')
    parser.add_argument('--adminserver_host', required=False,
                        help='AdminServer host', default="https://localhost")
    parser.add_argument('--adminserver_port', required=False,
                        help='AdminServer port', default="4445")
    args, remaining = parser.parse_known_args(argv)
    return args, remaining


def valid_port(port: str) -> str:
    if not port.isnumeric():
        raise TypeError("Port number must be numeric value")
    if (int(port) < 1 or int(port) > 65535):
        raise argparse.ArgumentError("Invalid port number")
    return port
