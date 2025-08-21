from typing import Dict, Type
from core.docs_extractor import DocsExtractor
from models.azure_docs_extractor import AzureDocsExtractor
from pydantic import BaseModel
from config.schemas import BituachLeumiSchema
from config.prompts import prompts, Prompts
from config.config_base import DocsExtractorConfig

class DocsExtractorFactory:
    """
    Factory class for creating document extractors.
    """
    extractors: Dict[str, DocsExtractor] = {
        "azure": AzureDocsExtractor
    }
    configs: Dict[str, DocsExtractorConfig] = {
        "bituach_leumi": DocsExtractorConfig(
            output_schema=BituachLeumiSchema,
            post_process_prompts=prompts["bituach_leumi"])
    }

    @classmethod
    def create(cls, extractor_name: str, config_name: str) -> DocsExtractor:
        """
        Create a document extractor based on the provided name.
        
        Args:
            extractor_name: Name of the document extractor to create.
            
        Returns:
            DocsExtractor: Created document extractor instance.
        """
        if extractor_name not in cls.extractors:
            raise ValueError(f"Unknown document extractor: {extractor_name}")
        if config_name not in cls.configs:
            raise ValueError(f"Unknown document extractor config: {config_name}")
        
        return cls.extractors[extractor_name](config=cls.configs[config_name])