import random
from typing import List
from Factoid import Factoid
from data import NAME_GROUPS, JOB_GROUPS, AGES, SYMPTOMS, SITUATIONS
from enums import Gender
from models import Job


class FactSheet:
    def __init__(self, n_groups: int = 5, n_per_group: int = 3):
        self.n_groups = n_groups
        self.n_per_group = n_per_group
        self.factoids: List[List[Factoid]] = []
        self._generate_factoids()

    def __str__(self) -> str:
        blocks = []
        for group in self.factoids:
            block = "\n".join(str(factoid) for factoid in group)
            blocks.append(block)
        return "\n\n".join(blocks) + "\n"

    def _generate_factoids(self):
        # Create deep copies (lists) of the global data to prevent mutation and allow shuffling/popping
        name_groups = [list(group) for group in NAME_GROUPS]
        job_groups = [list(group) for group in JOB_GROUPS]
        ages = list(AGES)
        symptoms = list(SYMPTOMS)
        situations = list(SITUATIONS)

        random.shuffle(name_groups)
        random.shuffle(job_groups)
        random.shuffle(ages)
        random.shuffle(symptoms)
        random.shuffle(situations)

        for _ in range(self.n_groups):
            if not name_groups:
                raise ValueError(f"Not enough name groups for n_groups={self.n_groups}")
            if not job_groups:
                raise ValueError(f"Not enough job groups for n_groups={self.n_groups}")
            if not ages:
                raise ValueError(f"Not enough ages for n_groups={self.n_groups}")

            self.factoids.append(
                self._generate_factoid_group(
                    self.n_per_group,
                    name_groups.pop(),
                    job_groups.pop(),
                    ages.pop(),
                    symptoms,
                    situations,
                )
            )

    @staticmethod
    def _generate_factoid_group(
        n_per_group: int,
        name_group: List[str],
        job_group: List[Job],
        age: str,
        symptoms: List[str],
        situations: List[str],
    ) -> List[Factoid]:
        factoid_group: List[Factoid] = []

        random.shuffle(name_group)
        random.shuffle(job_group)

        for _ in range(n_per_group):
            if not name_group:
                raise ValueError("Not enough names in group")
            if not job_group:
                raise ValueError("Not enough jobs in group")
            if not symptoms:
                raise ValueError("Not enough symptoms globally")
            if not situations:
                raise ValueError("Not enough situations globally")

            gender = random.choice(list(Gender))
            job_obj = job_group.pop()

            factoid_group.append(
                Factoid(
                    gender=gender,
                    name=name_group.pop(),
                    age=age,
                    job=job_obj.get_title(gender),
                    symptom=symptoms.pop(),
                    situation=situations.pop(),
                )
            )

        return factoid_group
