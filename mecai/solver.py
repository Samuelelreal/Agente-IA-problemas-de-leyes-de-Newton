from mecai.parser import parse_problem

def solve_problem(problem_text):
    """
    Resuelve un problema de la forma: masa=2kg, fuerza=10N
    Devuelve la aceleración aplicando la segunda ley de Newton: F = m * a
    """
    data = parse_problem(problem_text)
    if "fuerza" in data and "masa" in data:
        fuerza = data["fuerza"]
        masa = data["masa"]
        aceleracion = fuerza / masa
        return {"aceleracion": aceleracion, "unidad": "m/s^2"}
    else:
        return {"error": "Faltan datos (masa o fuerza)"}