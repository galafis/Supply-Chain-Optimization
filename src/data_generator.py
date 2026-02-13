import numpy as np

def generate_supply_chain_data(num_suppliers, num_customers, seed=42):
    """
    Gera dados sintéticos para um problema de otimização da cadeia de suprimentos.

    Args:
        num_suppliers (int): Número de fornecedores.
        num_customers (int): Número de clientes.
        seed (int): Semente para reprodutibilidade.

    Returns:
        tuple: Um tuple contendo (costs, supplies, demands, supplier_names, customer_names).
    """
    np.random.seed(seed)

    # Gerar custos de transporte
    costs = np.random.randint(5, 50, size=(num_suppliers, num_customers)).tolist()

    # Gerar capacidades de fornecimento
    supplies = np.random.randint(50, 200, size=num_suppliers).tolist()

    # Gerar demandas dos clientes
    demands = np.random.randint(30, 100, size=num_customers).tolist()

    # Garantir que a oferta total seja maior ou igual à demanda total
    total_supply = sum(supplies)
    total_demand = sum(demands)
    if total_supply < total_demand:
        # Ajustar suprimentos para cobrir a demanda
        diff = total_demand - total_supply
        supplies[np.argmax(supplies)] += diff
        total_supply = sum(supplies) # Recalcular para garantir

    supplier_names = [f"Fornecedor_{i+1}" for i in range(num_suppliers)]
    customer_names = [f"Cliente_{j+1}" for j in range(num_customers)]

    return costs, supplies, demands, supplier_names, customer_names

if __name__ == "__main__":
    num_suppliers = 3
    num_customers = 4
    costs, supplies, demands, supplier_names, customer_names = generate_supply_chain_data(num_suppliers, num_customers)

    print("Custos:")
    for i, s_name in enumerate(supplier_names):
        for j, c_name in enumerate(customer_names):
            print(f"  {s_name} para {c_name}: {costs[i][j]}")

    print("\nSuprimentos:")
    for i, s_name in enumerate(supplier_names):
        print(f"  {s_name}: {supplies[i]}")

    print("\nDemandas:")
    for j, c_name in enumerate(customer_names):
        print(f"  {c_name}: {demands[j]}")

    print(f"\nTotal Suprimento: {sum(supplies)}")
    print(f"Total Demanda: {sum(demands)}")

