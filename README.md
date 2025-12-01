
---

# 🐳 SwarmDataHub — Final Project (Docker)

Este repositório contém um projeto final desenvolvido utilizando **Docker**, **Docker Compose** e conceitos de **containers**, com foco na criação, gerenciamento e orquestração de aplicações em ambientes isolados e portáveis.

## 👥 Equipe

* **Nicolas Antunes de Sousa Fé**
* **Francisco Eduardo de Vasconcelos Costa**
* **Carlos Eduardo Simão de Queiroz**

---

## 🎞️ Demonstração (GIF)

> Prévia da execução ou inicialização dos containers:

![Demonstração do Projeto](https://github.com/user-attachments/assets/8115d7d9-970b-4558-834b-d1d51112a0bf)

---

# 📌 Introdução ao Projeto

Este projeto foi desenvolvido para demonstrar, na prática, o uso de tecnologias modernas de containerização e orquestração. Ele envolve a construção e execução de serviços utilizando:

* **Docker**
* **Docker Containers**
* **Docker Images**
* **Docker Compose**
* **Docker Swarm**

A seguir está um resumo dos conceitos aplicados no projeto.

---

# 🧱 Conceitos Fundamentais Utilizados

## 🐳 **Docker**

Plataforma de código aberto que automatiza o *deployment* de aplicações dentro de **containers de software**.
Permite empacotar, distribuir e executar aplicações de maneira consistente em qualquer ambiente.

---

## 📦 **Containers Docker**

Unidades padronizadas de software que incluem:

* Código da aplicação
* Bibliotecas
* Dependências
* Configurações

Eles compartilham o **kernel do sistema operacional**, mas isolam seus processos e recursos.

Características:

* Leves
* Portáteis
* Consistentes entre ambientes
* Rápidos para iniciar e destruir

---

## 🧩 **Imagens Docker**

Templates que são usados para criar containers.

Uma imagem contém tudo que a aplicação precisa:

* Código
* Runtime
* Bibliotecas
* Dependências

As imagens podem ser armazenadas, versionadas, reutilizadas e compartilhadas em repositórios como Docker Hub ou GitHub Packages.

---

## 🧬 **Docker Compose**

Ferramenta usada para gerenciar aplicações **multi-container**.

Através de um arquivo **YAML (`docker-compose.yml`)**, você define:

* Serviços
* Redes
* Volumes
* Dependências
* Porta de acesso

Isso facilita a criação de ambientes completos com apenas um comando:

```bash
docker compose up -d
```

---

## 🌐 **Docker Swarm**

Ferramenta de **orquestração** nativa do Docker que permite:

* Criar clusters de múltiplas máquinas
* Distribuir containers entre os nós
* Escalar automaticamente a aplicação
* Gerenciar serviços de forma coordenada

Ele transforma vários hosts Docker em um **único cluster lógico**.

---

# 🚀 Como Executar o Projeto

### **1. Certifique-se de ter instalado:**

* Docker
* Docker Compose

### **2. No diretório do projeto, execute:**

```bash
docker compose up -d
```

### **3. Para parar os serviços:**

```bash
docker compose down
```

---

# 📂 Estrutura do Repositório

```
SwarmDataHub_-Final-project_Docker/
│
├── backend/          
├── frontend/         
├── db/               
├── docker-compose.yml
└── README.md
```

---

# 🐞 Problemas Conhecidos

* Busca sensível a maiúsculas/minúsculas
* Relações que podem permanecer após remoção de entidades
  (caso aplicável à lógica do projeto)

---

# 📌 Melhorias Futuras

* Implementar busca case-insensitive
* Adicionar monitoramento em tempo real
* Criar logs centralizados
* Melhorias na padronização das imagens e build

---

# 🤝 Como Contribuir

1. Faça um fork
2. Crie um branch (`feature/nova-feature`)
3. Envie um Pull Request

---

🔹 Criar um banner para colocar no topo
🔹 Criar um GIF mais bonito (mais suave, com animação moderna)
🔹 Gerar badges de linguagens, Docker, versão, etc.

Quer alguma dessas melhorias?
