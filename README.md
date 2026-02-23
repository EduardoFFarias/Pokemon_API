# 🐱‍👤 Pokémon API — Análise e Visualização de Dados

Projeto desenvolvido para consumo de dados da **PokéAPI**, tratamento das informações em **Python** e criação de análises visuais no **Power BI**.

**LINK PROJETO:** https://app.powerbi.com/view?r=eyJrIjoiYWQxZjA3ZDgtMzU3Yi00ODI3LTllMGMtNmJhODlmMDQ5M2I1IiwidCI6IjM4ZjZhMDc3LTMzM2QtNGUwZS1iODk0LTM1NmRiMTI5YmQ5OCJ9

O foco do projeto é praticar o fluxo completo de dados (**ETL**), desde a extração via API até a visualização e interpretação dos dados.

---

## 🎯 Objetivo

- Consumir dados da **PokéAPI**
- Estruturar e tratar dados em formato JSON
- Criar análises e dashboards interativos
- Consolidar conhecimentos em **APIs, Python e Power BI**

---

## 🛠️ Tecnologias Utilizadas

- **Python**
  - `requests`
  - `pandas`
  - `json`
- **API**
  - [PokéAPI](https://pokeapi.co/)
- **Power BI**
- **Git & GitHub**

---

## 🔄 Fluxo de Dados (ETL)

### 1️⃣ Extração
- Consumo da PokéAPI via requisições HTTP
- Coleta de informações como:
  - Nome do Pokémon
  - Tipo(s)
  - Atributos base (HP, Attack, Defense, etc.)

### 2️⃣ Transformação
- Normalização de dados JSON
- Tratamento de listas e objetos aninhados
- Padronização e limpeza das colunas
- Criação de campos auxiliares para análise

### 3️⃣ Carga
- Exportação dos dados tratados para:
  - CSV
- Importação no Power BI

### 4️⃣ Visualização
- Dashboards interativos
- Comparação entre Pokémons
- Análises por tipo
- Filtros e métricas dinâmicas

---

## 📊 Análises Desenvolvidas

- Quantidade de Pokémons por tipo
- Média de atributos por tipo
- Ranking de Pokémons por status
- Comparação individual de Pokémons
- Distribuição de atributos base

---

## 📁 Estrutura do Projeto

```bash
pokemon-api-project/
│
├── data/
│   ├── pokemons.csv
│
│
├── scripts/
│   └── pokemon_api.py
│
├── powerbi/
│   └── dashboard_pokemon.pbix
│
└── README.md
