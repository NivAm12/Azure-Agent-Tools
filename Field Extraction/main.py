from dotenv import load_dotenv
from core.docs_extractor_factory import DocsExtractorFactory
load_dotenv()

if __name__ == "__main__":
    extractor_name = "azure"
    extractor = DocsExtractorFactory.create(extractor_name)
    