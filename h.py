from mutagen.mp3 import MP3

def info_lenght_mp3_file(file_mp3):
    mp3 = MP3(file_mp3)
    g = mp3.info.length
    value = g / 60
    return value


