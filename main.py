from mecai.solver import solve_problem
from mecai.explain import explain_solution

def main():
    print("🤖 Bienvenido al Agente de IA de Mecánica Clásica")
    problem = input("Describe el problema (por ejemplo: masa=2kg, fuerza=10N): ")

    solution = solve_problem(problem)
    explanation = explain_solution(solution)

    print("\nResultado:")
    print(solution)
    print("\nExplicación:")
    print(explanation)

if __name__ == "__main__":
    main()