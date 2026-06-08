#⚙️ CONFIGURATION DES RÉSEAUX SANS FIL (Scénario de l'Hôtel)
Pour illustrer les états "Avant" et "Après" les mesures de sécurité, la configuration Wi-Fi des machines doit être gérée manuellement selon les étapes suivantes.

##🔴 Phase 1 : Le Réseau Vulnérable (Réseau Ouvert)
###Sur l'Ordinateur Légitime (Réseau de l'Hôtel) :
Activez le Point d'accès sans fil mobile (Hotspot) natif du système d'exploitation (Windows ou macOS).

Configurez les propriétés de diffusion :
```
Nom du réseau (SSID) : Hotel_Premium_Guest
```

Sécurité : Sélectionnez Ouvert (Open / Aucun mot de passe). 
Note : si l'OS exige une clé, définissez un mot de passe trivial connu du groupe (ex: 12345678).

###Sur l'Ordinateur Attaquant :
Préparez la configuration de votre partage de connexion avec exactement le même nom : `Hotel_Premium_Guest` en mode Ouvert.

Laissez ce point d'accès désactivé au début de la démonstration.

##🟢 Phase 2 : Le Réseau Sécurisé (Chiffrement fort)
Après constatation des risques, l'Ordinateur Légitime applique les contre-mesures techniques :

* Accédez aux paramètres du point d'accès sans fil mobile de l'ordinateur légitime.

* Modifiez le profil de sécurité :
```
Type de sécurité : Choisissez WPA3-Personnel (SAE) (ou WPA2-Personnel selon la compatibilité matérielle).

Clé de sécurité : Définissez un mot de passe fort (ex: HotelSecurity2026!).
```

#🎬 DÉROULEMENT DE LA DÉMONSTRATION (Scénario de l'Exposé)
Rôles affectés :
* **Ordinateur A** : Serveur Légitime (Interface d'administration + Vrai Portail).

* **Ordinateur B** : Victime (Son écran est connecté au vidéoprojecteur de la salle).

* **Ordinateur C** : Attaquant (Serveur de capture).

###Partie A : Démonstration de la Vulnérabilité (État "Avant")
- Démarrage des services :

  * Sur l'Ordinateur A (Admin) : 
    ```
    python legit_server/legit_server.py (puis allez sur http://localhost/portal).
    ```
  * Sur l'Ordinateur C (Admin) : 
    ```
    python attacker_server/attacker_server.py.
    ```

- Connexion initiale : **L'Ordinateur B (Victime) se connecte au Wi-Fi ouvert Hotel_Premium_Guest.** En naviguant sur le web, la page d'accueil officielle s'affiche.


- Le Sabotage : **L'Ordinateur A coupe son point d'accès** Wi-Fi. Simultanément, **l'Ordinateur C active son point d'accès** clone.


- Le Piège : **L'Ordinateur B (Victime)** est automatiquement reconnecté au clone en raison de la similitude du SSID. Lors d'une **tentative de navigation** vers une page non chiffrée, le faux portail apparaît à l'écran du projecteur, simulant une déconnexion technique et proposant une reconnexion via Google ou Microsoft 365.


- La Capture : **La victime saisit des identifiants de test**. **Les données s'affichent** instantanément en rouge **sur le terminal de l'Ordinateur C**.

###Partie B : Application des Contre-mesures (État "Après")
* **Correction Wi-Fi** : L'Ordinateur A applique la Phase 2 (WPA2/WPA3) sur son infrastructure sans fil.

* **Correction Web** : Sur la console d'administration de l'Ordinateur A (http://localhost), activez l'interrupteur pour déployer l'en-tête HSTS.

* **Résultat** : Tentez de reproduire l'attaque. L'Ordinateur B refusera de s'associer au réseau ouvert de l'attaquant ou, si le flux Web est intercepté, le navigateur affichera un avertissement de sécurité bloquant empêchant l'accès au faux portail d'authentification.