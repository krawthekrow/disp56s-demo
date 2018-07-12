import subprocess

for i in range(150):
    subprocess.call(['convert', 'rickroll-lesscolors-frames/rickroll-lesscolors-%d.png' % i, '+dither', '-colors', '4', '-remap', 'rickroll-altogether-lesscolors.png', 'compressed-frames/rickroll-frame-compressed-%d.png' % i])
