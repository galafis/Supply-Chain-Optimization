
import pulp
import matplotlib.pyplot as plt
import numpy as np

def solve_transportation_problem(costs, supplies, demands, supplier_names=None, customer_names=None):
    """
    Resolve um problema de transporte usando programação linear.

    Args:
        costs (list of lists): Matriz de custos de transporte de cada fornecedor para cada cliente.
        supplies (list): Lista de capacidades de fornecimento de cada fornecedor.
        demands (list): Lista de demandas de cada cliente.
        supplier_names (list, optional): Nomes dos fornecedores. Defaults to None.
        customer_names (list, optional): Nomes dos clientes. Defaults to None.

    Returns:
        dict: Um dicionário contendo o status da solução, o custo total e as quantidades transportadas.
    """
    num_suppliers = len(supplies)
    num_customers = len(demands)

    # Verificação de depuração para 'costs'
    if not isinstance(costs, list) or not all(isinstance(row, list) for row in costs):
        raise TypeError("Costs deve ser uma lista de listas.")
    if len(costs) != num_suppliers or any(len(row) != num_customers for row in costs):
        raise ValueError("As dimensões de costs não correspondem ao número de fornecedores e clientes.")

    if supplier_names is None:
        supplier_names = [f"Fornecedor_{i+1}" for i in range(num_suppliers)]
    if customer_names is None:
        customer_names = [f"Cliente_{j+1}" for j in range(num_customers)]

    # Criar o problema de otimização
    prob = pulp.LpProblem("Supply Chain Transportation Problem", pulp.LpMinimize)
    # Variáveis de decisão: x[i][j] é a quantidade transportada do fornecedor i para o cliente j
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_suppliers) for j in range(num_customers)), lowBound=0, cat=pulp.LpContinuous)

    # Função objetivo: Minimizar o custo total de transporte
    prob += pulp.lpSum(costs[i][j] * x[(i, j)] for i in range(num_suppliers) for j in range(num_customers)), "Total Transportation Cost"

    # Restrições de fornecimento
    for i in range(num_suppliers):
        prob += pulp.lpSum(x[(i, j)] for j in range(num_customers)) <= supplies[i], f"Supply_Constraint_{supplier_names[i]}"

    # Restrições de demanda
    for j in range(num_customers):
        prob += pulp.lpSum(x[(i, j)] for i in range(num_suppliers)) >= demands[j], f"Demand_Constraint_{customer_names[j]}"

    # Resolver o problema
    prob.solve()

    # Obter resultados
    status = pulp.LpStatus[prob.status]
    total_cost = pulp.value(prob.objective)
    transported_quantities = np.zeros((num_suppliers, num_customers))
    for i in range(num_suppliers):
        for j in range(num_customers):
            transported_quantities[i][j] = x[(i, j)].varValue

    return {"status": status, "total_cost": total_cost, "transported_quantities": transported_quantities, "supplier_names": supplier_names, "customer_names": customer_names}

def plot_transportation_plan(result, filename="transportation_plan.png"):
    """
    Plota o plano de transporte e salva a imagem.
    """
    transported_quantities = result["transported_quantities"]
    supplier_names = result["supplier_names"]
    customer_names = result["customer_names"]
    total_cost = result["total_cost"]

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.imshow(transported_quantities, cmap='Blues', origin='upper')

    # Adicionar rótulos e valores
    for i in range(transported_quantities.shape[0]):
        for j in range(transported_quantities.shape[1]):
            text = ax.text(j, i, f"{transported_quantities[i, j]:.0f}",
                           ha="center", va="center", color="black", fontsize=10)

    # Configurar ticks e rótulos
    ax.set_xticks(np.arange(len(customer_names)))
    ax.set_yticks(np.arange(len(supplier_names)))
    ax.set_xticklabels(customer_names, rotation=45, ha="right")
    ax.set_yticklabels(supplier_names)

    ax.set_xlabel("Clientes")
    ax.set_ylabel("Fornecedores")
    ax.set_title(f"Plano de Transporte Otimizado\nCusto Total: {total_cost:.2f}")
    fig.tight_layout()
    plt.savefig(filename)
    plt.close(fig)

if __name__ == "__main__":
    # Exemplo de uso (dados de exemplo)
    costs_example = [
        [10, 15, 20],
        [12, 10, 18],
        [15, 13, 10]
    ]
    supplies_example = [100, 150, 80]  # Capacidade dos fornecedores
    demands_example = [70, 120, 140]  # Demanda dos clientes

    result_example = solve_transportation_problem(costs_example, supplies_example, demands_example)

    print(f"Status da Solução (Exemplo): {result_example['status']}")
    print(f"Custo Total de Transporte (Exemplo): {result_example['total_cost']}")
    print("Quantidades Transportadas (Exemplo):")
    for i in range(len(supplies_example)):
        for j in range(len(demands_example)):
            value = result_example['transported_quantities'][i][j]
            if value > 0:
                print(f"  Do Fornecedor {i+1} para o Cliente {j+1}: {value}")

    # Plotar o exemplo
    plot_transportation_plan(result_example, filename="example_transportation_plan.png")
    print("Plano de transporte de exemplo salvo como example_transportation_plan.png")

