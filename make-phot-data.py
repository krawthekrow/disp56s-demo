import png

def getimg(filename):
    return png.Reader(filename=filename).read()

WIDTH, HEIGHT = 56, 56
HALF_WIDTH, HALF_HEIGHT = int(WIDTH/2), int(HEIGHT/2)
NUM_FRAMES = 150
res = []
colors = []
f = open('rickroll-data.txt', 'w')
f_cols = open('rickroll-colors.txt', 'w')
for frame in range(NUM_FRAMES):
    img = getimg('compressed-frames/rickroll-frame-compressed-%d.png' % frame)
    if img[3]['greyscale']:
        raise Exception('whut')
    if not 'palette' in img[3]:
        raise Exception('whut')
    palette = img[3]['palette']
    if len(palette) > 5:
        raise Exception('whut')
    pixmap = list(img[2])

    actual_palette = []
    actual_palette_map = {}
    for pi in range(len(palette)):
        col_index = len(colors)
        found_actual_palette = False
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if pixmap[i][j] == pi:
                    found_actual_palette = True
        for k in range(len(colors)):
            if colors[k] == palette[pi]:
                col_index = k
                break
        if found_actual_palette:
            actual_palette_map[pi] = len(actual_palette)
            actual_palette += [col_index]
        if col_index == len(colors):
            colors += [palette[pi]]

    subimages = []
    for pi in range(len(actual_palette)):
        subimage = []
        for i in range(HEIGHT):
            subimage += [[0] * WIDTH]
        subimages += [subimage]

    for i in range(HEIGHT):
        for j in range(WIDTH):
            subimages[actual_palette_map[pixmap[i][j]]][i][j] = 1

    for i in range(HEIGHT):
        for j in range(WIDTH):
            found_si = False
            for si in range(len(subimages)):
                if subimages[si][i][j] == 1:
                    found_si = True
                    break
            if not found_si:
                raise Exception('whut')

    for si in range(len(subimages)):
        for i in range(HEIGHT):
            firstNum = 0
            for j in range(HALF_WIDTH):
                firstNum <<= 1
                if subimages[si][i][WIDTH - j * 2 - 2] != 1:
                    firstNum |= 1
            secondNum = 0
            for j in range(HALF_WIDTH):
                secondNum <<= 1
                if subimages[si][i][WIDTH - j * 2 - 1] != 1:
                    secondNum |= 1
            # f.write(format(firstNum, '028b') + ' ' + format(secondNum, '028b') + '\n')
            f.write(str(firstNum) + '\n')
            f.write(str(secondNum) + '\n')
        control_word = actual_palette[si]
        if si == len(subimages) - 1:
            control_word |= (1 << 28)
        f.write(str(control_word) + '\n')
    # f.write('\n')

for i in range(len(colors)):
    f_cols.write(str(colors[i][0]) + '\n')
    f_cols.write(str(colors[i][1]) + '\n')
    f_cols.write(str(colors[i][2]) + '\n')
f.close()
f_cols.close()
