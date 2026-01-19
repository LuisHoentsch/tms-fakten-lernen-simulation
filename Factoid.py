from dataclasses import dataclass
from enums import Gender


@dataclass
class Factoid:
    gender: Gender
    name: str
    age: str
    job: str
    symptom: str
    situation: str

    def __str__(self) -> str:
        salutation = "Herr" if self.gender == Gender.MALE else "Frau"
        full_name = f"{salutation} {self.name}:"

        # Adjust padding values as needed for optimal display
        return (
            f"{full_name:<15} "
            f"{self.age:<15} "
            f"{self.job + ',':<25} "
            f"{self.situation:<20} "
            f"- {self.symptom}"
        )
