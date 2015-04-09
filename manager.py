#!venv/bin/python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


def runserver(args):
    from app import create_app
    create_app(config=args.config).run()

def runtests(args):
    from tests import run
    run(verbosity=args.verbosity)

def main():
    arg_parser = ArgumentParser()
    sub_parsers = arg_parser.add_subparsers()

    cmd_runserver = sub_parsers.add_parser('runserver',
            help='runs the Flask development Server')
    cmd_runserver.add_argument('--config', default='production',
            help='config to use, default: production')
    cmd_runserver.set_defaults(func=runserver)

    cmd_runtests = sub_parsers.add_parser('runtests',
            help='runs the test suite')
    cmd_runtests.add_argument('--verbosity', default=1, type=int,
            help='set unittest output verbosity, default: 1')
    cmd_runtests.set_defaults(func=runtests)

    args = arg_parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
