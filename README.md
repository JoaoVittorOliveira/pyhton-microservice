# 🐍 Projeto Microservice Python

Este projeto demonstra a arquitetura de **microserviços** utilizando Python com o framework **Flask** e conteinerização com **Docker** e **Docker Compose**.

## 🧠 O que são Microserviços?

Microserviços são uma abordagem de arquitetura de software na qual uma aplicação é estruturada como um conjunto de serviços pequenos e independentes, cada um responsável por uma funcionalidade específica. Esses serviços se comunicam entre si geralmente por meio de APIs HTTP ou mensageria.

### ✅ Vantagens:
- Maior escalabilidade
- Desacoplamento entre os serviços
- Facilidade de manutenção e atualização
- Distribuição entre diferentes times ou tecnologias

### 🚫 Desvantagens dos Microserviços:
- Complexidade no gerenciamento: Manter múltiplos serviços, cada um com seu ciclo de vida, exige mais ferramentas e organização.
- Dificuldade na comunicação
- Desafio em testes
- Deploy mais complexo
- Gerenciamento de dados: Cada microserviço deve ter seu próprio banco de dados, o que dificulta transações distribuídas e exige técnicas como eventual consistency.
- Sobrecarga operacional

### 🚀 Aplicação no Projeto

Neste projeto, implementamos dois microserviços simples, cada um com sua responsabilidade:

- **Service 1**: Responsável pela autenticação de usuários (login).
- **Service 2**: Responsável por fornecer dados simulados.

Cada serviço é isolado em seu próprio container Docker, o que permite desenvolvimento, teste e deploy de forma independente.

## 📂 Estrutura do Projeto

```
microservice_python/ 
│
├── service1/               # Serviço de autenticação (login)
│   ├── app.py              # Código principal do serviço
│   ├── requirements.txt    # Dependências Python
│   └── Dockerfile          # Dockerfile para criação da imagem
│
├── service2/               # Serviço de dados
│   ├── app.py              # Código principal do serviço
│   ├── requirements.txt    # Dependências Python
│   └── Dockerfile          # Dockerfile para criação da imagem
│
└── docker-compose.yml      # Orquestração dos containers
```

## 🐳 docker-compose.yml

```yaml
services:
  service1:
    build: ./service1
    ports:
      - "5000:5000"

  service2:
    build: ./service2
    ports:
      - "5001:5000"
```

✅ Cada serviço é mapeado para uma porta da máquina local:
- **service1:** http://localhost:5000
- **service2:** http://localhost:5001

## 🔥 Funcionalidades dos Serviços

### 🔐 Service 1 - Login
- **Endpoint:** `/login`
- **Métodos:**
  - **POST:** Realiza a autenticação (simulada).
  - **GET:** Retorna uma mensagem informando que aceita apenas POST.

### 📊 Service 2 - Dados
- **Endpoint:** `/data`
- **Método:** 
  - **GET:** Retorna uma mensagem com dados simulados (porta, valor e status).

## 🛠️ Como executar o projeto

### 1️⃣ Pré-requisitos:
- Docker instalado [Docker](https://www.docker.com/)
- Docker Compose instalado

### 2️⃣ Comandos para rodar:

No terminal, na raiz do projeto, execute:

```bash
docker-compose up --build
```

### 3️⃣ Teste os serviços:

- **Service 1 (Login):**
  - Acesse: [http://localhost:5000/login](http://localhost:5000/login)
  - Método GET: Retorna que aceita apenas POST
  - Método POST: Retorna mensagem de sucesso na autenticação

- **Service 2 (Dados):**
  - Acesse: [http://localhost:5001/data](http://localhost:5001/data)
  - Método GET: Retorna os dados simulados

## 📌 Conclusões
- Esse projeto é um exemplo didático para demonstrar a arquitetura de microserviços com Python, Flask e Docker.
- Pode ser expandido facilmente adicionando banco de dados, autenticação real, comunicação entre serviços, APIs externas, etc.
- Serviu de forma de aprendizado para matéria de engenharia de software 2 - UNITINS
