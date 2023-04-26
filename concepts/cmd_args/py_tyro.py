

# tyro is a tool for building command-line interfaces and configuration objects in Python.
# Our core interface, tyro.cli(), generates command-line interfaces from type-annotated callables.

"""Sum two numbers from argparse."""
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--a", type=int, required=True)
# parser.add_argument("--b", type=int, default=3)
# args = parser.parse_args()

# total = args.a + args.b

# print(total)


"""Sum two numbers by calling a function with tyro."""
# import tyro

# def add(a: int, b: int = 3) -> int:
#     return a + b

# # Populate the inputs of add(), call it, then return the output.
# # 从函数的参数中推断需要的命令行参数
# total = tyro.cli(add)

# print(total)


"""Sum two numbers by instantiating a dataclass with tyro."""
from dataclasses import dataclass

import tyro

@dataclass
class Args:
    a: int
    b: int = 3

args = tyro.cli(Args)
print(args.a + args.b)