# Etapa 1: Imagem Base do Node.js
FROM node:14-alpine

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o package.json e o package-lock.json para o container
COPY package.json package-lock.json ./

# Instalar as dependências
RUN npm install

# Copiar o restante do código da aplicação para o container
COPY . .

# Expor a porta em que o Express está rodando
EXPOSE 3000

# Comando para iniciar o servidor
CMD ["node", "server.js"]
