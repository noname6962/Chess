import legalnosc
import move
import szach
def pozycje(biale_figury, czarne_figury):

    biale_pozycje= []
    czarne_pozycje = []

    for figury in biale_figury:
        if figury[1] == 1:
            biale_pozycje.append((figury[2], figury[3]))
    for figury in czarne_figury:
        if figury[1] == 1:
            czarne_pozycje.append((figury[2], figury[3]))

    return biale_pozycje, czarne_pozycje


def ruch(biale_figury, czarne_figury, x, y, vec_x, vec_y, tura, moves):
    biale_pozycje, czarne_pozycje = pozycje(biale_figury, czarne_figury)
    if move.move(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura, moves):
        return 1

