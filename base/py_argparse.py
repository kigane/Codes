import argparse

# %(prog)s 程序名称，可以在help字符串中引用
# 程序名称来自sys.arg[0] 或 prog关键字参数
# usage可以用来修改帮助信息的第一行usage:xx.py [-h] ...
# epilog
parser = argparse.ArgumentParser(
    prog='PROG',
    usage='%(prog)s [options]',
    description='A brief description of this program',
    epilog='epilog shows in the very end of help messages')
# 位置参数
# parser.add_argument("echo", help="echo the string you use here")
# 默认 type=str
# parser.add_argument("square", type=int, help="square the numbers")

# 可选参数/选项 有前缀'-'
# 短选项， 长选项， help=显示的帮助信息
# action = 'store_true' 若选项出现，则将其设为True
#        = 'store_const' 根据选项是否出现将其设为 const=xxx 指定的值xxx
#        = 'count' 将选项的出现次数设为其值。 -vvv ==> args.verbose == 3。未出现则存 None
#        = 'store' 存储参数的值。这是默认的动作。后面有参数则存储参数，无则存储 None
# default = xx 选项的默认值
# dest=xx 选项将存储在args.dest中
# metavar 显示在help中的名称
parser.add_argument('-v', '--verbose', action='store_true', help='show %(prog)s verbose message')
parser.add_argument('--foo', metavar='F', dest='f')
parser.add_argument('--patch_size', type=int, nargs="+", default=[256, 256],
                    help='patch size of network input')
parser.add_argument('--num_classes', type=int,  default=4,
                    help='output channel of network')
# 不使用默认的位置参数，可选参数分组，而是自定义分组
# group = parser.add_argument_group('group', 'group_description)
# group.add_argumaent(...)

# 互斥选项放在一个互斥组中
# group = parser.add_mutually_exclusive_group()
# group.add_argumaent(...)

args = parser.parse_args()
# args, unknown_arg_list = parse_known_args()

# print(args.echo)
# print(args.square ** 2)
print(args)
