
import sys

from .runner import FatControllerRunner


class FatControllerCommand(object):
    description = "CLI for fatc container management"

    def run(self, *args, **kwargs):
        """Run command."""
        # ...mangle... args
        #
        command = args[0]
        FatControllerRunner().run(command, *args[1:])


def main():
    FatControllerCommand().run(*sys.argv[1:])


if __name__ == "__main__":
    main()
