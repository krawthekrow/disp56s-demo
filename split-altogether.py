import png

def getimg(filename):
    return png.Reader(filename=filename).read()

WIDTH, HEIGHT = 56, 56
res = []
colors = []
img = getimg('rickroll-altogether-lesscolors.png')
NUM_FRAMES = int(img[1] / HEIGHT)
if img[3]['greyscale']:
    raise Exception('whut')
if not 'palette' in img[3]:
    raise Exception('whut')
palette = img[3]['palette']
pixmap = list(img[2])
for frame in range(NUM_FRAMES):
    output_img = []
    for i in range(HEIGHT):
        curr_row = []
        for j in range(WIDTH):
            curr_row += list(palette[pixmap[i + HEIGHT * frame][j]])
        output_img += [tuple(curr_row)]
    f = open('rickroll-lesscolors-frames/rickroll-lesscolors-%d.png' % frame, 'wb')
    w = png.Writer(WIDTH, HEIGHT)
    w.write(f, output_img)
    f.close()

