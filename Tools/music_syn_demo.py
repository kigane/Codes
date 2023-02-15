import pysynth
from pysynth_b import *

# pysynth_X 对应不同音色

# ('c', 8)：演奏C4一个八分音符的长度
# 元组第一个元素表示音名: c4组的后缀可以省略。可以在其后添加'#'或'b'表示身高或降低半音。在其后再添加*表示这个音声音大一点。r表示休止符0。
# 元组的第二个元素表示音符的长度:
# 1：全音符
# 2：二分音符
# 4：四分音符
# 8: 八分音符

song = (
    ('c', 4),
    ('c*', 4), ('e', 4), ('g', 4),
    ('g*', 2), ('g5', 4),
    ('g5*', 4), ('r', 4), ('e5', 4),
    ('e5*', 4)
)

make_wav(song, fn="danube.wav", leg_stac=.7, bpm=180)