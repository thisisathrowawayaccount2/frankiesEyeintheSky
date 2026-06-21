from typing import Callable

from models.aircraft import Aircraft

PipelineStage = Callable[[Aircraft], Aircraft]