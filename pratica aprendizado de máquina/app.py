from flask import Flask, render_template, request
import pandas as pd
import teste

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Obter dados do formulário
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        bmi = float(request.form['bmi'])
        age = float(request.form['age'])
        
        # Realizar a previsão com o modelo treinado
        entrada_usuario = {
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'BMI': bmi,
            'Age': age
        }
        resultado = teste.enviar_dados_teste(entrada_usuario)
        
        # Retornar a mensagem apropriada com base na previsão do modelo
        if resultado == "Reação a Diabetes Positivo":
            return 'Reação a Diabetes Positivo'
        else:
            return 'Reação a Diabetes Negativo'

if __name__ == '__main__':
    app.run(debug=True)
