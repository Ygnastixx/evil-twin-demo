# 🛡️ Simulation d'Attaque Evil Twin & Contre-mesures (Exposé)

Ce projet académique permet de simuler une attaque Wi-Fi de type **Evil Twin** (Jumeau Maléfique) et de démontrer l'efficacité des contre-mesures associées (**WPA2/WPA3** et **HSTS**).

Le projet est divisé en deux rôles distincts, portés par deux serveurs Flask indépendants.

---

## 🛠️ Installation Générale (Pour tous les membres)

Chaque participant doit préparer son environnement Python :

1. **Cloner le projet** :
```bash
git clone <url-de-votre-depot-git>
cd evil-twin-demo

```

2. **Créer un environnement virtuel** :
```bash
python -m venv venv
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate

```


3. **Installer les dépendances** :
```bash
pip install -r requirements.txt

```



---

## ⚙️ GUIDE DE CONFIGURATION DU WI-FI (Étape par Étape)

Pour l'exposé, nous allons modifier manuellement la configuration de la carte Wi-Fi de l'**Ordinateur Légitime** pour illustrer l'état de sécurité "Avant" et "Après".

### 🔴 CONFIGURATION 1 : Le Réseau Vulnérable (Avant)

L'objectif est de créer un réseau totalement ouvert (sans mot de passe).

#### Sur Windows 10 / 11 :

1. Ouvrez les **Paramètres** (`Windows + I`) puis allez dans **Réseau et Internet**.
2. Cliquez sur **Point d'accès sans fil mobile** dans le menu de gauche.
3. Cliquez sur le bouton **Modifier**.
4. Configurez ainsi :
* **Nom du réseau (SSID)** : `Cafe_Gratuit`
* **Mot de passe réseau** : *Si Windows vous y oblige, mettez `12345678`. Si votre système le permet, laissez le champ vide.*
* **Bande réseau** : `2,4 GHz` (plus stable pour la démo).


5. Activez l'interrupteur **Point d'accès sans fil mobile** tout en haut.

#### Sur macOS :

1. Allez dans **Réglages Système** > **Partage** > **Partage Internet**.
2. Cliquez sur l'icône `i` (Informations) à côté de Partage Internet.
3. Dans **Options Wi-Fi** :
* **Nom du réseau** : `Cafe_Gratuit`
* **Sécurité** : Sélectionnez **Aucune** (Réseau Ouvert).


4. Activez le Partage Internet.

---

### 🟢 CONFIGURATION 2 : Le Réseau Sécurisé (Après)

L'objectif est d'appliquer le chiffrement fort pour bloquer l'usurpation.

#### Sur Windows 10 / 11 :

1. Retournez dans les paramètres du **Point d'accès sans fil mobile**.
2. Cliquez sur **Modifier**.
3. Changez les paramètres suivants :
* **Type de sécurité** : Sélectionnez **WPA3-Personnel (SAE)** (ou *WPA2-Personnel* si votre carte PC est plus ancienne).
* **Mot de passe réseau** : Saisissez un mot de passe robuste (ex: `TechCorp2026!Security`).


4. Enregistrez et réactivez le point d'accès.

#### Sur macOS :

1. Retournez dans **Réglages Système** > **Partage** > **Partage Internet** (désactivez-le temporairement pour modifier).
2. Dans **Options Wi-Fi** :
* **Sécurité** : Sélectionnez **WPA3 Personnel** (ou *WPA2/WPA3 Transition*).
* **Mot de passe** : Saisissez votre clé robuste.


3. Réactivez le Partage Internet.

---

## 💻 LANCEMENT DES SERVEURS FLASK

### 1. Démarrer le Serveur Légitime (Ordinateur A)

Exécutez le script avec les privilèges d'administration requis pour utiliser le port 80 :

* **Windows (Invite de commande en Admin)** : `python legit_server/legit_server.py`
* **Mac/Linux** : `sudo python legit_server/legit_server.py`

*Ouvrez votre navigateur sur `http://localhost` pour accéder à la console d'administration et gérer le bouton HSTS.*

### 2. Démarrer le Serveur Pirate (Ordinateur B)

L'attaquant prépare son piège en arrière-plan **SANS activer son point d'accès Wi-Fi au début** :

* **Windows (Admin)** : `python attacker_server/attacker_server.py`
* **Mac/Linux** : `sudo python attacker_server/attacker_server.py`

---

## 🎬 DÉROULEMENT DE LA DÉMONSTRATION (Jour J)

1. **Scénario Vulnérable** : Connectez le téléphone au Wi-Fi ouvert de l'Ordinateur A. Coupez le Wi-Fi de l'Ordinateur A. Activez le Wi-Fi ouvert (même SSID) sur l'Ordinateur B. Le téléphone bascule, la victime navigue et ses identifiants sont volés en direct sur le terminal de l'Ordinateur B.
2. **Scénario Sécurisé** : Appliquez la **Configuration 2 (WPA2/WPA3)** sur l'Ordinateur A et cliquez sur "Activer les mesures de sécurité" sur sa console Web (HSTS). Tentez de reproduire l'attaque : le téléphone refuse de s'associer au pirate ou bloque la page web avec une alerte de sécurité.

