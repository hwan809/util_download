from requests import get
import os
import util_download


CURRENT_PATH = os.getcwd()


SIDE_BAR = '_'
SIDE_BAR_LENGTH = 50

SIDE_BAR_STR = SIDE_BAR * SIDE_BAR_LENGTH


DOWNLOAD_LINK_KAKAO = 'https://app-pc.kakaocdn.net/talk/win32/KakaoTalk_Setup.exe'
DOWNLOAD_LINK_PYTHON = 'https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe'
DOWNLOAD_LINK_JAVA = 'https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe'
DOWNLOAD_LINK_INTELLIJ = 'https://download-cdn.jetbrains.com/idea/ideaIC-2021.3.2.exe'
DOWNLOAD_LINK_DISCORD = 'https://dl.discordapp.net/distro/app/stable/win/x86/1.0.9003/DiscordSetup.exe'
DOWNLOAD_LINK_STEAM = 'https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe'
DOWNLOAD_LINK_OBS = 'https://cdn-fastly.obsproject.com/downloads/OBS-Studio-27.1.3-Full-Installer-x64.exe'


UTIL_LIST = []


class Util:
    def __init__(self, util_name, util_code, util_link, util_function):
        self.name = util_name
        self.code = util_code
        self.link = util_link
        self.function = util_function

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def install_by_link(self, file_name):
        download_file(self.link, 'temp/' + file_name)

    def install(self):
        os.system('cls')

        print(SIDE_BAR_STR + '\n' +
              '\n' +
              f'[ {self.name} ] 설치 파일을 받아오는 중...'.center(SIDE_BAR_LENGTH - 10, ' ') + '\n' +
              '\n' +
              SIDE_BAR_STR + '\n')

        self.function(self)

        print('설치 완료.')


def download_file(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url)               # get request
        file.write(response.content)      # write to file


def set_util_list():
    UTIL_LIST.append(Util('카카오톡', 'K', DOWNLOAD_LINK_KAKAO, util_download.kakao))
    UTIL_LIST.append(Util('Python', 'P', DOWNLOAD_LINK_PYTHON, util_download.python))
    UTIL_LIST.append(Util('Java SDK', 'J', DOWNLOAD_LINK_JAVA, util_download.java))
    UTIL_LIST.append(Util('IntelliJ Community', 'I', DOWNLOAD_LINK_INTELLIJ, util_download.intellij))
    UTIL_LIST.append(Util('Discord', 'D', DOWNLOAD_LINK_DISCORD, util_download.discord))
    UTIL_LIST.append(Util('Steam', 'S', DOWNLOAD_LINK_STEAM, util_download.steam))
    UTIL_LIST.append(Util('OBS', 'O', DOWNLOAD_LINK_OBS, util_download.obs))


def main():
    os.system('cls')

    print(
          ' ## 유용 유틸 설치 By Vivace 22.02.12 ##' + '\n' +
          ' ' + SIDE_BAR_STR + '\n' +
          '\n' +
          ' [K] KakaoTalk              [P] Python 3.10.2\n' 
          ' [J] Java SDK 16.0.2        [I] IntelliJ Community 2021.3\n'
          ' [D] Discord                [S] Steam Game\n'
          ' [O] OBS 27.1.3\n')

    code = input(' [설치하실 프로그램을 선택해 주세요]: ')
    return code


if __name__ == '__main__':
    set_util_list()

    os.makedirs('temp', exist_ok=True)

    now_code = ' '

    while now_code != 'X':
        now_code = main().upper()

        for util in UTIL_LIST:
            if now_code == util.get_code():
                util.install()
                os.system('pause')

