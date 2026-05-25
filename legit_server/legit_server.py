from flask import Flask, render_template_string, make_response, redirect, url_for

app = Flask(__name__)

# Variable globale pour piloter la sécurité depuis la GUI
security_status = {"active": False}

GUI_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Contrôle Sécurité Réseau</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; background: #fafafa; }
        .box { padding: 30px; margin: 20px auto; border-radius: 8px; display: inline-block; width: 400px; }
        .vulnerable { background: #ffebeb; color: #b91c1c; border: 2px dashed #fca5a5; }
        .secure { background: #ecfdf5; color: #047857; border: 2px solid #34d399; }
        .btn { padding: 12px 24px; font-size: 16px; font-weight: bold; cursor: pointer; border: none; border-radius: 4px; color: white; }
        .btn-toggle { background: #2563eb; }
    </style>
</head>
<body>
    <h1>Console d'Administration du Réseau</h1>
    
    <div class="box {{ 'secure' if status.active else 'vulnerable' }}">
        <h2>Configuration Actuelle :</h2>
        <p><b>Wi-Fi :</b> {{ 'Protégé (WPA2/WPA3)' if status.active else 'Réseau Ouvert (Pas de clé)' }}</p>
        <p><b>Flux Web :</b> {{ 'HTTPS Forcé (HSTS Actif)' if status.active else 'HTTP Simple (Non chiffré)' }}</p>
    </div>

    <form action="/toggle" method="post">
        <button type="submit" class="btn btn-toggle">
            👉 Passer en mode {{ 'VULNÉRABLE' if status.active else 'SÉCURISÉ' }}
        </button>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    response = make_response(render_template_string(GUI_TEMPLATE, status=security_status))
    if security_status["active"]:
        # On injecte la contre-mesure HSTS directement dans les en-têtes HTTP
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/toggle', methods=['POST'])
def toggle():
    security_status["active"] = not security_status["active"]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)