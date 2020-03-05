# Python Version

1.  Find the list of planets under a particular star inside of Urbit using Hoon:

        =p (turn (gulf 0x1 0xffff) |=(a/@ `@p`(cat 4 ~dopzod a)))
        *%/web/planets/txt (turn p |=(a/@p (scot %p a)))

2.  Copy that resulting file, `web/planets.txt`, from your pier to this directory.

3.  `python solar-system.py` will scan and produce the list of planets with components from `english-words.txt`.  Planets with double components (such as `winter-hatred`) will be output in bold.

