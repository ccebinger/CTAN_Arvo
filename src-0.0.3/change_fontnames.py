#
#   Modify the CHANGES table as needed, then call
#
#       FontForge -lang=py -script change_fontnames.py <font files>
#

import sys

import fontforge


CHANGES = [
    ("Arvo",   "Arv0"),
#    ("Merriweather Sans",   "MerriwthrSans"),
#    ("MerriweatherSans",    "MerriwthrSans"),
]


def modify(name):
    for (old, new) in CHANGES:
        if old in name:
            return name.replace(old, new, 1)

    raise ValueError(
        "None of the 'old' names matched '" + name + "', nothing changed!")


for filename in sys.argv[1:]:
    font = fontforge.open(filename)

    try:
        font.familyname = modify(font.familyname)
        font.fullname = modify(font.fullname)
        font.fontname = modify(font.fontname)

        filename_out = modify(filename)
    except ValueError as e:
        print(e)
        next

    sfnt = list(font.sfnt_names)
    for i, t in enumerate(sfnt):
        if t[1] in ["Family", "Preferred Family"]:
            sfnt[i] = (t[0], t[1], font.familyname)
        elif t[1] in ["Fullname"]:
            sfnt[i] = (t[0], t[1], font.fullname)
        elif t[1] in ["PostscriptName"]:
            sfnt[i] = (t[0], t[1], font.fontname)
    font.sfnt_names = tuple(sfnt)

    font.generate(filename_out)

