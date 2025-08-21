import re

def validar_telefono(numero: str) -> bool:
    limpio = numero.replace(" ", "").replace("-", "")
    
    if limpio.startswith("+"):
        limpio = limpio[1:]
    
    if not limpio.isdigit():
        return False
    
    return 9 <= len(limpio) <= 12


