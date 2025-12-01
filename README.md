# SwarmDataHub_Final-project_Docker


# 🐝 SwarmDataHub — Final Project (Docker)

Repositório destinado ao projeto **SwarmDataHub**, uma solução containerizada usando **Docker** para monitoramento, armazenamento e visualização de dados relacionados a colmeias e sensores ambientais.

## 👥 **Equipe**

* **Nicolas Antunes**
* **Francisco Eduardo**
* **Carlos Eduardo**

---

## 🎞️ Demonstração (GIF)

> 🔽 **Coloque aqui o GIF demonstrando a execução da ferramenta ou do painel:**

```md
![Demonstração do SwarmDataHub][swarmdatahub_demo](https://github.com/user-attachments/assets/8115d7d9-970b-4558-834b-d1d51112a0bf)

```

Caso queira, posso criar um GIF estilizado com animação da arquitetura, cards, sensores ou animação simulada do dashboard.

---

## 📌 **Descrição do Projeto**

O **SwarmDataHub** tem como objetivo centralizar, processar e exibir dados provenientes de sensores de abelhas e colmeias, garantindo facilidade de implantação através do uso de containers Docker.

O projeto permite:

* Execução com **Docker Compose**
* Separação clara entre serviços:

  * Backend
  * Banco de dados
  * Interface de visualização
* Portabilidade total do ambiente com apenas um comando

---

## 🏗️ **Arquitetura**

A solução é composta por múltiplos serviços Docker que trabalham juntos:

* **Backend API** — lógica de negócio e rotas.
* **Banco de Dados** — persistência dos dados coletados.
* **Frontend/Visualization** — interface para análise dos dados.

Tudo isso orquestrado pelo **docker-compose.yml**.

---

## 🚀 **Como Executar o Projeto**

### 🔧 Requisitos

* **Docker** instalado
* **Docker Compose** instalado

### ▶️ Rodando

```bash
docker compose up -d
```

Parando os containers:

```bash
docker compose down
```

---

## 📂 **Estrutura do Repositório**

```
SwarmDataHub_-Final-project_Docker/
│
├── backend/          # Código-fonte da API
├── frontend/         # Interface de visualização
├── db/               # Scripts e configs do banco
├── docker-compose.yml
└── README.md
```

---

## 🐞 **Problemas Conhecidos**

* Após remover uma abelha, o sensor pode continuar associado a ela.
* A busca por nome **é sensível a maiúsculas/minúsculas**

  * “abelha” ≠ “Abelha” ≠ “ABELHA”

---

## 📌 **Melhorias Futuras**

* Busca case-insensitive
* Dashboard em tempo real
* Logs centralizados
* Validação mais robusta na API

---

## 🤝 Contribuição

1. Faça um fork
2. Crie um branch (`feature/nova-feature`)
3. Envie um Pull Request

---

## 📜 Licença

Projeto acadêmico desenvolvido pela equipe mencionada acima.

---


