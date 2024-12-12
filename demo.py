from PIL import Image
im = Image.open('clusterfuzz-testcase-minimized-fuzz_pillow-5015640213159936')
print(im)
im.load()