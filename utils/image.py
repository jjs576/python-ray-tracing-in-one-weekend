from __future__ import annotations
import numpy as np
from PIL import Image
from utils.vec3 import Color


class Img:
    def __init__(self, w: int, h: int) -> None:
        self.frame: np.ndarray = np.zeros((h, w, 3), dtype=np.float32)

    def set_array(self, array: np.ndarray) -> None:
        self.frame = array

    def write_pixel(self, w: int, h: int, pixel_color: Color, samples_per_pixel: int) -> None:
        color: Color = pixel_color / samples_per_pixel
        self.frame[h][w] = color.clamp(0, 0.999).gamma(2).e

    def save(self, path: str, show: bool = False) -> None:
        im = Image.fromarray(np.uint8(self.frame * 255))
        im.save(path)
        if show:
            im.show()
