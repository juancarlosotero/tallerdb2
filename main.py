from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

list = [
    {
        'id': 0,
        'company': 'Google',
        'service': 'Cloud CDN',
        'detail': 'Red de distribucion para publicar contenido web y de video.',
        'price': '175.00'
    },
    {
        'id': 1,
        'company': 'Amazon Web Services AWS',
        'service': 'Amazon EC2',
        'detail': 'Servicio web que proporciona una capacidad informatica segura y redimensionable en la nube.',
        'price': '71.84'
    },
    {
        'id': 2,
        'company': 'Microsoft Azure',
        'service': 'Virtual Machine',
        'detail': 'Maquinas virtuales basicas a precios economicos para desarrollo y pruebas',
        'price': '152.62'
    },
    {
        'id': 3,
        'company': 'Alibaba Cloud',
        'service': 'Cloud CDN',
        'detail': 'Servicio de entrega de contenido escalable y de alto rendimiento',
        'price': '93.52'
    }



]

@app.route('/', methods=['GET'])
def home():
    return "<center><h1>Taller2 - Creacion de API</h1></center>"

@app.route('/api/v1/empresa', methods=['GET'])
def service():
    return jsonify(list)


if __name__ == '__main__':
    app.run()
