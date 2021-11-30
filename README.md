Islands wars is a 2 player game where players fight to see who is the last one remaining.

Commands
- env
    - . env/bin/activate
    - deactivate

- Build (Windows)
    - python setup.py build 
    - python setup.py bdist_msi
    
- Build (MacOS)
    - remove ./env/lib/pygame/examples
    - python setup.py bdist_mac --iconfile=icon.icns
    - python setup.py bdist_dmg 