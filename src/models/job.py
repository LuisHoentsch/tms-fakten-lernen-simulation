from dataclasses import dataclass
from src.data.enums import Gender

@dataclass(frozen=True)
class Job:
    male: str
    female: str

    def get_title(self, gender: Gender) -> str:
        return self.male if gender == Gender.MALE else self.female
