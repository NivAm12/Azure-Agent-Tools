from abc import ABC, abstractmethod

class DocsExtractor(ABC):
    """Abstract base class for form extractors"""
    @abstractmethod
    def extract(self, text):
        pass