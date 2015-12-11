pacman -S --needed wmctrl hicolor-icon-theme python-dbus python-pyinotify zenity xautomation imagemagick xorg-xwd
# dependencies for GTK GUI, install only if you intend to use the GTK GUI.
pacman -S --needed python-gobject gtksourceview3 libnotify python-pip
# dependencies for QT GUI, install only if you intend to use the QT GUI.
# pacman -S --needed python-qscintilla kdebindings-python
# execute as non root
pip3 install --user python3-xlib
# install AutoKey-Py3 from PyPI or …
pip3 install --user autokey-py3
# get the development version from GitHub
# pip3 install --user git+https://github.com/guoci/autokey-py3