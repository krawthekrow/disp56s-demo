#!/bin/bash

set -eu

mkdir frames compressed-frames rickroll-lesscolors-frames
ffmpeg -y -i rickroll.mp4 -filter:v "crop=720:720:120:0" rickroll-square.mp4
ffmpeg -y -i rickroll-square.mp4 -s 56x56 -c:a copy rickroll-small.mp4
ffmpeg -y -i rickroll-small.mp4 -vf palettegen rickroll-palette.png
ffmpeg -y -i rickroll-small.mp4 -i rickroll-palette.png -filter_complex paletteuse -r 10 rickroll-small.gif
convert rickroll-small.gif -coalesce frames/rickroll-frame.png
python3 put-frames-into-single-image.py
convert rickroll-altogether.png +dither -colors 16 rickroll-altogether-lesscolors.png
python3 split-altogether.py
python3 compress-frames.py
python3 make-phot-data.py
# lua: import-phot-data.py

