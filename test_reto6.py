from reto6 import validar_telefono

def test_validar_telefono():
    assert validar_telefono("987654321") == True
    assert validar_telefono("+51-987654321") == True
    assert validar_telefono("98A765") == False


