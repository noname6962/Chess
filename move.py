import legalnosc
import szach
def move(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura, moves):

    legality = legalnosc.check_check(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura, moves)

    if legality == 1 or legality == 2 or legality == 3:
        if szach.check_szach(biale_figury, czarne_figury, biale_pozycje, czarne_pozycje, x, y, vec_x, vec_y, tura, moves) != 1:
            if tura % 2 == 0:
                for i, figura in enumerate(biale_figury):
                    # Convert tuple to list
                    figura_list = list(figura)
                    # wybor figury
                    if figura_list[2] == x and figura_list[3] == y and figura_list[1] == 1:
                        if legality == 2:
                            moves.append(('biale', 'Pe', x, y, x+vec_x, y+vec_y))
                        elif legality == 3:
                            moves.append(('biale', 'O-O', x, y, x+vec_x, y+vec_y))
                        else:
                            moves.append(('biale', figura[0], x, y, x+vec_x, y+vec_y))

                        figura_list[2] += vec_x
                        figura_list[3] += vec_y

                        if legality == 3:
                            for j, wieza in enumerate(biale_figury):
                                if (wieza[2] == figura_list[2] + 2 and wieza[3] == figura_list[3] and wieza[1] == 1):
                                    wieza_list = list(wieza)
                                    wieza_list[2] -= 3
                                    biale_figury[j] = tuple(wieza_list)
                                    break
                                elif (wieza[2] == figura_list[2] - 1 and wieza[3] == figura_list[3] and wieza[1] == 1):
                                    wieza_list = list(wieza)
                                    wieza_list[2] += 2
                                    biale_figury[j] = tuple(wieza_list)
                                    break

                        #promocja pionka
                        if figura_list[3] == 7 and figura_list[0] == 'P':
                            figura_list[0] = 'D'

                        # Convert list back to tuple
                        biale_figury[i] = tuple(figura_list)
                        for j, czarna_figura in enumerate(czarne_figury):
                            czarna_figura_list = list(czarna_figura)
                            if legality == 2:
                                if czarna_figura_list[2] == x + vec_x and czarna_figura_list[3] == y and czarna_figura_list[1] == 1:
                                    czarna_figura_list[1] = 0
                                    czarne_figury[j] = tuple(czarna_figura_list)
                                    break
                            elif czarna_figura_list[2] == x + vec_x and czarna_figura_list[3] == y + vec_y and czarna_figura_list[1] == 1:
                                czarna_figura_list[1] = 0
                                czarne_figury[j] = tuple(czarna_figura_list)
                                break
            else:
                for i, figura in enumerate(czarne_figury):
                    # Convert tuple to list
                    figura_list = list(figura)
                    # wybor figury
                    if figura_list[2] == x and figura_list[3] == y and figura_list[1] == 1:
                        if legality == 2:
                            moves.append(('czarne', 'Pe', x, y, x+vec_x, y+vec_y))
                        elif legality == 3:
                            moves.append(('czarne', 'O-O', x, y, x+vec_x, y+vec_y))
                        else:
                            moves.append(('czarne', figura[0], x, y, x+vec_x, y+vec_y))

                        figura_list[2] += vec_x
                        figura_list[3] += vec_y

                        if legality == 3:
                            for j, wieza in enumerate(czarne_figury):
                                if (wieza[2] == figura_list[2] + 2 and wieza[3] == figura_list[3] and wieza[1] == 1):
                                    wieza_list = list(wieza)
                                    wieza_list[2] -= 3
                                    czarne_figury[j] = tuple(wieza_list)
                                    break
                                elif (wieza[2] == figura_list[2] - 1 and wieza[3] == figura_list[3] and wieza[1] == 1):
                                    wieza_list = list(wieza)
                                    wieza_list[2] += 2
                                    czarne_figury[j] = tuple(wieza_list)
                                    break

                        #promocja pionka
                        if figura_list[3] == 0 and figura_list[0] == 'P':
                            figura_list[0] = 'D'
                        # Convert list back to tuple
                        czarne_figury[i] = tuple(figura_list)
                        for j, biala_figura in enumerate(biale_figury):
                            biala_figura_list = list(biala_figura)
                            if legality == 2:
                                if biala_figura_list[2] == x + vec_x and biala_figura_list[3] == y and biala_figura_list[1] == 1:
                                    biala_figura_list[1] = 0
                                    biale_figury[j] = tuple(biala_figura_list)
                                    break
                            elif biala_figura_list[2] == x + vec_x and biala_figura_list[3] == y + vec_y and biala_figura_list[1] == 1:
                                biala_figura_list[1] = 0
                                biale_figury[j] = tuple(biala_figura_list)
                                break
            return 1
