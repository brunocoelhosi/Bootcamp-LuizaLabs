# 🏦 Sistema Bancário em Python

Um sistema bancário simples desenvolvido em **Python**, utilizando:

- `@dataclass`
- Funções **positional-only** (`/`)
- Funções **keyword-only** (`*`)
- Armazenamento de dados em dicionários
- Estrutura de **Usuários** e **Contas Correntes**
- Associação conta → usuário via CPF

Este projeto simula parte do funcionamento de um banco: cadastro de clientes, criação de contas e listagem das contas existentes.

---

## 📌 Funcionalidades

### ✅ Cadastro de Usuário

- Nome
- Data de nascimento
- CPF
- Endereço completo

O CPF é utilizado como chave única.

---

### ✅ Abertura de Conta Corrente

- Número da conta
- Agência (padrão: `0001`)
- Relacionada a um CPF existente

Caso o usuário não exista, a conta não é criada.

---

### ✅ Listagem de Contas

Mostra:

- Agência
- Número da conta
- CPF do titular
- Nome do cliente (buscado automaticamente na lista de usuários)

---

## 🧱 Estrutura de Dados

### 📌 `Usuario`

```python
@dataclass
class Usuario:
    nome: str
    nasc: str
    cpf: int
    endereco: str
```

### 📌 `Conta`

```python
@dataclass
class Conta:
    agencia: str = "0001"
    numero: int = 0
    cpf: int = 0
```

📜 Licença

Este projeto é de uso livre para fins educacionais.
