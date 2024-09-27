def przesuniecie(press_x, press_y, release_x, release_y):
    press_x = press_x // 60
    press_y = press_y // 60
    release_x = release_x // 60
    release_y = release_y // 60

    vec_x = release_x - press_x
    vec_y = release_y - press_y
    return press_x, press_y, release_x, release_y, vec_x, vec_y

