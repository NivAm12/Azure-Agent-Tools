from pydantic import BaseModel, Field

class DateTriple(BaseModel):
    day: str = ""
    month: str = ""
    year: str = ""

class Address(BaseModel):
    street: str = ""
    houseNumber: str = ""
    entrance: str = ""
    apartment: str = ""
    city: str = ""
    postalCode: str = ""
    poBox: str = ""

class MedicalInstitutionFields(BaseModel):
    healthFundMember: str = ""
    natureOfAccident: str = ""
    medicalDiagnoses: str = ""

class BituachLeumiSchema(BaseModel):
    lastName: str = ""
    firstName: str = ""
    idNumber: str = ""
    gender: str = ""
    dateOfBirth: DateTriple = Field(default_factory=DateTriple)
    address: Address = Field(default_factory=Address)
    landlinePhone: str = ""
    mobilePhone: str = ""
    jobType: str = ""
    dateOfInjury: DateTriple = Field(default_factory=DateTriple)
    timeOfInjury: str = ""
    accidentLocation: str = ""
    accidentAddress: str = ""
    accidentDescription: str = ""
    injuredBodyPart: str = ""
    signature: str = ""
    formFillingDate: DateTriple = Field(default_factory=DateTriple)
    formReceiptDateAtClinic: DateTriple = Field(default_factory=DateTriple)
    medicalInstitutionFields: MedicalInstitutionFields = Field(default_factory=MedicalInstitutionFields)