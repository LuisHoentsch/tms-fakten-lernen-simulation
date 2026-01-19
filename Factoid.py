from dataclasses import dataclass
from enums import Gender


@dataclass
class Factoid:
    gender: Gender
    name: str
    age: str
    job: str
    diagnosis: str
    situation: str

    def __str__(self) -> str:
        salutation = "Herr" if self.gender == Gender.MALE else "Frau"
        full_name = f"{salutation} {self.name}:"
        formatted_age = f"ca. {self.age} Jahre"

        # Adjust padding values as needed for optimal display
        return (
            f"{full_name:<20} "
            f"{formatted_age:<20} "
            f"{self.job + ',':<20} "
            f"{self.situation:<20} "
            f"{self.diagnosis}"
        )
