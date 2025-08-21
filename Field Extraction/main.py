from dotenv import load_dotenv
load_dotenv()
from core.docs_extractor_factory import DocsExtractorFactory

if __name__ == "__main__":
    extractor_name = "azure"
    extractor = DocsExtractorFactory.create(extractor_name)
    doc_path = 'Field Extraction/test_data/283_ex1.pdf'

    with open(doc_path, 'rb') as f:
        document = f.read()
        result = extractor.extract(document)
        print(result)
    