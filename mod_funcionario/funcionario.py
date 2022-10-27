from flask import Blueprint, render_template, request
import requests

bp_funcionario = Blueprint(
    'funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' endereços do endpoint '''
urlApiFuncionarios = "http://localhost:8000/funcionario/"
urlApiFuncionario = "http://localhost:8000/funcionario/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas '''
@bp_funcionario.route('/', methods=['GET', 'POST'])
def formListaFuncionario():
    response = requests.get(urlApiFuncionarios, headers=headers)
    result = response.json()
    return render_template('formListaFuncionario.html', result=result)

@bp_funcionario.route('/form-funcionario/', methods=['POST'])
def formFuncionario(): 
    return render_template('formFuncionario.html')  