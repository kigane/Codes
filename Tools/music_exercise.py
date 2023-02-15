import random

from pysynth import *

# from pysynth_b import *

num_to_note_dict = {
    '0': 'r',
    '1': 'c',
    '2': 'd',
    '3': 'e',
    '4': 'f',
    '5': 'g',
    '6': 'a',
    '7': 'b',
}

# 1 2 3 4 5 6 7
# c d e f g a b
song = (
    ('e', 4), ('c', 8), ('f', 8), ('e', 4),
    ('c', 8), ('f', 8), ('e', 4), ('f', 8), ('e', 8), ('r', 8),
    ('e', 4), ('d', 8), ('c', 8), ('d', 4),
    ('g', 4), ('e', 4), ('f', 8), ('e', 8),
)


def process_song(s: str, t: str):
    song = []
    for note, l in zip(s, t):
        song.append((num_to_note_dict[note], int(l)))
    return song


def nums_to_clip(nums: str):
    assert len(nums) > 0, "输入为空"
    clip = []
    for x in nums:
        if int(x) > 7 or int(x) < 0:
            print(f"输入不合法 {x}")
            return
        clip.append((num_to_note_dict[x], 4))
    return clip


def gen_random_exer(name='excer.wav', bpm=90):
    ret = ''
    for i in range(8):
        ret += str(random.randint(1, 7))
    make_wav(nums_to_clip(ret), fn=name, bpm=bpm)
    return ret


if __name__ == '__main__':
    print(gen_random_exer())

    # exer1 = '314314343321'
    # make_wav(nums_to_clip(exer1), fn="exer1.wav", bpm=80)

    # song = '31431434332125343'
    # leng = '48848848848844488'
    # make_wav(process_song(song, leng), fn="exer.wav", bpm=80)
