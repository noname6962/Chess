import legalnosc

def check_szach(biale_check, czarne_check, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura,moves):
    attack = []
    if tura % 2 == 0:
        for i, figura in enumerate(biale_check):
            if figura[2] == x and figura[3] == y and figura[1] == 1:
                figura_list = list(figura)
                figura_list[2] += vec_x
                figura_list[3] += vec_y
                biale_check[i] = tuple(figura_list)
                break
        for figura in czarne_check:
            if figura[1] == 1:
                for xx in range(-7, 8):
                    for yy in range(-7, 8):
                        if figura[2] + xx >= 0 and figura[2] + xx <= 7 and figura[3] + yy >= 0 and figura[3] + yy <= 7:
                            if legalnosc.check_check(biale_check, czarne_check, biale_pozycje, czarne_pozycje, figura[2], figura[3], xx, yy, tura, moves):
                                attack.append((figura[2]+xx, figura[3]+yy))
        for figura in biale_check:
            if figura[0] == 'K':
                if (figura[2], figura[3]) in attack:
                    print('Szach')
                    return 1
    else:
        for i, figura in enumerate(czarne_check):
            if figura[2] == x and figura[3] == y and figura[1] == 1:
                figura_list = list(figura)
                figura_list[2] += vec_x
                figura_list[3] += vec_y
                czarne_check[i] = tuple(figura_list)
                break
        for figura in biale_check:
            if figura[1] == 1:
                for xx in range(-7, 8):
                    for yy in range(-7, 8):
                        if figura[2] + xx >= 0 and figura[2] + xx <= 7 and figura[3] + yy >= 0 and figura[3] + yy <= 7:
                            if legalnosc.check_check(biale_check, czarne_check, biale_pozycje, czarne_pozycje, figura[2], figura[3], xx, yy, tura, moves):
                                attack.append((figura[2]+xx, figura[3]+yy))
        for figura in czarne_check:
            if figura[0] == 'K':
                if (figura[2], figura[3]) in attack:
                    print('Szach')
                    return 1
