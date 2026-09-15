"""Chroma-key a flat green-screen render into a transparent PNG.

Run:  python tools/chroma_key.py <in.png> <out.png>

The AI stills in generated/ are rendered on a uniform chroma green so they can
be cut out for the layers the site composites with real alpha
(public/fin/man.png, public/projects/person.png).
"""

import sys

import numpy as np
from PIL import Image


def key(src, dst):
    im = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
    r, g, b = im[..., 0], im[..., 1], im[..., 2]
    # greenness: how far the pixel sits above the other two channels
    grn = g - np.maximum(r, b)
    # soft key: pure green -> 0 alpha, neutral/dark/warm -> 1
    alpha = np.clip(1.0 - (grn - 18.0) / 46.0, 0.0, 1.0)
    # despill: never let green outrun the warmer channels on edge pixels
    g2 = np.minimum(g, np.maximum(r, b) + 24.0)
    out = np.stack([r, g2, b, alpha * 255.0], -1).astype(np.uint8)
    Image.fromarray(out, "RGBA").save(dst)
    print("%s -> %s  (clear %.1f%%  opaque %.1f%%)" %
          (src, dst, (alpha < 0.05).mean() * 100, (alpha > 0.95).mean() * 100))


if __name__ == "__main__":
    key(sys.argv[1], sys.argv[2])
