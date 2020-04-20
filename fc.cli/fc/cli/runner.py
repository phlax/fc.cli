
import os
import shlex
import subprocess
import sys
import time

import termcolor


class FatControllerRunner(object):

    def __init__(self):
        pass

    def cmd(self, command, *args):
        return subprocess.run(shlex.split(command) + list(args))

    def handle_exec(self, command, *args):
        self.cmd("docker-compose exec fat-controller %s" % command, *args)

    def handle_journalctl(self, *args):
        self.handle_exec("journalctl", *args)

    def handle_systemctl(self, *args):
        self.handle_exec("systemctl status", *args)

    def handle_compose(self, proctype, name, *args):
        if proctype == "s":
            proctype = "service"
        elif proctype == "d":
            proctype = "daemon"
        self.handle_exec(
            "/controller/bin/docker-compose "
            "-f /var/lib/controller/%ss/%s/docker-compose.yml -p %s_%s"
            % (proctype, name, proctype, name),
            *args)

    def run(self, command, *args):
        if command == "systemctl":
            self.handle_systemctl(*args)
        if command == "journalctl":
            self.handle_journalctl(*args)
        elif command == "compose":
            self.handle_compose(*args)
        elif command == "exec":
            self.handle_exec(*args)
