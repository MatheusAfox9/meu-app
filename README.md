# Aplicação Multi-Camadas Containerizada

Este projeto demonstra uma aplicação utilizando **Docker**, com arquitetura multi-camadas (frontend, backend, banco de dados e API externa). A aplicação foi projetada para demonstrar a comunicação entre diferentes componentes e a persistência de dados, além de integrar a API externa e implementar um sistema de autenticação com JWT.

## Estrutura do Projeto

O projeto é composto pelos seguintes serviços:

1. **Frontend**: Interface de usuário desenvolvida com React e servida via Nginx.
2. **Backend**: API RESTful em Node.js com Express, responsável por gerenciar as operações de CRUD.
3. **API Externa**: API simulada em Flask para fornecer dados fictícios.
4. **Banco de Dados**: PostgreSQL para persistência de dados, com inicialização automática.

## Como Rodar o Projeto

### Pré-requisitos

- Docker
- Docker Compose

### Passos para rodar

1. Clone o repositório:

   ```bash
   git clone https://github.com/usuario/meu-projeto.git
   cd meu-projeto
