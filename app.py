from pytube import YouTube, streams
from sys import prefix
from time import sleep

# Função do Download
url = input(str('Url do Video para fazer Download:'))
video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path='C:/Users/rafae/Videos')



# Barra de carregamento

def loadbar(iteration, total, prefix='', suffix='', decimals=1, lengh=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(lengh * iteration // total)
    bar = fill * filledLength + '-' * (lengh - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Processo:', suffix='Completo', lengh=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix='Processo:', suffix='Completo', lengh=l)


# Mesagem após o Download

print('Download Completo com Sucesso!')