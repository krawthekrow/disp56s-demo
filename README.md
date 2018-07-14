This is the code used to generate the demo for DISP56S.

This is just intended as an example, and I do not guarantee that it will work on your computer even with all dependencies installed. You will also need to find your own ``rickroll.mp4``.

The steps are listed in ``rickroll-convert.sh``. It crops the video into a square, scales it down to 56x56, sets a global limit of 16 colors (by putting all frames into one image and applying -colors 16), reduces each frame to a maximum of 5 colors, and converts the pixel data into FILT data. You will need to do the last step, which is to import the FILT data into TPT, yourself.
