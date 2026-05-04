# Usa uma imagem oficial do Python slim
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código restante para o container
COPY . .

# Expõe a porta 5003 (interna do container)
EXPOSE 5003

# Executa o aplicativo
CMD ["python", "app.py"]