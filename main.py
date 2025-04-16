from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import ReasoningInput, ReasoningOutput
from rrla_engine import run_rrla_engine
import uvicorn

# Création de l'application FastAPI
app = FastAPI(
    title="AION MCP Server",
    description="Serveur MCP exposant le moteur de raisonnement AION basé sur l'architecture RRLA",
    version="1.0.0"
)

# Configuration CORS pour permettre les requêtes cross-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifiez les domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Endpoint racine pour vérifier que le serveur fonctionne."""
    return {
        "status": "online",
        "service": "AION MCP Server",
        "version": "1.0.0",
        "endpoints": {
            "reasoning": "/api/schema/rrla"
        }
    }

@app.post("/api/schema/rrla", response_model=ReasoningOutput)
async def rrla_reasoner(input_data: ReasoningInput):
    """
    Endpoint principal du moteur de raisonnement RRLA.
    
    Reçoit une structure ReasoningInput et retourne une réponse RRLA complète
    générée par le moteur AION.
    """
    try:
        # Appel au moteur RRLA
        result = run_rrla_engine(input_data.input, input_data.context)
        return result
    except Exception as e:
        # Gestion des erreurs
        raise HTTPException(status_code=500, detail=f"Erreur du moteur RRLA: {str(e)}")

# Point d'entrée pour exécuter l'application directement
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
