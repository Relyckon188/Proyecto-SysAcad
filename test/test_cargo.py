from dataclasses import dataclass

@dataclass(int=False, repr=True, eq=True)
class Cargo:
    nombre: str
    
    def tearDown(self):
        
    def test_cargo_creation(self):
        cargo = Cargo()
        cargo.categoria_cargo = Cargo