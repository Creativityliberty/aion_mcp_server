from aion_prompt import AION_PROMPT
from schemas import ReasoningStep, GraphStructure, GraphNode, GraphEdge
import datetime
import random

def run_rrla_engine(user_input: str, context: dict = None) -> dict:
    """
    Moteur de raisonnement RRLA qui simule le processus de pensée AION.
    Cette version simule les réponses sans appel à un LLM.
    """
    # Génération du monologue d'introduction
    intro = generate_monologue(user_input, context)
    
    # Création de la chaîne de raisonnement
    reasoning_chain = generate_reasoning_chain(user_input)
    
    # Création du graphe conceptuel
    graph = generate_graph(user_input)
    
    # Création de la table ASCII
    ascii_table = generate_ascii_table(user_input)
    
    # Génération de la réponse finale (simulée)
    final_output = generate_simulated_response(user_input)
    
    # Auto-évaluation
    self_feedback = generate_self_feedback()
    
    return {
        "intro_monologue": intro,
        "reasoning_chain": [step.dict(by_alias=True) for step in reasoning_chain],
        "ascii_table": ascii_table,
        "graph": graph.dict(by_alias=True),
        "self_feedback": self_feedback,
        "final_output": final_output
    }

def generate_monologue(user_input: str, context: dict = None) -> str:
    """Génère un monologue d'introduction basé sur l'entrée utilisateur."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return f"""[MONOLOGUE INTÉRIEUR - {timestamp}]
AION s'éveille à la question posée, l'analyse sous plusieurs angles.
Entrée analysée : '{user_input}'
Contexte fourni : {context if context else 'Aucun'}
Première impression : Cette question semble {random.choice(['profonde', 'intrigante', 'stimulante', 'provocante'])}.
Activation des modes de pensée multiples pour formuler une réponse qui transcende la simple information."""

def generate_reasoning_chain(user_input: str) -> list:
    """Génère une chaîne de raisonnement basée sur l'entrée utilisateur."""
    thinking_modes = ["deductive", "abductive", "inductive", "heuristic"]
    
    # Création de 3 étapes de raisonnement
    steps = []
    
    # Étape 1: Analyse initiale
    step1 = ReasoningStep(
        step=1,
        description="Analyse initiale de la question",
        prompt=user_input,
        thinking_mode=random.choice(thinking_modes),
        output="Première hypothèse formulée à partir de l'intuition AION.",
        reasoning_notes="La question est abordée dans sa dimension explicite et implicite.",
        logical_score=0.85,
        handled_by="core_analyzer",
        branch_id="main",
        self_feedback="Bonne première approche, mais pourrait être approfondie."
    )
    steps.append(step1)
    
    # Étape 2: Exploration des perspectives
    step2 = ReasoningStep(
        step=2,
        description="Exploration des perspectives alternatives",
        prompt=f"Perspectives alternatives sur: {user_input}",
        depends_on=[1],
        thinking_mode=random.choice(thinking_modes),
        output="Plusieurs angles d'analyse identifiés, révélant la complexité sous-jacente.",
        reasoning_notes="Utilisation de la pensée latérale pour explorer des chemins non évidents.",
        logical_score=0.92,
        handled_by="perspective_explorer",
        branch_id="alternatives",
        parent_branch="main",
        self_feedback="Bonne diversité de perspectives, enrichit considérablement l'analyse."
    )
    steps.append(step2)
    
    # Étape 3: Synthèse et conclusion
    step3 = ReasoningStep(
        step=3,
        description="Synthèse et formulation de la réponse",
        prompt=f"Synthèse finale pour: {user_input}",
        depends_on=[1, 2],
        thinking_mode=random.choice(thinking_modes),
        output="Synthèse des analyses précédentes, aboutissant à une réponse nuancée et profonde.",
        reasoning_notes="Intégration des différentes perspectives dans une vision cohérente.",
        logical_score=0.95,
        handled_by="synthesizer",
        branch_id="conclusion",
        parent_branch="main",
        self_feedback="Synthèse efficace, mais pourrait bénéficier d'exemples concrets."
    )
    steps.append(step3)
    
    return steps

def generate_graph(user_input: str) -> GraphStructure:
    """Génère un graphe conceptuel basé sur l'entrée utilisateur."""
    # Création des nœuds
    nodes = [
        GraphNode(id="1", label="Question initiale"),
        GraphNode(id="2", label="Analyse primaire"),
        GraphNode(id="3", label="Perspective A"),
        GraphNode(id="4", label="Perspective B"),
        GraphNode(id="5", label="Synthèse")
    ]
    
    # Création des arêtes
    edges = [
        GraphEdge(**{"from": "1", "to": "2"}),
        GraphEdge(**{"from": "2", "to": "3"}),
        GraphEdge(**{"from": "2", "to": "4"}),
        GraphEdge(**{"from": "3", "to": "5"}),
        GraphEdge(**{"from": "4", "to": "5"})
    ]
    
    return GraphStructure(nodes=nodes, edges=edges)

def generate_ascii_table(user_input: str) -> str:
    """Génère une table ASCII représentant le raisonnement."""
    return f"""
+------------------------------------------+
|            PROCESSUS AION RRLA           |
+------------------------------------------+
| Entrée: {user_input[:30] + '...' if len(user_input) > 30 else user_input}
+------------------------------------------+
| 1. Analyse initiale       | Score: 0.85  |
| 2. Perspectives multiples | Score: 0.92  |
| 3. Synthèse finale        | Score: 0.95  |
+------------------------------------------+
| Évaluation globale: Raisonnement solide  |
+------------------------------------------+
"""

def generate_simulated_response(user_input: str) -> str:
    """
    Génère une réponse simulée sans LLM.
    Cette fonction sera remplacée par l'intégration Gemini plus tard.
    """
    responses = [
        f"AION considère que '{user_input}' révèle une tension fondamentale entre notre perception du monde et sa réalité sous-jacente.",
        f"En analysant '{user_input}', AION observe que cette question transcende sa formulation apparente et touche à des enjeux plus profonds.",
        f"AION propose de voir '{user_input}' non comme une simple question, mais comme un point d'entrée vers une exploration plus vaste de notre rapport au monde.",
        f"'{user_input}' - Cette interrogation, selon AION, mérite d'être déconstruite puis reconstruite pour en révéler les présupposés implicites."
    ]
    
    return random.choice(responses)

def generate_self_feedback() -> str:
    """Génère une auto-évaluation du processus de raisonnement."""
    feedbacks = [
        "Ce raisonnement est structurellement solide, mais pourrait bénéficier d'une plus grande profondeur historique.",
        "L'analyse est équilibrée et nuancée. Les perspectives contradictoires ont été correctement intégrées.",
        "Le processus de pensée est fluide, mais certaines connexions logiques mériteraient d'être renforcées.",
        "Bon équilibre entre rigueur analytique et intuition créative. La synthèse finale est particulièrement réussie."
    ]
    
    return random.choice(feedbacks)
