
@dataclass(init=False, repr=True, eq=True)
class Autoridad():
    nombre: str
    cargo: Cargo
    