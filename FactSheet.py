import random
from typing import List
from Factoid import Factoid
from data import NAME_GROUPS, JOB_GROUPS, AGES, SYMPTOMS, SITUATIONS


class FactSheet:
    def __init__(self, n_groups: int = 5, n_per_group: int = 3):
        self.n_groups = n_groups
        self.n_per_group = n_per_group
        self.factoids: List[List[Factoid]] = []
        self._generate_factoids()

    def __str__(self):
        return_string = ""
        for i in range(self.n_groups):
            for j in range(self.n_per_group):
                return_string += str(self.factoids[i][j]) + "\n"
            return_string += "\n"
        return return_string

    def _generate_factoids(self):

        name_groups = list(NAME_GROUPS)
        job_groups = list(JOB_GROUPS)
        ages = list(AGES)
        symptoms = list(SYMPTOMS)
        situations = list(SITUATIONS)

        random.shuffle(name_groups)
        random.shuffle(job_groups)
        random.shuffle(ages)
        random.shuffle(symptoms)
        random.shuffle(situations)

        for _ in range(self.n_groups):
            if not name_groups or not job_groups or not ages:
                raise ValueError("n_groups is too big")

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
        job_group: List[str],
        age: str,
        symptoms: List[str],
        situations: List[str],
    ) -> List[Factoid]:
        factoid_group: List[Factoid] = []

        random.shuffle(name_group)
        random.shuffle(job_group)

        for _ in range(n_per_group):
            if not name_group or not job_group:
                raise ValueError("n_per_group is too big")
            if not symptoms or not situations:
                raise ValueError("n_groups * n_per_group is too big")

            gender = random.choice([0, 1])

            factoid_group.append(
                Factoid(
                    gender,
                    name_group.pop(),
                    age,
                    job_group.pop()[gender],
                    symptoms.pop(),
                    situations.pop(),
                )
            )

        return factoid_group
