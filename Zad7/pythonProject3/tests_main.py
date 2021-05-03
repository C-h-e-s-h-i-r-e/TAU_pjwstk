from main import Commands
import pytest
from main import lab7func


class TestsWindows:
    def test_wrong_system(self):
        system_name = "Widnows2.0"
        with pytest.raises(Exception):
            Commands(system_name)

    def test_windows_cd(self):
        command = Commands("Windows")
        assert command.help('cd') == 'Displays the current directory and lets you switch to other directories.'

    def test_windows_cdd(self):
        command = Commands("Windows")
        assert command.help('cd /d') == 'Changes the current drive as well as the current directory for a drive.'

    def test_windows_cls(self):
        command = Commands("Windows")
        assert command.help('cls') == 'Clears the content of the screen.'

    def test_windows_dir(self):
        command = Commands("Windows")
        assert command.help('dir') == 'Displays all folders and files within the current directory.'

    def test_windows_mkdir(self):
        command = Commands("Windows")
        assert command.help('mkdir') == 'Creates a new directory on the specified path.'

    def test_windows_tree(self):
        command = Commands("Windows")
        assert command.help('tree') == 'Graphically displays the directory structure of a drive or path.'

    def test_windows_None(self):
        command = Commands("Windows")
        assert command.help('foo') is None


class TestsLinux:
    def test_wrong_system(self):
        system_name = "Linux2.0"
        with pytest.raises(Exception):
            Commands(system_name)

    def test_linux_ls(self):
        command = Commands("Linux")
        assert command.help('ls') == 'List information about file(s).'

    def test_linux_lssort(self):
        command = Commands("Linux")
        assert command.help('ls --sort') == 'Sort files.'

    def test_linux_apt(self):
        command = Commands("Linux")
        assert command.help('apt') == 'Search for and install software packages.'

    def test_linux_clear(self):
        command = Commands("Linux")
        assert command.help('clear') == 'Clear terminal screen.'

    def test_linux_echo(self):
        command = Commands("Linux")
        assert command.help('echo') == 'Display message on screen.'

    def test_linux_mkdir(self):
        command = Commands("Linux")
        assert command.help('mkdir') == 'Create new folder(s).'

    def test_linux_None(self):
        command = Commands("Linux")
        assert command.help('foo') is None


class TestParaTests:
    test_data = [(10, None), (-10, None), ("foo", None), (5.55, None), (-5.55, None), (float(6.66), None), (float(-6.66), None), ("5", None), (5, 1)]

    @pytest.mark.parametrize("tdata,result", test_data)
    def test_func(tdata, result):
        assert lab7func(tdata) == result