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
    
    # Processa a lista de usuários (ex: separados por quebra de linha)
    usuarios_input = request.form.get('usuarios', '')
    
    usuarios = []
    for linha in usuarios_input.strip().split('\n'):
        if linha.strip():
            partes = linha.split(';')
            if len(partes) >= 3:
                matricula = partes[0].strip()
                nome = partes[1].strip()
                info = partes[2].strip()
                usuarios.append({
                    'matricula': matricula,
                    'nome': nome,
                    'info': info
                })

    return render_template(
        'print_cards.html',
        logo_url=logo_url,
        titulo_cabecalho=titulo_cabecalho,
        usuarios=usuarios
    )

if __name__ == '__main__':
    # Define a porta 5003 e escuta em todas as interfaces para o container
    app.run(host='0.0.0.0', port=5003)