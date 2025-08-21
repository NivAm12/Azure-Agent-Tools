from core.docs_extractor import DocsExtractor
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
from config.config_base import DocsExtractorConfig
import os

# Load environment variables
DI_KEY = os.getenv("DI_KEY", "")
DI_ENDPOINT = os.getenv("DI_ENDPOINT", "")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "")
AZURE_OPENAI_MODEL=os.getenv("AZURE_OPENAI_MODEL", "")

class AzureDocsExtractor(DocsExtractor):
    """
    Azure Docs Extractor class that extends the DocsExtractor class.
    This class encapsulates the Azure Document Intelligence (DI) and Azure OpenAI APIs for document extraction.
    """
    def __init__(self, config: DocsExtractorConfig=None):
        try:
            primary_extractor = DocumentIntelligenceClient(
                        endpoint=DI_ENDPOINT,
                        credential=AzureKeyCredential(DI_KEY)
                    )
            post_processor = AzureOpenAI(azure_endpoint=AZURE_OPENAI_ENDPOINT,
                                        api_key=AZURE_OPENAI_KEY,
                                        api_version=AZURE_OPENAI_API_VERSION)
            super().__init__(primary_extractor, post_processor, config=config)
        except Exception as e:
            print(f"Error initializing Azure Docs Extractor: {e}")
            raise e
        
    
    def extract(self, document: bytes):
        """
        Extract structured information from a document using Azure Document Intelligence and Azure OpenAI APIs.
        """
        # Step 1: Perform OCR using Azure Document Intelligence
        ocr_res = self._extract_text_with_ocr(document)
        # Step 2: Post-process the OCR output using Azure OpenAI
        response = self._post_process(ocr_res)

        return response
    def _extract_text_with_ocr(self, document: bytes):
        """
        Extract text from a document using Azure Document Intelligence.
        """
        try:
            ocr_res = self.primary_extractor.begin_analyze_document(
                "prebuilt-layout", 
                body=AnalyzeDocumentRequest(
                    bytes_source=document
                ),
            )
            result = ocr_res.result()
            return result.content
        except Exception as e:
            print(f"Error in Azure Docs Extractor: {e}")
            raise e
    
    def _post_process(self, ocr_res: str):
        """
        Post-process the OCR output using Azure OpenAI.
        """
        try:
            sys_prompt = self.config.post_process_prompts.system
            # user_dummy_prompt = self.post_process_prompts["user_prompt"]
            user_dummy_prompt = ("OCR TEXT (may contain Hebrew/English, mixed):\n" + ocr_res)

            response = self.post_processor.chat.completions.parse(
            model=AZURE_OPENAI_MODEL,
            temperature=0,
            response_format=self.config.output_schema,
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_dummy_prompt},
            ],
        )
            
            return response.choices[0].message.parsed
        except Exception as e:
            print(f"Error in Azure Docs Extractor: {e}")
            raise e