from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any

class GraphNode(BaseModel):
    id: str
    label: str

class GraphEdge(BaseModel):
    from_: str = Field(..., alias="from")
    to: str

class ReasoningStep(BaseModel):
    step: int
    description: str
    prompt: str
    depends_on: List[int] = []
    output: Optional[str] = None
    thinking_mode: Literal["deductive", "inductive", "abductive", "heuristic"]
    ai_override: bool = False
    reasoning_notes: Optional[str] = None
    trace: Optional[List[Dict[str, str]]] = None
    logical_score: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    handled_by: Optional[str] = None
    branch_id: Optional[str] = None
    parent_branch: Optional[str] = None
    self_feedback: Optional[str] = None

class GraphStructure(BaseModel):
    nodes: List[GraphNode] = []
    edges: List[GraphEdge] = []

class CognitiveEvent(BaseModel):
    timestamp: str
    source: str
    impact: str
    category: str

class ReasoningInput(BaseModel):
    input: str
    context: Optional[Dict[str, Any]] = {}
    reasoning_chain: Optional[List[ReasoningStep]] = []
    hypotheses: Optional[List[str]] = []
    graph: Optional[GraphStructure] = None
    granularity: Optional[Literal["macro", "meso", "micro"]] = "macro"
    cognitive_events: Optional[List[CognitiveEvent]] = []
    ascii_table: Optional[str] = None
    intro_monologue: Optional[str] = None

class ReasoningOutput(BaseModel):
    intro_monologue: str
    reasoning_chain: List[Dict[str, Any]]
    ascii_table: str
    graph: Dict[str, Any]
    self_feedback: str
    final_output: str
