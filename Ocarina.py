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
print('                      \033[1;32mZELDA OCARINA OF TIME SONGS') 
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
    print('\n')

    mixer.music.load('musicas/menu_turn_left.ogg')  # musica de efeito
    mixer.music.play()
    tempo = time.Clock()
    tempo.tick(10)
    while mixer.music.get_busy():
        tempo.tick(10)

    musicas()


    # repetição escolha para ir para a função que toca música


def musicas():    # função principal do programa onde se toca as musicas

    mixer.music.load('musicas/PauseMenu_Open.ogg')
    mixer.music.play()
    tempo = time.Clock()
    tempo.tick(0)
    while mixer.music.get_busy():
        tempo.tick(10)
        
    try:

        sequence = input(str('\033[1;30;mMake a sequence using \033[1;31mW A S D X\033[1;30;m to play one song or help to open the song list or E to exit :\033[m')).strip().lower()
    
        song = ' '


        if sequence == 'help':
            lista()

        elif sequence == 'awdawd':
            song = 'musicas/Zeldas_lullaby.ogg'

            print("\033[1;35mZeldas lullaby")

        elif sequence == 'wadwad':
            song = 'musicas/Eponas_Song.ogg'
            print("\033[1;33mEponas Song")

        elif sequence == 'sdasda':
            song = 'musicas/Lost_Woods.ogg'
            print("\033[1;32mLost Woods")

        elif sequence == 'dswdsw':
            song = 'musicas/Suns_Song.ogg'
            print("\033[1;33mSun's Song")

        elif sequence == 'dxsdxs':
            song = 'musicas/Song_of_Time.ogg'
            print("\033[1;36mSong of Time")

        elif sequence == 'xswxsw':
            song = 'musicas/Song_of_Storms.ogg'
            print("\033[1;36mSong of Storms")

        elif sequence == 'xwadad':
            song = 'musicas/Minuet_of_Forest.ogg'
            print("\033[1;32mMinuet of Forest")

        elif sequence == 'sxsxdsds':
            song = 'musicas/Bolero_of_Fire.ogg'
            print("\033[1;31mBolero of Fire")

        elif sequence == 'xsdda':
            song = 'musicas/Serenade_of_Water.ogg'
            print("\033[1;34mSerenade of Water")

        elif sequence == 'xsxsdsx':
            song = 'musicas/Requiem_of)Spirit.ogg'
            print("\033[1;30mRequiem of Spirit")

        elif sequence == 'addxads':
            song = 'musicas/Nocturne_of_Shadow.ogg'
            print("\033[1;37mNocturne of Shadow")

        elif sequence == 'wdwdaw':
            song = 'musicas/Prelude_of_Light.ogg'
            print("\033[1;33mPrelude of light")

        elif sequence == 'secret':
            song = 'musicas/Secret.ogg'
            print("\033[1;37mSecret song")

        elif sequence == 'e':
            mixer.music.load('musicas/PauseMenu_Close.ogg')
            mixer.music.play()
            tempo = time.Clock()
            tempo.tick(0)
            while mixer.music.get_busy():
                tempo.tick(10)

            exit(0)

        else:
            print('\033[1;32mWrong Sequence')


        if song == ' ':

            print("\033[4;31mType another sequence\033[m")
            mixer.music.load('musicas/Song_Error.ogg')
            mixer.music.play()
            tempo = time.Clock()
            tempo.tick(0)
            while mixer.music.get_busy():
                tempo.tick(10)
        else:
            vet = ['musicas/Song_Correct.ogg', song]
            for i in vet:
                mixer.music.load(i)
                mixer.music.play()
                mixer.music.set_volume(0.1)
                tempo = time.Clock()
                tempo.tick(0)
                while mixer.music.get_busy():
                    tempo.tick(10)

    except EOFError:
        print('Please type an sequence')
        musicas()

    except KeyboardInterrupt:   
        exit(0)
    
    musicas()


# print para startar tudo

musicas()
