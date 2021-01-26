from __future__ import annotations
import numpy as np
from typing import Union
from utils.utils import random_float, random_float_list


class Vec3:
    def __init__(self, e0: float = 0, e1: float = 0, e2: float =0) -> None:
        self.e: np.ndarray = np.array([e0, e1, e2], dtype=np.float32)

    def x(self) -> float:
        return self.e[0]

    def y(self) -> float:
        return self.e[1]

    def z(self) -> float:
        return self.e[2]

    def __getitem__(self, idx: int) -> float:
        return self.e[idx]

    def __str__(self) -> str:
        return f'{self.e[0]} {self.e[1]} {self.e[2]}'

    def length_squared(self) -> float:
        return self.e @ self.e

    def length(self) -> float:
        return np.sqrt(self.length_squared())

    def __add__(self, v: Vec3) -> Vec3:
        return Vec3(*(self.e + v.e))

    def __neg__(self) -> Vec3:
        return Vec3(*(-self.e))

    def __sub__(self, v: Vec3) -> Vec3:
        return self + (-v)

    def __mul__(self, v: Union[Vec3, int, float]) -> Vec3:
        if isinstance(v, Vec3):
            return Vec3(*(self.e * v.e))
        elif isinstance(v, (int, float, np.floating)):
            return Vec3(*(self.e * v))
        raise TypeError

    def __matmul__(self, v: Vec3) -> float:
        return self.e @ v.e

    def __truediv__(self, t: float) -> Vec3:
        return self * (1 / t)

    def __iadd__(self, v: Vec3) -> Vec3:
        self.e += v.e
        return self

    def __imul__(self, v: Union[Vec3, int, float]) -> Vec3:
        if isinstance(v, Vec3):
            self.e *= v.e
        elif isinstance(v, (int, float, np.floating)):
            self.e *= v
        else:
            raise TypeError
        return self

    def __itruediv__(self, t: float) -> Vec3:
        self *= (1 / t)
        return self

    def cross(self, v: Vec3) -> Vec3:
        return Vec3(*np.cross(self.e, v.e))

    def unit_vector(self) -> Vec3:
        return self / self.length()

    def clamp(self, _min: float, _max: float) -> Vec3:
        return Vec3(*np.clip(self.e, _min, _max))

    def gamma(self, gamma: float) -> Vec3:
        return Vec3(*(self.e ** (1 / gamma)))

    def reflect(self, n: Vec3) -> Vec3:
        return self - (n * (self @ n)) * 2

    def refract(self, normal: Vec3, etai_over_etat: float) -> Vec3:
        cos_theta: float = -self @ normal
        r_out_parallel: Vec3 = (self + normal * cos_theta) * etai_over_etat
        r_out_prep: Vec3 = normal * (-np.sqrt(1 - r_out_parallel.length_squared()))
        return r_out_parallel + r_out_prep

    @staticmethod
    def random(_min: float = 0, _max: float = 1) -> Vec3:
        return Vec3(*random_float_list(3, _min, _max))

    @staticmethod
    def random_in_unit_sphere() -> Vec3:
        while True:
            p: Vec3 = Vec3.random(-1, 1)
            if p.length_squared() >= 1:
                continue
            return p

    @staticmethod
    def random_unit_vector() -> Vec3:
        a: float = random_float(0, 2 * np.pi)
        z: float = random_float(-1, 1)
        r: float = np.sqrt(1 - z**2)
        return Vec3(r * np.cos(a), r*np.sin(a), z)

    @staticmethod
    def random_in_hemisphere(normal: Vec3) -> Vec3:
        in_unit_sphere: Vec3 = Vec3.random_in_unit_sphere()
        if in_unit_sphere @ normal > 0:
            return in_unit_sphere
        else:
            return -in_unit_sphere

    @staticmethod
    def random_in_unit_disk():
        while True:
            p = Vec3(random_float(-1, 1), random_float(-1, 1), 0)
            if p.length_squared() >= 1:
                continue
            return p


Point3 = Vec3
Color = Vec3
