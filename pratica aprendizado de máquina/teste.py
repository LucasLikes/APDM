import pandas as pd
import pickle

def enviar_dados_teste(entrada_usuario):
    try:
        # Carregar o modelo treinado
        with open('modelos/modelo.pkl', 'rb') as arquivo:
            modelo = pickle.load(arquivo)

        # Criar um DataFrame a partir dos dados de entrada do usuário
        entrada_df = pd.DataFrame([entrada_usuario])

        # Realizar a previsão com o modelo treinado
        resultado = modelo.predict(entrada_df)

        # Definir um limiar de decisão
        limiar = 0.56

        # Verificar o resultado e retornar a mensagem apropriada
        if resultado > limiar:
            return "Reação a Diabetes Positivo"
        else:
            return "Reação a Diabetes Negativo"
    except Exception as e:
        return f"Erro ao processar a previsão: {e}"

# Exemplo de utilização da função enviar_dados_teste:
if __name__ == "__main__":
    entrada_usuario = {
        'Glucose': 143,
        'BloodPressure': 75,
        'BMI': 211,
        'Age': 52,
        # Adicione mais features conforme necessário
    }
    resultado_previsao = enviar_dados_teste(entrada_usuario)
    print(resultado_previsao)
