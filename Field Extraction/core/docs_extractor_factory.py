from typing import Dict
from core.docs_extractor import DocsExtractor
from models.azure_docs_extractor import AzureDocsExtractor

class DocsExtractorFactory:
    """
    Factory class for creating document extractors.
    """
    extractors: Dict[str, DocsExtractor] = {
        "azure": AzureDocsExtractor()
    }

    @classmethod
    def create(cls, extractor_name: str) -> DocsExtractor:
        """
        Create a document extractor based on the provided name.
        
        Args:
            extractor_name: Name of the document extractor to create.
            
        Returns:
            DocsExtractor: Created document extractor instance.
        """
        if extractor_name not in cls.extractors:
            raise ValueError(f"Unknown document extractor: {extractor_name}")
        
        return cls.extractors[extractor_name]