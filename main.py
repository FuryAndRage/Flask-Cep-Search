from flask import Flask, request, render_template, request
import requests

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def home():
	if request.method == 'POST':
		cep = request.form.get('cep')
		url = f'https://viacep.com.br/ws/{cep}/json/'
		try:
			req = requests.get(url)
			res = req.json()
			return render_template('index.html', res = res)
		except:
			return render_template('index.html', erro = 'CEP nao encontrado')
	return render_template('index.html')

if __name__ == '__main__':
	app.run()