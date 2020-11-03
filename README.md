# Star Blast

In 1984, my brother Tony wrote this game for the Apple ][ and had it published as a listing in the January 1985 issue of Practical Computing.

This is an attempt to re-create that game from the listing and create a disk image able to run on an Apple ][ emulator.

## How to run

First boot into an [Apple 2 emulator](https://www.scullinsteel.com/apple//e). Then load the [Star Blast.dsk](https://github.com/paulsinnett/StarBlast/blob/main/Star%20Blast.dsk?raw=true) file as a disk image.

## Illegal op codes

This program contained a machine code routine embedded in the data that used an illegal 6502 op code. The listing as printed only works on later 65c02 models. However, as a quick hack you can change the data on line 1660:

```.bas
1640 DATA 0,234,234
```

## Converting the listing

To get my listing onto the Apple ][ I used the utility [AppleCommander](https://applecommander.github.io/). Although this program has lots of ways to export files from disk images, to get files onto it, you need to match the Apple's ASCII file format with the high bit set on each byte.

I used a python script to convert a standard text file to Apple's ASCII format.
