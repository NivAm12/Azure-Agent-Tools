from abc import ABC, abstractmethod

class DocsExtractor(ABC):
    """
    Abstract base class for document extractors using a two-stage processing pipeline.
    
    This class defines the interface for document extraction systems that use:
    1. A primary extraction client (OCR, LLM, or hybrid system)
    2. An optional secondary LLM for post-processing and refinement
    
    The design supports flexible architectures:
    - OCR + LLM post-processing (traditional pipeline)
    - LLM-only extraction (modern approach)
    - OCR-only extraction (basic text extraction)
    """
    
    def __init__(self, primary_extractor, post_processor=None):
        """
        Initialize the document extractor with primary and optional secondary components.
        
        Args:
            primary_extractor: Primary extraction component that handles the initial document processing.
                             Can be:
                             - OCR client (Azure Document Intelligence, Abbyy OCR, etc.)
                             - LLM client (GPT-4, Claude, etc.) for direct document-to-data extraction
                             - Custom extraction service or hybrid system
                             
            post_processor: Optional secondary LLM component for post-processing and refinement.
                          Typically used for:
                          - Structuring raw OCR output into JSON format
                          - Data validation and correction
                          - Field mapping and normalization  
                          - Quality enhancement and error correction
                          - Language translation or standardization
                          Can be None if primary_extractor handles complete extraction.
        """
        self.primary_extractor = primary_extractor
        self.post_processor = post_processor
        
    @abstractmethod
    def extract(self, document: bytes):
        """
        Extract structured information from a document.
        
        This method defines the core extraction interface that concrete implementations
        must provide. The extraction process typically follows these stages:
        
        1. Primary extraction using self.primary_extractor
        2. Optional post-processing using self.post_processor (if available)
        3. Return structured results
        
        Args:
            document: Document to process. Typically a PDF or image file.
        
        Returns:
            Structured extraction results. Format depends on implementation:
            - Dict[str, Any]: Simple key-value structured data
            - ExtractionResult: Rich result object with metadata and validation
            - Custom result type specific to the extractor
        """
        pass