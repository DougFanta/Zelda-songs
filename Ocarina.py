# version 3.7.0

# Atualizado em 14/08/2019

# Autor: Douglas

''' O sistema Pede para que o usuário insira uma sequencia de teclas e verifica a sequencia digitada
    Se a sequencia estiver certa ele toca a musica, se não ele pede para digitar outra sequencia
    O programa fica rodando em loop até que o usuário digite a tecla E'''

# Inicio do código

from pygame import mixer, time # CARREGANDO a lib

mixer.init() # Inicialização do mixer


print('\033[1;36m-\033[m\033[1;32m=\033[m\033[1;31m-' * 27)
print('                      \033[1;32mZELDA OCARINA OF TIME SONGS') # read do programa
print('\033[1;36m-\033[m\033[1;32m=\033[m\033[1;31m-' * 27)


# lista de códigos
def lista():                               # função que mostra os códigos para tocar as musicas
    songs = ['\033[1;35mZelda´s lulabby: A W D A W D','\033[1;33mEpona´s song: W A D W A D',
             '\033[1;32mLost Woods: S D A S D A','\033[1;33mSun´s Song: D S W D S W',
             '\033[1;34mSong of time: D X S D X S','\033[1;36mSong of storms: X S W X S W',
             '\033[1;32mMinuet of forest: X W A D A D','\033[1;31mBolero of fire: S X S X D S D S',
             '\033[1;34mSerenade of water: X S D D A','\033[1;30mRequiem of spirit: X S X S D S X',
             '\033[1;37mNocturne of Shadow: A D D X A D S','\033[1;33mPrelude of light: W D W D A W']

    for i in songs:
        print(i)
    print(' ')

    mixer.music.load('menu_turn_left.wav')  # musica de efeito
    mixer.music.play()
    tempo = time.Clock()
    tempo.tick(10)
    while mixer.music.get_busy():
        tempo.tick(10)

    a = input('\033[4;32;36mPress ENTER to write a sequence\033[m')
    if a == '':
        print(musicas())
    else:
        print(lista())


    # repetição escolha para ir para a função que toca música


def musicas():    # função principal do programa onde se toca as musicas

    mixer.music.load('PauseMenu_Open.mp3')
    mixer.music.play()
    tempo = time.Clock()
    tempo.tick(0)
    while mixer.music.get_busy():
        tempo.tick(10)

    m = input(str('\033[1;30;mMake a sequence using \033[1;31mW A S D X\033[1;30mto play one song or help to open the song list or E to exit :\033[m')).strip().lower()
    a = ' '

    if m == 'help':
        print(lista())

    elif m == 'awdawd':
        a = 'Zeldas lullaby.mp3'

        print("\033[1;35m", a[:14])

    elif m == 'wadwad':
        a = 'Eponas Song.mp3'
        print("\033[1;33m", a[:11])

    elif m == 'sdasda':
        a = 'Lost Woods.mp3'
        print("\033[1;32m", a[:10])

    elif m == 'dswdsw':
        a = 'Suns Song.mp3'
        print("\033[1;33m", a[:9])

    elif m == 'dxsdxs':
        a = 'Song of Time.mp3'
        print("\033[1;36m", a[:12])

    elif m == 'xswxsw':
        a = 'Song of Storms.mp3'
        print("\033[1;36m", a[:14])

    elif m == 'xwadad':
        a = 'Minuet of Forest.mp3'
        print("\033[1;32m", a[:16])

    elif m == 'sxsxdsds':
        a = 'Bolero of Fire.mp3'
        print("\033[1;31m", a[:14])

    elif m == 'xsdda':
        a = 'Serenade of Water.mp3'
        print("\033[1;34m", a[:17])

    elif m == 'xsxsdsx':
        a = 'Requiem of Spirit.mp3'
        print("\033[1;30m", a[:17])

    elif m == 'addxads':
        a = 'Nocturne of Shadow.mp3'
        print("\033[1;37m", a[:18])

    elif m == 'wdwdaw':
        a = 'Prelude of light.mp3'
        print("\033[1;33m", a[:16])

    elif m == 'e':
        mixer.music.load('PauseMenu_Close.mp3')
        mixer.music.play()
        tempo = time.Clock()
        tempo.tick(0)
        while mixer.music.get_busy():
            tempo.tick(10)

        exit(0)

    else:
        print('\033[1;32mWrong Sequence')

    if a == ' ':

        print("\033[4;31mType another sequence\033[m")
        mixer.music.load('Song_Error.wav')
        mixer.music.play()
        tempo = time.Clock()
        tempo.tick(0)
        while mixer.music.get_busy():
            tempo.tick(10)
    else:
        vet = ['Song_Correct.mp3', a]
        for i in vet:
            mixer.music.load(i)
            mixer.music.play()
            mixer.music.set_volume(0.1)
            tempo = time.Clock()
            tempo.tick(0)
            while mixer.music.get_busy():
                tempo.tick(10)

    print(musicas())


# print para startar tudo

print(musicas())
