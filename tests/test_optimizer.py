import unittest
from src.supply_chain_optimizer import solve_transportation_problem
from src.data_generator import generate_supply_chain_data

class TestSupplyChainOptimizer(unittest.TestCase):

    def test_solve_transportation_problem_optimal(self):
        # Cenário simples com solução ótima esperada
        costs = [
            [10, 20],
            [5, 15]
        ]
        supplies = [100, 100]
        demands = [50, 50]

        result = solve_transportation_problem(costs, supplies, demands)
        self.assertEqual(result["status"], "Optimal")
        self.assertAlmostEqual(result["total_cost"], 1000.0)
        self.assertAlmostEqual(result["transported_quantities"][0][0], 0.0)
        self.assertAlmostEqual(result["transported_quantities"][0][1], 0.0)
        self.assertAlmostEqual(result["transported_quantities"][1][0], 50.0)
        self.assertAlmostEqual(result["transported_quantities"][1][1], 50.0)

    def test_solve_transportation_problem_unbalanced_supply_greater(self):
        # Cenário com mais oferta do que demanda
        costs = [
            [10, 20],
            [5, 15]
        ]
        supplies = [100, 100]
        demands = [30, 30]

        result = solve_transportation_problem(costs, supplies, demands)
        self.assertEqual(result["status"], "Optimal")
        self.assertAlmostEqual(result["total_cost"], 600.0)
        self.assertAlmostEqual(result["transported_quantities"][0][0], 0.0)
        self.assertAlmostEqual(result["transported_quantities"][0][1], 0.0)
        self.assertAlmostEqual(result["transported_quantities"][1][0], 30.0)
        self.assertAlmostEqual(result["transported_quantities"][1][1], 30.0)

    def test_solve_transportation_problem_unbalanced_demand_greater(self):
        # Cenário com mais demanda do que oferta
        costs = [
            [10, 20],
            [5, 15]
        ]
        supplies_adjusted = [70, 70]
        demands = [70, 70]

        result = solve_transportation_problem(costs, supplies_adjusted, demands)
        self.assertEqual(result["status"], "Optimal")
        self.assertAlmostEqual(result["total_cost"], 1750.0)
        self.assertAlmostEqual(result["transported_quantities"][0][0], 70.0)
        self.assertAlmostEqual(result["transported_quantities"][0][1], 0.0)
        self.assertAlmostEqual(result["transported_quantities"][1][0], 0.0)
        self.assertAlmostEqual(result["transported_quantities"][1][1], 70.0)

    def test_data_generator_balance(self):
        # Testa se o gerador de dados garante que a oferta total >= demanda total
        num_suppliers = 2
        num_customers = 2
        costs, supplies, demands, _, _ = generate_supply_chain_data(num_suppliers, num_customers)
        self.assertGreaterEqual(sum(supplies), sum(demands))

    def test_solve_transportation_problem_with_generated_data(self):
        # Testa o solver com dados gerados
        num_suppliers = 3
        num_customers = 3
        costs, supplies, demands, supplier_names, customer_names = generate_supply_chain_data(num_suppliers, num_customers)
        result = solve_transportation_problem(costs, supplies, demands, supplier_names, customer_names)
        self.assertEqual(result["status"], "Optimal")
        self.assertGreater(result["total_cost"], 0)

if __name__ == '__main__':
    unittest.main()
