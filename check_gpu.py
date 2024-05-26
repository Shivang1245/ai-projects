import torch

if torch.cuda.is_available():
    CPU = torch.cuda.get_device_name(0)
    VRAM = round(torch.cuda.get_device_properties(0).total_memory / 1024 ** 3)
    print(f"{GPU} is available with {VRAM}GB V-RAM")
    print("CUDA version: ", torch.version.cuda)

else:
    print("NO GPU AVAILABLE")
