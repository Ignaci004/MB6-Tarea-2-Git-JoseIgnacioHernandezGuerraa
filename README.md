✅ RETO 6 — Validar número de teléfono simple
 Contexto: “Como usuario quiero verificar que mi teléfono tenga 9–12 dígitos.”
 Tests:
validar_telefono("987654321") → True


validar_telefono("+51-987654321") → True (si se permiten + y -) / validar_telefono("98A765") → False
 Código mínimo: Quitar espacios/guiones, opcional + al inicio; comprobar que queden sólo dígitos y longitud en rango.
