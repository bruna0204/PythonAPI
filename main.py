from flask_pydantic_spec import FlaskPydanticSpec
from flask import Flask, jsonify
import datetime

app = Flask(__name__)
spec = FlaskPydanticSpec('flask',
                          title='First API - SENAI',
                          version='1.0.0',)
spec.register(app)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/datas/<data>', methods=['GET'])
def presente_futuro(data):
    # Converter a string da data para formato datetime
    """
     API para calcular a diferença entre duas datas

     ## Endpoint
     GET /datas/<data>

     ##Parãmetros
     data: **Data no formato "d-m-y"** (exemplo: 15-03-2023)
     -**Qualque outro formulario resultara em erro**


     ### Resposta (JSON):
     '''json
    {
    "Situação": passado
    "dias_diferenca": 5
    "diferenca_meses": 0
    "diferenca_ano": 0
    }
    '''
    ## Erros possiveis:
    - Se data não estiver no formato "d-m-y", retorna erro 400 Bad Request**:
    """
    tempo_atual = datetime.datetime.now()
    data_informada = datetime.datetime.strptime(data, '%d-%m-%Y')
    if tempo_atual < data_informada:
        resultado = 'Futuro'
    else:
        resultado = 'Passado'

    diferenca_data = (data_informada - tempo_atual).days
    meses = data_informada.month - tempo_atual.month
    diferenca_ano =  data_informada.year - tempo_atual.year
    anos_mes = diferenca_ano * 12
    diferenca_mes = anos_mes + meses
    return jsonify ({"Situacao": resultado,
                     "dias_diferenca": diferenca_data,
                     "diferenca_meses": diferenca_mes,
                     "diferenca_ano": diferenca_ano})


@app.route('/dias_de_diferenca/<data>')
def difere(data):
    data_informada = datetime.datetime.strptime(data,'%d-%m-%Y')
    tempo_atual = datetime.datetime.now()
    diferenca_data = (tempo_atual - data_informada).days
    return jsonify({"dias_difereca": diferenca_data})



if __name__ == '__main__':
    app.run(debug=True) #presisa desabilitar ele quando subir pra internet