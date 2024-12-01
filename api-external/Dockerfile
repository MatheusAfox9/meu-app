# Usar a imagem base do Python 3.9 slim
FROM python:3.9-slim

# Setar o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt para o container
COPY requirements.txt .

# Instalar as dependências (incluindo o Gunicorn)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o container
COPY . .

# Definir a porta em que a API Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação Flask usando o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Instalar dependências necessárias
RUN pip install --no-cache-dir Flask psycopg2-binary
