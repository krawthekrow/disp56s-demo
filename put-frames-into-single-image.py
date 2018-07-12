import png

def getimg(filename):
    return png.Reader(filename=filename).read()

WIDTH, HEIGHT = 56, 56
NUM_FRAMES = 150
res = []
colors = []
output_img = []
for frame in range(NUM_FRAMES):
    img = getimg('frames/rickroll-frame-%d.png' % (frame + 3))
    if img[3]['greyscale']:
        raise Exception('whut')
    if not 'palette' in img[3]:
        raise Exception('whut')
    palette = img[3]['palette']
    pixmap = list(img[2])

    for i in range(HEIGHT):
        curr_row = []
        for j in range(WIDTH):
            curr_row += list(palette[pixmap[i][j]])
        output_img += [tuple(curr_row)]
f = open('rickroll-altogether.png', 'wb')
w = png.Writer(WIDTH, HEIGHT * NUM_FRAMES)
w.write(f, output_img)
f.close()
