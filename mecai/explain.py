def explain_solution(solution):
    if "error" in solution:
        return "No se pudo calcular la aceleración: " + solution["error"]
    a = solution["aceleracion"]
    return f"Usamos la segunda ley de Newton: F = m·a → a = F/m = {a} m/s²."