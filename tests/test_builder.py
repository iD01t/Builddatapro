import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import builder


def test_build_command_defaults():
    cmd = builder.build_command('script.py', 'dist')
    assert 'pyinstaller' in cmd[0]
    assert '--onefile' in cmd
    assert '--noconsole' in cmd
    assert '--distpath=dist' in cmd

def test_build_command_custom():
    cmd = builder.build_command('s.py', 'out', onefile=False, windowed=False, icon='icon.ico', additional='--clean')
    assert '--onefile' not in cmd
    assert '--noconsole' not in cmd
    assert '--icon=icon.ico' in cmd
    assert '--clean' in cmd

