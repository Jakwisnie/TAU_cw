import unittest

class Komendy():
    def __init__(self, nazwa_systemu):
        self.nazwa_systemu = nazwa_systemu

        self.komendy_linux = {
            'man': {
                'opis': 'informacje o danym poleceniu'
            },
            'mkdir': {
                'opis': 'tworzenie katalogu'
            },
            'ls': {
                'opis': 'pokazuje liste plikow w danej lokacji',
                '-a': 'pokazuje ukryte pliki'
            },
            'rm': {
                'opis': 'usuwa pliki',
                '*': 'usuwa wszystko z danego katalogu',
                '-r': 'usuwa pliki za potwierdzeniem',
                '-f': 'usuwa pliki nawet te zabezpieczone'
            },
            'chmod': {
                'opis': 'edycja dostepu do pliku'

            }
        }



        self.komendy_windows = {
            'sfc/scannow': {
                'opis': 'skanowanie systemu, jesli cos z plikow systemowych jest uszkodzone to skaner to naprawi'
            },
            'cipher': {
                'opis': 'trwałe nadpisywanie plików'
            },
            'shutdown': {
                'opis': 'zamkniecie systemu',
                'shutdown /s /t 0': 'zamkniecie systemu',
                'shutdown /r /t 0': 'restart systemu.',
                'shutdown /r /o' : 'restart systemu i ustawienie na ekran opcji startowych'
            },
            'ipconfig/flushdns': {
                'opis': 'oczyszczanie pamięci cache DNS’ów'

            },
            'ipconfig': {
                'opis':'wyswietl adres ip oraz dodatkowe informacje sieciowe'


            }
        }

        if nazwa_systemu == "Windows":
            self.komendy = self.komendy_windows
        elif nazwa_systemu == "Linux":
            self.komendy = self.komendy_linux
        else:
            raise Exception("Cos zle!")

    def czy_istnieje(self, komenda):
        komenda = komenda.lower()
        if not isinstance(komenda, str):
            return None
        good = komenda.lower().split()
        if len(good) < 1:
            return None
        return good

    def wyswietlanie(self, komenda):
        komenda = komenda.lower()
        dobra = self.czy_istnieje(komenda)
        if dobra is None:
            return None

        if dobra[0] in self.komendy:
            komenda = self.komendy[dobra[0]]
            if len(dobra) > 1:
                if dobra[1] in komenda:
                    return komenda[dobra[1]]
                else:
                    return komenda['opis']
            else:
                return komenda['opis']
        else:
            return None


class TestowanieKomend(unittest.TestCase):
    def test_system_name_windows(self):
        nazwa_systemu = "Windows"
        komendy = Komendy(nazwa_systemu)
        assert komendy.nazwa_systemu == nazwa_systemu

    def test_system_name_linux(self):
        nazwa_systemu = "Linux"
        komendy = Komendy(nazwa_systemu)
        assert komendy.nazwa_systemu == nazwa_systemu

class TestLinux(unittest.TestCase):
    def test_linux_ls(self):
        komenda = Komendy("Linux")
        wynik = komenda.wyswietlanie('man')
        assert wynik == 'informacje o danym poleceniu'

    def test_linux_ls_la(self):
        komenda = Komendy("Linux")
        wynik = komenda.wyswietlanie('mkdir')
        assert wynik == 'tworzenie katalogu'

    def test_linux_rm_f(self):
        komenda = Komendy("Linux")
        wynik = komenda.wyswietlanie('ls -a')
        assert wynik == 'pokazuje ukryte pliki'

    def test_linux_hostname_i(self):
        komenda = Komendy("Linux")
        wynik = komenda.wyswietlanie('rm *')
        assert wynik == 'usuwa wszystko z danego katalogu'

    def test_linux_uptime(self):
        komenda = Komendy("Linux")
        wynik = komenda.wyswietlanie('chmod')
        assert wynik == 'edycja dostepu do pliku'

class TestWindows(unittest.TestCase):
    def test_windows_cd(self):
        komenda = Komendy("Windows")
        wynik = komenda.wyswietlanie('sfc/scannow')
        assert wynik == 'skanowanie systemu, jesli cos z plikow systemowych jest uszkodzone to skaner to naprawi'

    def test_windows_mkdir(self):
        komenda = Komendy("Windows")
        wynik = komenda.wyswietlanie('cipher')
        assert wynik == 'trwałe nadpisywanie plików'

    def test_windows_shutdown_s(self):
        komenda = Komendy("Windows")
        wynik = komenda.wyswietlanie('shutdown')
        assert wynik == 'zamkniecie systemu'

    def test_windows_ping_t(self):
        komenda = Komendy("Windows")
        wynik = komenda.wyswietlanie('ipconfig/flushdns')
        assert wynik == 'oczyszczanie pamięci cache DNS’ów'

    def test_windows_ipconfig_all(self):
        komenda = Komendy("Windows")
        wynik = komenda.wyswietlanie('ipconfig')
        assert wynik == 'wyswietl adres ip oraz dodatkowe informacje sieciowe'


if __name__ == '__main__':
    unittest.main()