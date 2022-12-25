class PluginMount(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'): # 处理父类时，添加一个plugins属性
            cls.plugins = []
        else: # 加子类添加到列表
            cls.plugins.append(cls)

class InputValidator(metaclass=PluginMount):
    # a plugin
    def validate(self, input):
        raise NotImplementedError


class ASCIIValidator(InputValidator):
    def validate(self, input):
        input.encode('ascii')


def is_valid(input):
    for plugin in InputValidator.plugins:
        try:
            plugin().validate(input)
        except ValueError:
            return False
    return True

print(is_valid("aldfj"))


