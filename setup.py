import platform
from cx_Freeze import setup, Executable

if platform.system() == 'Windows':
    bin_inc = './env/lib/pygame'
    name = 'island_wars.exe'
else:
    bin_inc = './env/lib/pygame'
    name = 'island_wars'

buildOptions = dict(packages = ['pygame'], excludes = [],
        include_files = ['assets'],
        bin_path_includes=bin_inc)

executables = [
    Executable('main.py', targetName=name)
]

setup(name='island_wars',
      version = '1.0',
      description = '2 Player Game',
      options = dict(build_exe = buildOptions),
      executables = executables)