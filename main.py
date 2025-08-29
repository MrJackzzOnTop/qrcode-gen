import qrcode
import os
import sys
from colorama import Fore
import time

if sys.platform == 'win32':
    os.system("cls")
else:
    os.system("clear")

banner = """
 ░░      ░░░       ░░░░      ░░░░      ░░░       ░░░        ░░░░░░░░░      ░░░        ░░   ░░░  ░
 ▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒    ▒▒  ▒
 ▓  ▓▓ ▓  ▓▓       ▓▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓▓      ▓▓▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓      ▓▓▓▓  ▓  ▓  ▓
 █  ███   ██  ███  ███  ████  ██  ████  ██  ████  ██  ██████████████  ████  ██  ████████  ██    █
 ██      █ █  ████  ███      ████      ███       ███        █████████      ███        ██  ███   █
                                                                                                
    """

credits = """
                     _____________________________________
                    |                                     |
                    |  Coded by: github.com/MrJackzzOnTop |
                    |_____________________________________|

"""

def main():
    print(banner + Fore.GREEN)
    print(credits + Fore.YELLOW)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    data = input(" [?] Enter the URL OR Text that will contain the Qr Code: ")

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    File = input(" [?] Enter the filename to save (ex: QR.png): ")
    if not File.strip():
        File = "QRcode.png"

    img.save(File)

    print(f" [!] QR code generated and saved as {File}!" + Fore.CYAN)
    time.sleep(2)

def menu():
    while True:
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        print(banner + Fore.GREEN)
        print(credits + Fore.YELLOW)
        print(" [1] Generate another Qr Code")
        print(" [2] Exit" + Fore.CYAN)
        choice = input(" [?] Select your choice: " + Fore.GREEN)

        if choice == "1":
            if sys.platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")
            main()
        elif choice == "2":
            exit()
        else:
            print(" [!] Invalid option, program closed.")
            return


if __name__ == '__main__':
    main()
    menu()