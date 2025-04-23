

from dataclasses import dataclass
from app.models.categoria_cargo import CategoriaCargo, TipoDedicacion


@dataclass(init=False, repr=True, eq=True)
class Cargo:
    nombre: str
    puntos: int
    categoria_cargo: CategoriaCargo
    tipo_dedicacion: TipoDedicacion
    