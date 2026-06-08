# Simulation d'Attaque Evil Twin & Mécanismes de Protection

Ce dépôt contient le matériel nécessaire pour réaliser une démonstration académique d'une attaque Wi-Fi de type **Evil Twin** (Jumeau Maléfique) couplée à une tentative d'ingénierie sociale.

La démonstration s'articule autour de 3 rôles distincts (répartis idéalement sur 3 ordinateurs).

---

## Installation et Prérequis

Chaque machine participantaux rôles de serveurs doit disposer de l'environnement Python configuré :

1. **Récupération du projet** :
```bash
git clone https://github.com/Ygnastixx/evil-twin-demo.git
cd evil-twin-demo
```

2. **Création d'un environnement virtuel** :
```bash
python -m venv venv
# Activation sous windows
venv\Scripts\activate
# Activation sous Mac/Linux
source venv\Scripts\activate
```

3. **Installation des dépendances** :
```bash
pip install -r requirements.txt
```

---
## Guide de lancement de la simulation
 Voir [le guide prévu à cet effet](DEMO_SCRIPT.md).

---
