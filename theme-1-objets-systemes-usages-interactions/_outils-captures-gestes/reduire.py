# Réduit les captures brutes : largeur max 1400 px (LANCZOS), palette 256 couleurs, PNG optimisé.
import sys, os
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
for f in sorted(os.listdir(src)):
    if not f.endswith('.png'): continue
    im = Image.open(os.path.join(src, f)).convert('RGB')
    w, h = im.size
    if w > 1400:
        im = im.resize((1400, round(h * 1400 / w)), Image.LANCZOS)
    im = im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    out = os.path.join(dst, f)
    im.save(out, optimize=True)
    print(f"{f}: {w}x{h} -> {im.size[0]}x{im.size[1]}  {os.path.getsize(out)//1024} Ko")
