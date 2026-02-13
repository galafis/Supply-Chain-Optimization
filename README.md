# Supply Chain Optimization

[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg)](https://www.python.org/)
[![PuLP](https://img.shields.io/badge/PuLP-2.7-blue.svg)](https://coin-or.github.io/pulp/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-013243.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-11557C.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Portugues](#portugues) | [English](#english)

---

## Portugues

### Visao Geral

Ferramenta de otimizacao de cadeia de suprimentos que resolve o problema de transporte usando programacao linear. Dado um conjunto de fornecedores (com capacidades), clientes (com demandas) e custos de transporte, encontra a alocacao de menor custo total.

### Arquitetura

```mermaid
graph LR
    A[Gerador de Dados<br>custos, oferta e demanda aleatorios] --> B[Solver PuLP<br>problema de transporte LP]
    B --> C[Matriz de Alocacao Otima]
    C --> D[Heatmap Matplotlib]
```

### Como Funciona

1. **Geracao de dados** (`src/data_generator.py`): Gera custos de transporte, capacidades de fornecimento e demandas aleatorias usando NumPy
2. **Otimizacao** (`src/supply_chain_optimizer.py`): Formula e resolve o problema de transporte como programacao linear usando PuLP (minimiza custo total respeitando restricoes de oferta e demanda)
3. **Visualizacao** (`main.py`): Executa cenarios e gera heatmaps das alocacoes otimas com Matplotlib

### Como Usar

```bash
# Clonar o repositorio
git clone https://github.com/galafis/Supply-Chain-Optimization.git
cd Supply-Chain-Optimization

# Criar ambiente virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Executar
python main.py
```

### Testes

```bash
pytest tests/test_optimizer.py -v
```

### Estrutura do Projeto

```
Supply-Chain-Optimization/
├── src/
│   ├── __init__.py
│   ├── data_generator.py        # Geracao de dados sinteticos
│   └── supply_chain_optimizer.py # Solver LP + visualizacao
├── tests/
│   ├── __init__.py
│   └── test_optimizer.py        # Testes unitarios
├── main.py                      # Ponto de entrada
├── requirements.txt
├── LICENSE
└── README.md
```

### Stack Tecnologica

| Tecnologia | Uso |
|------------|-----|
| **Python** | Linguagem principal |
| **PuLP** | Solver de programacao linear |
| **NumPy** | Geracao de dados numericos |
| **Matplotlib** | Visualizacao (heatmap) |

### Autor

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-demetrios-lafis)

### Licenca

Licenciado sob a Licenca MIT - veja [LICENSE](LICENSE) para detalhes.

---

## English

### Overview

Supply chain optimization tool that solves the transportation problem using linear programming. Given a set of suppliers (with capacities), customers (with demands), and transportation costs, it finds the minimum total cost allocation.

### Architecture

```mermaid
graph LR
    A[Data Generator<br>random costs, supply & demand] --> B[PuLP Solver<br>transportation LP problem]
    B --> C[Optimal Allocation Matrix]
    C --> D[Matplotlib Heatmap]
```

### How It Works

1. **Data generation** (`src/data_generator.py`): Generates random transportation costs, supply capacities, and demands using NumPy
2. **Optimization** (`src/supply_chain_optimizer.py`): Formulates and solves the transportation problem as linear programming using PuLP (minimizes total cost subject to supply and demand constraints)
3. **Visualization** (`main.py`): Runs scenarios and generates heatmaps of optimal allocations with Matplotlib

### Usage

```bash
# Clone the repository
git clone https://github.com/galafis/Supply-Chain-Optimization.git
cd Supply-Chain-Optimization

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run
python main.py
```

### Tests

```bash
pytest tests/test_optimizer.py -v
```

### Project Structure

```
Supply-Chain-Optimization/
├── src/
│   ├── __init__.py
│   ├── data_generator.py        # Synthetic data generation
│   └── supply_chain_optimizer.py # LP solver + visualization
├── tests/
│   ├── __init__.py
│   └── test_optimizer.py        # Unit tests
├── main.py                      # Entry point
├── requirements.txt
├── LICENSE
└── README.md
```

### Tech Stack

| Technology | Usage |
|------------|-------|
| **Python** | Core language |
| **PuLP** | Linear programming solver |
| **NumPy** | Numerical data generation |
| **Matplotlib** | Visualization (heatmap) |

### Author

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-demetrios-lafis)

### License

Licensed under the MIT License - see [LICENSE](LICENSE) for details.
