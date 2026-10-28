import os
import requests
from flask import Flask

app = Flask(__name__)

# CONFIGURAÇÕES - Substitua com os seus dados reais do Telegram
TOKEN_TELEGRAM = "9011106722:AAE4bOZIO2XOnc7yFf9BJRYMVpaj3wvF6Wk"
ID_TELEGRAM = "9095363392"

def buscar_e_enviar_vagas():
    try:
        # Mensagem com links focados em Cambé e Londrina nas últimas 24h
        mensagem = (
            "💼 *Robô de Vagas: Novas Oportunidades!*\n"
            "📍 *Região:* Cambé e Londrina\n"
            "🎯 *Cargos:* Auxiliar Adm. / Assistente Adm. / Assistente Financeiro\n\n"
            "Clique nos links abaixo para conferir as vagas abertas hoje:\n\n"
            
            "🔹 *Vagas no INDEED:*\n"
            "🔗 [Ver vagas de hoje](https://indeed.com)\n\n"
            
            "🔹 *Vagas no LINKEDIN:*\n"
            "🔗 [Ver vagas de hoje](https://linkedin.com)\n\n"
            
            "🔹 *Vagas no GLASSDOOR:*\n"
            "🔗 [Ver vagas de hoje](https://glassdoor.com.br)\n\n"
            
            "📌 *Dica do Robô:* Acesse os links acima para ver as postagens mais recentes!"
        )
        
        url_telegram = f"https://telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
        dados = {
            "chat_id": ID_TELEGRAM,
            "text": mensagem,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True
        }
        requests.post(url_telegram, data=dados)
        return "Notificação enviada com sucesso!"
        
    except Exception as e:
        return f"Erro ao processar: {str(e)}"

@app.route('/')
def home():
    resultado = buscar_e_enviar_vagas()
    return f"Status do Robô: {resultado}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
