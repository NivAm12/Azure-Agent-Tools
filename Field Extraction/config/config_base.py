from typing import  Type
from pydantic import BaseModel
from .prompts import Prompts

class DocsExtractorConfig(BaseModel):
    output_schema: Type[BaseModel]
    post_process_prompts: Prompts