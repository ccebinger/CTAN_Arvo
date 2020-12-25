#!/usr/bin/fontforge -lang=py
from os.path import splitext
from sys import argv
import fontforge
for file in argv[1:]:
  font=fontforge.open(file)
  font.em = 1000
  font.generate(splitext(file)[0] + ".otf")

