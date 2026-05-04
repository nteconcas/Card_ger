import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuração para upload de arquivos (se precisar salvar logos no servidor)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    # Coleta os dados do formulário principal
    logo_url = request.form.get('logo_url', '')
    titulo_cabecalho = request.form.get('titulo_cabecalho', 'CARTÃO DE ACESSO')
    
    # Processa o arquivo Excel
    arquivo = request.files.get('planilha')
    usuarios = []
    
    if arquivo and arquivo.filename.endswith(('.xlsx', '.xls')):
        try:
            import pandas as pd
            df = pd.read_excel(arquivo)
            for _, row in df.iterrows():
                if len(row) >= 3:
                    usuarios.append({
                        'matricula': str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else '',
                        'nome': str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else '',
                        'info': str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else ''
                    })
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")

    return render_template(
        'print_cards.html',
        logo_url=logo_url,
        titulo_cabecalho=titulo_cabecalho,
        usuarios=usuarios
    )

if __name__ == '__main__':
    # Define a porta 5003 e escuta em todas as interfaces para o container
    app.run(host='0.0.0.0', port=5003)