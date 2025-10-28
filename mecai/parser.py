def parse_problem(text):
    """
    Convierte texto tipo 'masa=2kg, fuerza=10N' en un diccionario con valores numéricos
    """
    datos = {}
    partes = text.replace(" ", "").split(",")
    for p in partes:
        if "=" in p:
            variable, valor = p.split("=")
            if "kg" in valor:
                datos["masa"] = float(valor.replace("kg", ""))
            elif "N" in valor:
                datos["fuerza"] = float(valor.replace("N", ""))
            elif "m/s2" in valor or "m/s^2" in valor:
                datos["aceleracion"] = float(valor.replace("m/s2", "").replace("m/s^2", ""))
    return datos