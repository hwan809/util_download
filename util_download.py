from requests import get
import os


def kakao(util):
    util.install_by_link('ka.exe')
    os.system('temp\\ka.exe /S')
    os.remove('temp\\ka.exe')


def python(util):
    util.install_by_link('py.exe')
    os.system('temp\\py.exe /quiet InstallAllUsers=1 PrependPath=1')
    os.remove('temp\\py.exe')


def java(util):
    util.install_by_link('ja.exe')
    os.system('temp\\ja.exe /S')
    os.remove('temp\\ja.exe')
