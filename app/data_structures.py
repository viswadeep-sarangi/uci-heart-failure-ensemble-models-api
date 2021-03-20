from pydantic import BaseModel
from typing import Optional, List, Dict
from enum import Enum
from fastapi import UploadFile, File


class PredictRequest(BaseModel):
    features: Dict[str, float]


class ModelResponse(BaseModel):
    predictions: Optional[List[Dict[str, float]]]
    error: Optional[str]


class TrainRequest(BaseModel):
    data: UploadFile = File(...)
    model_name: str
    save_model: Optional[bool]


class TrainResponse(BaseModel):
    accuracy: str
    model_hash_id: Optional[str]


class ModelName(str, Enum):
    svm = "svm"
    decisiontree = "decisiontree"
    neuralnetwork = "neuralnetwork"