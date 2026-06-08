from flask import Flask, render_template_string, make_response, redirect, url_for

app = Flask(__name__)

# État de la sécurité Web pour la démonstration
network_status = {
    "is_secure": False  # Commencer en mode vulnérable (Sans HSTS)
}

GUI_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Console d'Administration Réseau - Hôtel</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; text-align: center; padding: 40px; background: #f3f4f6; }
        .container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: inline-block; width: 480px; }
        .status-box { padding: 20px; margin: 20px 0; border-radius: 8px; font-weight: bold; text-align: left; }
        .vulnerable { background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }
        .secure { background: #d1fae5; color: #065f46; border: 1px solid #6ee7b7; }
        .badge { display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-left: 10px; }
        .badge-danger { background: #ef4444; color: white; }
        .badge-success { background: #10b981; color: white; }
        .btn { padding: 12px 24px; font-size: 16px; font-weight: bold; cursor: pointer; border: none; border-radius: 6px; color: white; transition: 0.2s; }
        .btn-toggle { background: #2563eb; }
        .btn-toggle:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Console Wi-Fi Hôtel (Officiel)</h1>
        <p>Contrôle des politiques de sécurité pour l'exposé</p>
        
        <div class="status-box {{ 'secure' if status.is_secure else 'vulnerable' }}">
            <p>📡 {**SSID :** Hotel_Premium_Guest</p>
            <p>🌐 **Sécurité Web (HSTS) :** {{ 'ACTIVÉE (HTTPS forcé)' if status.is_secure else 'DESACTIVÉE (HTTP standard)' }}
                <span class="badge {{ 'badge-success' if status.is_secure else 'badge-danger' }}">
                    {{ 'SÉCURISÉ' if status.is_secure else 'VULNÉRABLE' }}
                </span>
            </p>
        </div>

        <form action="/toggle" method="post">
            <button type="submit" class="btn btn-toggle">
                🔄 {{ 'Désactiver' if status.is_secure else 'Activer' }} l'en-tête de protection HSTS
            </button>
        </form>
    </div>
</body>
</html>
'''

HOTEL_PORTAL = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Portail Wi-Fi Grand Hôtel</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; text-align: center; padding-top: 100px; }
        .box { background: white; padding: 40px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.1); max-width: 400px; }
        .btn { background: #22c55e; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Bienvenue au Grand Hôtel</h2>
        <p>Profitez de votre accès Internet haut débit gratuit pendant votre séjour.</p>
        <button class="btn" onclick="alert('Votre connexion Internet est maintenant active !')">Accéder Gratuitement à Internet</button>
    </div>
</body>
</html>
'''

@app.route('/')
def admin_panel():
    # Interface d'administration accessible sur l'hôte local
    return render_template_string(GUI_TEMPLATE, status=network_status)

@app.route('/portal', defaults={'path': ''})
@app.route('/portal/<path:path>')
def hotel_portal(path):
    response = make_response(render_template_string(HOTEL_PORTAL))
    # Si le mode sécurisé est activé, on applique la contre-mesure HSTS
    if network_status["is_secure"]:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/toggle', methods=['POST'])
def toggle():
    network_status["is_secure"] = not network_status["is_secure"]
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)