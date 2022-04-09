from pydantic import BaseModel, validator


class Company(BaseModel):
    phones: list[str]
    emails: list[str]

    @validator("*", pre=True)
    def split_str(cls, value):
        if isinstance(value, str):
            return value.split("|")
        return value

    @validator("phones", "emails")
    def check_list_type(cls, value):
        if not isinstance(value, list):
            raise ValueError("it is not list type")
        return value


def test_case():
    Company(
        phones="01011112222|01033334444", emails="info@example.com|admin@example.com"
    )
