from dataclasses import dataclass


@dataclass
class Boat:
    name: str
    cost: int
    owned: bool
    equipped: bool
    hp: int
    image: str


boats = [
    Boat(
        name="Research Submarine",
        cost=0,
        owned=True,
        equipped=True,
        hp=100,
        image="submarine1.png"
    ),
    Boat(
        name="Special Submarine",
        cost=100,
        owned=False,
        equipped=False,
        hp=200,
        image="submarine2.png"
    ),
    Boat(
        name="Attack Submarine",
        cost=250,
        owned=False,
        equipped=False,
        hp=300,
        image="submarine3.png"
    ),
    Boat(
        name="Missile Submarine",
        cost=500,
        owned=False,
        equipped=False,
        hp=500,
        image="submarine4.png"
    ),
    Boat(
        name="Ballistic Submarine",
        cost=1000,
        owned=False,
        equipped=False,
        hp=800,
        image="submarine5.png"
    ),
]