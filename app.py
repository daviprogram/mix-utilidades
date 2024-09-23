from flask import Flask, render_template

app = Flask(__name__)

# Produtos fictícios
produtos = [
    {
        'nome': 'Arroz 5kg',
        'preco': 25.90,
        'imagem': 'images/arroz.png'  # Somente o caminho relativo a 'static'
    },
    {
        'nome': 'Feijão 1kg',
        'preco': 8.50,
        'imagem': 'images/feijao.png'
    },
    {
        'nome': 'Macarrão 500g',
        'preco': 4.30,
        'imagem': 'images/macarrao.png'
    },
    {
        'nome': 'Azeite 500ml',
        'preco': 15.90,
        'imagem': 'images/azeite.png'
    }
]

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
