
from src.data_generator import generate_supply_chain_data
from src.supply_chain_optimizer import solve_transportation_problem, plot_transportation_plan
import os

def run_optimization_scenario(num_suppliers, num_customers, output_dir="output"):
    """
    Executa um cenário completo de otimização da cadeia de suprimentos:
    gera dados, resolve o problema e plota o resultado.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"\n--- Cenário com {num_suppliers} Fornecedores e {num_customers} Clientes ---")
    costs, supplies, demands, supplier_names, customer_names = generate_supply_chain_data(num_suppliers, num_customers)

    print("Dados Gerados:")
    print("  Custos:", costs)
    print("  Suprimentos:", supplies)
    print("  Demandas:", demands)

    result = solve_transportation_problem(costs, supplies, demands, supplier_names, customer_names)

    print(f'Status da Solução: {result["status"]}')
    print(f'Custo Total de Transporte: {result["total_cost"]:.2f}')
    print("Quantidades Transportadas:")
    for i in range(len(supplier_names)):
        for j in range(len(customer_names)):
            value = result["transported_quantities"][i][j]
            if value > 0:
                print(f'  De {supplier_names[i]} para {customer_names[j]}: {value:.0f}')

    plot_filename = os.path.join(output_dir, f'transportation_plan_{num_suppliers}s_{num_customers}c.png')
    plot_transportation_plan(result, filename=plot_filename)
    print(f'Plano de transporte salvo como {plot_filename}')

if __name__ == "__main__":
    # Cenário 1: Pequeno
    run_optimization_scenario(num_suppliers=3, num_customers=3)

    # Cenário 2: Médio
    run_optimization_scenario(num_suppliers=5, num_customers=4)

    # Cenário 3: Grande
    run_optimization_scenario(num_suppliers=7, num_customers=6)

