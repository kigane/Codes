import importlib
import importlib.util


class A(object):
    def __init__(self) -> None:
        pass

    foo = "foo"


class B(A):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':
    importlib.import_module('other')
    importlib.import_module('Tools.music_exercise', 'Tools')
    spec = importlib.util.spec_from_file_location(
        'a', 'Tools/music_exercise.py')
    a = spec.loader.load_module()
    print(a.song)
    print('done!!!')

    print(B.foo)
