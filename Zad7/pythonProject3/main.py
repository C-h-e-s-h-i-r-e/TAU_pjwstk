class Commands:

    def __init__(self, system_name):

        self.commands_windows = {
            'cd': {
                '': 'Displays the current directory and lets you switch to other directories.',
                '/d': 'Changes the current drive as well as the current directory for a drive.'
            },
            'cls': {
                '': 'Clears the content of the screen.'
            },
            'dir': {
                '': 'Displays all folders and files within the current directory.'
            },
            'mkdir': {
                '': 'Creates a new directory on the specified path.'
            },
            'tree': {
                '': 'Graphically displays the directory structure of a drive or path.'
            }
        }

        self.commands_linux = {
            'ls': {
                '': 'List information about file(s).',
                '--sort': 'Sort files.'
            },
            'apt': {
                '': 'Search for and install software packages.'
            },
            'clear': {
                '': 'Clear terminal screen.'
            },
            'echo': {
                '': 'Display message on screen.'
            },
            'mkdir': {
                '': 'Create new folder(s).'
            }
        }

        if system_name == "Windows":
            self.commands = self.commands_windows
        elif system_name == "Linux":
            self.commands = self.commands_linux
        else:
            raise Exception("Wrong System.")

        self.system_name = system_name

    def correct_command(self, wrong_command):
        if not isinstance(wrong_command, str):
            return None
        x = wrong_command.lower().split(" ")
        if len(x) < 1:
            return None
        return x

    def help(self, wrong_command):
        x = self.correct_command(wrong_command)
        if x is None:
            return None

        if x[0] in self.commands:
            command = self.commands[x[0]]
            if len(x) > 1:
                if x[1] in command:
                    return command[x[1]]
                else:
                    return command['']
            else:
                return command['']
        else:
            return None


def lab7func(n):
    if type(n) is not int:
        return None
    elif n < 5 or n > 5:
        return None
    elif n == 5:
        return 1
