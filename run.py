import pyfiglet
from termcolor import colored

def generate_ascii_art(text, font="standard"):
    """
    Menghasilkan seni ASCII dari teks yang diberikan dengan menggunakan font tertentu.
    
    Parameters:
    text (str): Teks yang ingin diubah menjadi seni ASCII.
    font (str): Nama font yang digunakan untuk membuat seni ASCII.
    
    Returns:
    str: Seni ASCII yang dihasilkan.
    """
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art

def change_text_color(text, color="white"):
    """
    Mengubah warna teks.
    
    Parameters:
    text (str): Teks yang ingin diubah warnanya.
    color (str): Warna baru untuk teks.
    
    Returns:
    str: Teks dengan warna baru.
    """
    colored_text = colored(text, color)
    return colored_text

if __name__ == "__main__":
    # Meminta pengguna untuk memasukkan teks
    input_text = input("Masukkan teks yang ingin diperbagus: ")

    # Membuat seni ASCII dari teks
    ascii_art = generate_ascii_art(input_text)

    # Menampilkan seni ASCII dengan warna kuning
    colored_ascii_art = change_text_color(ascii_art, "yellow")
    print(colored_ascii_art)
