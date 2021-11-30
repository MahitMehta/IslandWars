import platform, sys
from cx_Freeze import setup, Executable

if platform.system() == 'Windows':
    bin_inc = './env/lib/pygame'
    name = 'island_wars.exe'
else:
    bin_inc = './env/lib/pygame'
    name = 'island_wars'

buildOptionsEXE = dict(packages = ['pygame'], excludes = [],
        include_files = ['assets', 'icon.ico', 'icon.icns'],
        bin_path_includes=bin_inc,
    )


buildOptionsMSI = dict(packages = ['pygame'], excludes = [],
        include_files = ['assets', 'icon.ico', 'icon.icns'],
        bin_path_includes=bin_inc,
        Icon=[
            ("IconId", "icon.ico"),
        ],
    )


buildOptionsMAC = dict(packages = ['pygame'], excludes = [],
        include_files = ['assets', 'icon.icns'],
        bin_path_includes=bin_inc,
        iconfile='icon.icns',
)

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable('main.py', targetName=name, base = base, icon="icon.ico",)
]

setup(name='Island Wars',
      version = '1.0',
      description = '2 Player Game',
      copyright = "Mahit Mehta 2021",
      options = { 
           "build_mac": buildOptionsMAC, 
           "build_exe": buildOptionsEXE,
           "build_msi": buildOptionsMSI 
        },
      executables = executables)