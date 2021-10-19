#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Pre-commit hook for PEP 8 style guidelines using pycodestyle."""

import argparse
from sys import executable

from .._internal.util import SubprocessError

from .._internal.commands.sanity.pep8 import (
    pep8_cmd,
)

from .._internal.util_common import (
    run_command,
)


class DummyConfig:
    def __init__(self):
        self.explain = False


def main(argv=None):
    parser = argparse.ArgumentParser(description='Runs \'pycodestyle\' with Ansible\'s configurations')
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    cmd = pep8_cmd(executable, args.filenames)

    try:
        stdout, stderr = run_command(DummyConfig(), cmd, capture=True)
        rc = 0
    except SubprocessError as ex:
        stdout = ex.stdout
        stderr = ex.stderr
        rc = ex.status

    print("\n".join([stdout, stderr]))
    return rc


if __name__ == 'main':
    exit(main())
