import torch
import os

path = "assets/ckpts/corneo_makima.pt"

ret = torch.load(path, map_location="cpu")
print(ret)
print(ret["string_to_param"]["*"].shape)
