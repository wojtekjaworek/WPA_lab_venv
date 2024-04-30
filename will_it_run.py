import matplotlib
import re

def check_matplotlib_version():
    version = matplotlib.__version__
    match = re.match(r'^(\d+)\.(\d+)', version)
    if match:
        major_version, minor_version = map(int, match.groups())
        if major_version == 3 and minor_version == 8:
            print("Matplotlib w wersji 3.8, program powinien działać poprawnie.")
        elif major_version == 3:
            print(f"Wersja Matplotlib {major_version}.{minor_version}, mogą pojawić się problemy.")
        else:
            print(f"Wersja Matplotlib {major_version}.{minor_version}, program może nie działać!.")
    else:
        print("Nie udało się określić wersji Matplotlib.")

if __name__ == "__main__":
    check_matplotlib_version()
