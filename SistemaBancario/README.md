# 🏦 Sistema Bancário em Python

Um sistema bancário simples desenvolvido em **Python**, utilizando:

- `@dataclass` para definir classes de dados
- Herança e classes abstratas (`ABC`)
- Armazenamento de dados em listas e dicionários
- Estrutura de **Clientes**, **Contas** e **Transações**
- Histórico de transações para cada conta
- Associação conta → cliente via CPF

Este projeto simula o funcionamento básico de um banco: cadastro de clientes, criação de contas correntes, depósitos, saques, exibição de extrato e listagem de contas.

---

## 📌 Funcionalidades

### ✅ Cadastro de Cliente (Pessoa Física)

- Nome
- Data de nascimento
- CPF (chave única)
- Endereço completo

### ✅ Criação de Conta Corrente

- Número da conta (auto-incrementado)
- Agência (padrão: `0001`)
- Limite de saque (R$ 500,00)
- Limite de saques por dia (3)
- Relacionada a um CPF existente

Caso o cliente não exista, a conta não é criada.

### ✅ Depósito

- Permite depositar valores positivos em uma conta existente.
- Registra a transação no histórico.

### ✅ Saque

- Permite sacar valores positivos, respeitando saldo, limite e limite de saques diários.
- Registra a transação no histórico.

### ✅ Extrato

- Exibe todas as transações realizadas (depósitos e saques).
- Mostra o saldo atual.

### ✅ Listagem de Contas

Mostra:

- Agência
- Número da conta
- Nome do titular

---

## 🚀 Como Executar

1. Certifique-se de ter Python instalado (versão 3.8+).
2. Execute o arquivo desafio.py:
3. Siga o menu interativo para realizar operações.
