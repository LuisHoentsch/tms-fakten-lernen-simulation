from dataclasses import dataclass
from typing import List, Set, Tuple
import random
from enums import Gender
from Factoid import Factoid

@dataclass
class Question:
    question_text: str
    options: List[str]
    correct_answer: str

class QuestionGenerator:
    def __init__(self, factoids: List[List[Factoid]]):
        # Flatten the list of lists
        self.factoids = [f for group in factoids for f in group]

        # Pools for distractors
        self.names = list(set(f.name for f in self.factoids))
        self.jobs = list(set(f.job for f in self.factoids))
        self.diagnoses = list(set(f.diagnosis for f in self.factoids))
        self.situations = list(set(f.situation for f in self.factoids))
        self.ages = list(set(self._format_age(f.age) for f in self.factoids))

    @staticmethod
    def _format_age(age: str) -> str:
        return f"Ca. {age} Jahre"

    def _get_article(self, gender: Gender) -> str:
        return "der" if gender == Gender.MALE else "die"

    def _get_patient_noun(self, gender: Gender) -> str:
        return "Patient" if gender == Gender.MALE else "Patientin"

    def _apply_template(self, template_id: int, f: Factoid) -> Tuple[str, str, str]:
        """
        Returns (question_text, correct_answer_text, answer_type_key)
        """
        article = self._get_article(f.gender)
        noun = self._get_patient_noun(f.gender)
        age_formatted = self._format_age(f.age)

        if template_id == 1:
            # Wie heißt <der/die> <Patient/Patientin> mit <Symptom>? <Name>
            q = f"Wie heißt {article} {noun} mit {f.diagnosis}?"
            return q, f.name, 'name'

        elif template_id == 2:
            # Wie heißt <der/die> <Beruf>? <Name>
            q = f"Wie heißt {article} {f.job}?"
            return q, f.name, 'name'

        elif template_id == 3:
            # <Der/die> <Patient/Patientin> mit <Symptom> ist? <Beruf>
            q = f"{article.capitalize()} {noun} mit {f.diagnosis} ist?"
            return q, f.job, 'job'

        elif template_id == 4:
            # Welchen Beruf hat <der/die> <Patient/Patientin>, <der/die> <Situation> ist? <Beruf>
            q = f"Welchen Beruf hat {article} {noun}, {article} {f.situation} ist?"
            return q, f.job, 'job'

        elif template_id == 5:
            # <Der/die> <Patient/Patientin> mit <Symptom> ist? <Situation>
            q = f"{article.capitalize()} {noun} mit {f.diagnosis} ist?"
            return q, f.situation, 'situation'

        elif template_id == 6:
            # <Der/die> <Beruf> ist? <Situation>
            q = f"{article.capitalize()} {f.job} ist?"
            return q, f.situation, 'situation'

        elif template_id == 7:
            # Welche Diagnose hat <der/die> <Beruf>? <Symptom>
            q = f"Welche Diagnose hat {article} {f.job}?"
            return q, f.diagnosis, 'diagnosis'

        elif template_id == 8:
            # Welche Diagnose hat <der/die> <Patient/Patientin>, <der/die> <Situation> ist? <Symptom>
            q = f"Welche Diagnose hat {article} {noun}, {article} {f.situation} ist?"
            return q, f.diagnosis, 'diagnosis'

        elif template_id == 9:
            # Wie alt ist <der/die> <Patient/Patientin> mit <Symptom>? <Alter>
            q = f"Wie alt ist {article} {noun} mit {f.diagnosis}?"
            return q, age_formatted, 'age'

        elif template_id == 10:
            # Wie alt ist <der/die> <Patient/Patientin>, <der/die> <Situation> ist? <Alter>
            q = f"Wie alt ist {article} {noun}, {article} {f.situation} ist?"
            return q, age_formatted, 'age'

        else:
            raise ValueError(f"Unknown template_id: {template_id}")

    def _get_pool(self, key: str) -> List[str]:
        if key == 'name':
            return self.names
        elif key == 'job':
            return self.jobs
        elif key == 'situation':
            return self.situations
        elif key == 'diagnosis':
            return self.diagnoses
        elif key == 'age':
            return self.ages
        else:
            return []

    def _generate_options(self, correct: str, pool: List[str]) -> List[str]:
        options = [x for x in pool if x != correct]
        if len(options) >= 4:
            distractors = random.sample(options, 4)
        else:
            distractors = options
            # If we strictly need 5 options, we might need to handle this.
            # But assuming the dataset is large enough as per analysis.

        final_options = distractors + [correct]
        random.shuffle(final_options)
        return final_options

    def generate_questions(self, num_questions: int = 20) -> List[Question]:
        questions = []
        used_combinations: Set[Tuple[int, int]] = set() # (template_id, factoid_index)

        # Safety counter to prevent infinite loop
        attempts = 0
        max_attempts = num_questions * 50

        while len(questions) < num_questions and attempts < max_attempts:
            attempts += 1

            # Pick random template (1-10) and random factoid
            t_id = random.randint(1, 10)
            f_idx = random.randint(0, len(self.factoids) - 1)

            if (t_id, f_idx) in used_combinations:
                continue

            f = self.factoids[f_idx]
            q_text, correct, q_type = self._apply_template(t_id, f)
            pool = self._get_pool(q_type)

            options = self._generate_options(correct, pool)

            questions.append(Question(
                question_text=q_text,
                options=options,
                correct_answer=correct
            ))
            used_combinations.add((t_id, f_idx))

        return questions
