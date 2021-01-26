from __future__ import annotations
from utils.vec3 import Vec3, Point3


class Ray:
    def __init__(self, origin: Point3 = Point3(), direction: Vec3 = Vec3()) -> None:
        self.origin = origin
        self.direction = direction

    def at(self, t: float) -> Point3:
        return self.origin + self.direction * t
