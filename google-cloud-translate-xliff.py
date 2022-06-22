#!/usr/bin/env python3

import datetime

from translate.storage.xliff import xlifffile
from google.cloud import translate_v2

now = datetime.datetime.now()  # used to create the output file without
                               # overwriting anything
dumpfilename = now.strftime("%Y%m%d_%H%M%S-translation.txt")

XLIFF_FILENAME = "flarum-core-en.xlf"
SOURCE_LANGUAGE = "en"
TARGET_LANGUAGE = "pt"

a = open(XLIFF_FILENAME, 'r')

translate_client = translate_v2.Client()  # have you creds ready here

b = a.read()  # str()
c = b.encode('utf-8')  # bytes()

d = xlifffile(inputfile=c, sourcelanguage=SOURCE_LANGUAGE,
              targetlanguage=TARGET_LANGUAGE)

# d.getunits() -> list[xliffunit]
# e = d.getunits()[0]  # first xliffunit, as `unit` in the `for` below

totalunits = len(d.getunits())

for number, unit in enumerate(d.getunits()):
   res = translate_client.translate(unit.gettarget(),
                                    target_language=TARGET_LANGUAGE,
                                    format_="text")

   howmuch = "({}/{})".format(number, totalunits)
   source = res['input']
   translation = res['translatedText']
   print(howmuch, source, translation, sep='\n', end="\n\n")

   unit.settarget(translation, lang=TARGET_LANGUAGE)

   #if number > 11:
   #    break

d.savefile(dumpfilename)

print("Done.")

