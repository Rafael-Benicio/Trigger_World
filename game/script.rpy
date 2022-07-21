# Definir configuraçãos do jogo

# Definir personagens
define Eu = Character("Maria",what_color="#ffffff",what_prefix='"',what_suffix='"',who_color="#fff",)
# Definições Pensamento
define Pensamento = Character(what_color="#ffffff", what_prefix='"{i}',what_suffix='"{/i}',who_color="#fff",)
# Definições da Amadi
define Amadi = Character("Amadi",kind=Eu,who_color="#ffe989",)
# Definições da Yun
define Yun = Character("Yun",kind=Eu,who_color="#ff4d4d",)
# Definições da Alo
define Alo = Character("Alo",kind=Eu,who_color="#fff34d",)
# Definições da Seraphina
define Serafina = Character("Serafina",kind=Eu,who_color="#59ffd6",)
# Definições da Nikka
define Nikka = Character("Nikka",kind=Eu,who_color="#4845ff",)
# Definições da Sophia
define Sophia = Character("Sophia",kind=Eu,who_color="#11ff2c",)
# Definições da Aneti
define Aneti = Character("Aneti",kind=Eu,who_color="#e72eff",)
# Definições da Hina
define Hina = Character("Hina",kind=Eu,who_color="#ff2a9e",)
# Definições da Olivia
define Olivia = Character("Olivia",kind=Eu,who_color="#ffa8d2",)
# Definições Diretora
define Alice = Character("Alice (Diretora)",kind=Eu,who_color="#fca7ff")
# Definições Professora Celia
define Celia = Character("Célia (Professora)",kind=Eu,who_color="#ff4949")
# Definições Mulher da Cantina
define Artemisia = Character("Artemísia (Cantina)",kind=Eu,who_color="#30f9f9")
# Definições Professora Celia
define Kae = Character("Kae (Professora)",kind=Eu,who_color="#a3a")
# Definições Lemu
define Lemu = Character("Lemu",kind=Eu,who_color="#0f0")
# Definições Pensamento
define Narrador = Character(what_color="#bbb")
# Definições Desconhecido
define Desconhecido = Character("???",kind=Eu,who_color="#ccc",)
# Definições Ser-Cosmico
define Cosmico = Character("®ŋħ←?°øß→",
                            kind=Eu,
                            who_color="#304",
                            who_italic=True,
                            what_italic=True,
                            what_color="#ff0",
                            what_prefix='-',
                            what_suffix='-',)

# Definições
## Posição
transform midLeft:
    xalign 0.25
    yalign 1.0

transform midRight:
    xalign 0.75
    yalign 1.0

## Transições
define slowFade= Fade(1.0, 1.0, 1.0, color="#000") 

define flash = Fade(0.5, 1.0,0.5,color="#fff")

define slowFlash = Fade(0.5, 2.5,2.0,color="#fff")

define slowDissolve= Dissolve(1.0)

define quickDissolve= Dissolve(0.25)

## Imagens

# Inicio do jogo
# Chegada na Cidade
label start:

    jump chapter01
