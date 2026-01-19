from dataclasses import dataclass


@dataclass
class Factoid:
    gender: int  # 0: Herr, 1: Frau
    name: str
    age: str
    job: str
    symptom: str
    situation: str

    def __str__(self) -> str:
        return f"{["Herr", "Frau"][self.gender]} {self.name}:\t\t{self.age},\t\t{self.job}, {self.situation}\t-\t{self.symptom}"
