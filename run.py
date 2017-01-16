#!/usr/bin/env python3

import subprocess
import shlex

import sys

MIGRATE = shlex.split('python manage.py migrate --configuration Production')
COLLECTSTATIC = shlex.split('python manage.py collectstatic --no-input --configuration Production')
DJANGO_RUN = shlex.split('python manage.py runserver --configuration Production 0.0.0.0:8000')
PASSENGER = shlex.split('passenger start --environment production --address 0.0.0.0 --port 8000')


class Main:
    def __init__(self):
        self.commands = [
            MIGRATE,
            COLLECTSTATIC,
            PASSENGER
        ]

    def run_command(self, command):
        p = subprocess.Popen(args=command)
        while p.returncode is None:
            try:
                p.wait()
            except KeyboardInterrupt:
                pass
        return p.returncode

    def run(self):
        return_code = 0
        for c in self.commands:
            return_code = self.run_command(c)
            if return_code != 0:
                break

        return return_code


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())
