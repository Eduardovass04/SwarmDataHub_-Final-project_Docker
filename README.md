
---

# 🐋 SwarmDataHub — Final Project (Docker)

Repositório destinado ao projeto **SwarmDataHub**, uma solução containerizada usando **Docker** 

## 👥 **Equipe**

* **Nicolas Antunes de Sousa Fé**
* **Francisco Eduardo de Vasconcelos Costa**
* **Carlos Eduardo Simão de Queiroz**

---

## 🎞️ Demonstração

![Demonstração do SwarmDataHub](https://github.com/user-attachments/assets/8115d7d9-970b-4558-834b-d1d51112a0bf)

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

* **Backend API** — lógica de negócio e rotas
* **Banco de Dados** — persistência dos dados coletados
* **Frontend/Visualization** — interface para análise dos dados

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

Para parar os containers:

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

* Após remover uma abelha, o sensor pode continuar associado a ela
* A busca por nome **é sensível a maiúsculas/minúsculas**, ou seja:

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

Se quiser, posso também:

✨ Criar um **banner gráfico** para o topo
✨ Criar **badges** (Docker, Python, status, versão)
✨ Gerar um GIF mais sofisticado (animado em loop suave, com efeitos)

Só pedir!
