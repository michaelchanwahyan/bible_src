import os
import sys

# from greeklish.converter import Converter
# myconverter = Converter(max_expansions=4)

fn = sys.argv[1] # fn = 'MAT_gk.txt'

_ = os.system('clear')

greek_alphabet = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω'
latin_alphabet = 'AaBbGgDdEeZzHhJjIiKkLlMmNnXxOoPpRrSssTtUuFfQqYyWw'

greek_alphabet += '⸂⸀⸃ΐάέήίΰϊϋόἁἂᾳῃῆῳῶ'
latin_alphabet += '"""iaehiuiuoaaahhww'

greek_alphabet += 'ύώἀὴὶὸὺἃἄἅἆἈ'
latin_alphabet += 'uwahiouaaaaa'

greek_alphabet += 'ἉἌἐὲῖῦἑἓἔἕἘἙἜ'
latin_alphabet += 'aaeeiueeeeeee'

greek_alphabet += 'ἍἝἠἡἢἣἤἥἦἧἨἩἪἭἮἰἱἴἵἶἷἸ'
latin_alphabet += 'aehhhhhhhhhhhhhiiiiiii'

greek_alphabet += 'ἬἹἽὀὁὃὄὅὈὉὋὌὍὐὑὒὓὔὕὖὗὙὝ'
latin_alphabet += 'hiioooooooooouuuuuuuuyy'

greek_alphabet += 'ὠῇὡὢὤὥὦὧὩὩὭὮὯὼᾅᾐᾑᾔᾖᾗᾠᾧᾶᾷῄῇῒῢῥῬῴῷ'
latin_alphabet += 'whwwwwwwwwwwwwahhhhhwwaahhiurpww'

greek_alphabet += 'ὟὬᾄἋᾴἎἛὰ⸁ἳἼὂ'
latin_alphabet += 'ywaaaaea"iio'

greek_alphabet += '⸄'
latin_alphabet += '"'

greek_alphabet += '⸅'
latin_alphabet += '"'

greek2latin = str.maketrans(greek_alphabet, latin_alphabet)

with open(fn, 'r') as fp:
    lines = [ _.strip() for _ in fp.readlines() ]
fp.close()

# #print(myconverter.convert(u'μια φορά και έναν καιρό.')[1])
# for line in lines:
#     res = myconverter.convert(line)
#     if '/' in line:
#         print(res[0])
#         continue
#     print(res[1])

for line in lines:
    print(line.translate(greek2latin))
