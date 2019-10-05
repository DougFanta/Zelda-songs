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

    mixer.music.load('musicas/menu_turn_left.wav')  # musica de efeito
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

    mixer.music.load('musicas/PauseMenu_Open.mp3')
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
        a = 'musicas/Zeldas lullaby.mp3'

        print("\033[1;35mZeldas lullaby")

    elif m == 'wadwad':
        a = 'musicas/Eponas Song.mp3'
        print("\033[1;33mEponas Song")

    elif m == 'sdasda':
        a = 'musicas/Lost Woods.mp3'
        print("\033[1;32mLost Woods")

    elif m == 'dswdsw':
        a = 'musicas/Suns Song.mp3'
        print("\033[1;33mLost Woods")

    elif m == 'dxsdxs':
        a = 'musicas/Song of Time.mp3'
        print("\033[1;36mSong of Time")

    elif m == 'xswxsw':
        a = 'musicas/Song of Storms.mp3'
        print("\033[1;36mSong of Storms")

    elif m == 'xwadad':
        a = 'musicas/Minuet of Forest.mp3'
        print("\033[1;32mMinuet of Forest")

    elif m == 'sxsxdsds':
        a = 'musicas/Bolero of Fire.mp3'
        print("\033[1;31mBolero of Fire")

    elif m == 'xsdda':
        a = 'musicas/Serenade of Water.mp3'
        print("\033[1;34mSerenade of Water")

    elif m == 'xsxsdsx':
        a = 'musicas/Requiem of Spirit.mp3'
        print("\033[1;30mRequiem of Spirit")

    elif m == 'addxads':
        a = 'musicas/Nocturne of Shadow.mp3'
        print("\033[1;37mNocturne of Shadow")

    elif m == 'wdwdaw':
        a = 'musicas/Prelude of light.mp3'
        print("\033[1;33mPrelude of light")

    elif m == 'e':
        mixer.music.load('musicas/PauseMenu_Close.mp3')
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
        mixer.music.load('musicas/Song_Error.wav')
        mixer.music.play()
        tempo = time.Clock()
        tempo.tick(0)
        while mixer.music.get_busy():
            tempo.tick(10)
    else:
        vet = ['musicas/Song_Correct.mp3', a]
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

musicas()
