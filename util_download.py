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
    os.system('temp\\ja.exe /s')
    os.remove('temp\\ja.exe')


def intellij(util):
    util.install_by_link('ij.exe')
    os.system('temp\\ij.exe /S /CONFIG=silent.config')
    os.remove('temp\\ij.exe')


def discord(util):
    util.install_by_link('dc.exe')
    os.system('temp\\dc.exe -s')
    os.remove('dc.exe')


def steam(util):
    util.install_by_link('st.exe')
    os.system('temp\\st.exe /S')
    os.remove('st.exe')


def obs(util):
    util.install_by_link('ob.exe')
    os.system('temp\\ob.exe /S')
    os.remove('ob.exe')