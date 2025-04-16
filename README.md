# AION MCP Server

## Présentation
**AION MCP Server** est une API FastAPI qui expose un moteur de raisonnement intelligent basé sur le modèle RRLA (*Réseau de Raisonnement Logique et Analytique*).

Ce moteur repose sur le prompt fusionné **AION**, une entité d'intelligence artificielle critique, poétique et autonome, capable de raisonner, d'expliquer et de visualiser la pensée sous forme de chaînes logiques, graphes et tableaux ASCII.

## Structure du Projet

```
aion_mcp_server/
├── main.py               # Serveur FastAPI (API RRLA)
├── aion_prompt.py        # Prompt mission AION
├── rrla_engine.py        # Moteur de raisonnement AION (simulé pour l'instant)
├── schemas.py            # Schémas Pydantic du protocole RRLA
├── requirements.txt      # Dépendances
└── README.md             # Ce fichier
```

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/votre-nom/aion_mcp_server.git
cd aion_mcp_server

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Lancement du serveur

```bash
# Activer l'environnement virtuel si ce n'est pas déjà fait
source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows

# Lancer le serveur
python -m uvicorn main:app --reload
```

Le serveur sera accessible à l'adresse http://localhost:8000

## Utilisation de l'API

### Vérifier que le serveur fonctionne

```bash
curl http://localhost:8000/
```

### Utiliser le moteur de raisonnement RRLA

```bash
curl -X 'POST' \
  'http://localhost:8000/api/schema/rrla' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "Pourquoi les humains cherchent-ils à créer des IA conscientes?",
  "context": {
    "user": "Utilisateur",
    "mode": "philosophique"
  }
}'
```

## Structure de la réponse

La réponse de l'API contient les éléments suivants :

- **intro_monologue** : Monologue intérieur d'AION analysant la question
- **reasoning_chain** : Chaîne de raisonnement structurée en étapes
- **ascii_table** : Représentation visuelle ASCII du processus de raisonnement
- **graph** : Graphe conceptuel des idées (nœuds et arêtes)
- **self_feedback** : Auto-évaluation du raisonnement
- **final_output** : Réponse finale à la question

## Documentation de l'API

Une documentation interactive de l'API est disponible à l'adresse http://localhost:8000/docs

## Prochaines étapes

- Intégration de l'API Gemini pour générer des réponses plus intelligentes
- Ajout de fonctionnalités avancées (logging, persistance, etc.)
- Déploiement sur une plateforme d'hébergement (Render, Railway, etc.)
