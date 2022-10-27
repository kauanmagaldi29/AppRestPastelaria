from flask import Blueprint, render_template, request
import requests

bp_cliente = Blueprint(
    'cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' endereços do endpoint '''
urlApiCliente = "http://localhost:8000/cliente/"
urlApiCliente = "http://localhost:8000/cliente/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas '''
@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    response = requests.get(urlApiCliente, headers=headers)
    result = response.json()
    return render_template('formListaCliente.html', result=result)

@bp_cliente.route('/form-Cliente/', methods=['POST'])
def formCliente(): 
    return render_template('formCliente.html')  