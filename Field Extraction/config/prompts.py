from pydantic import BaseModel

class Prompts(BaseModel):
    system: str
    
prompts = {
    "bituach_leumi": Prompts(system="""
        You task is to extract fields from Bituach Leumi (Israel National Insurance) forms. The form may be Hebrew or English.\n
        Return ONLY valid JSON that matches the provided JSON Schema. If a field is missing or unclear, use an empty string.\n
        Prefer exact substrings from the OCR text.
        """
    )
}