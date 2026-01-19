from dataclasses import dataclass
from typing import List, Set, Tuple
import random
from src.data.enums import Gender
from src.models.factoid import Factoid
from src.data.constants import QUESTION_TEMPLATES

@dataclass
class Question:
    question_text: str
    options: List[str]
    correct_answer: int

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

    def _generate_options(self, correct: str, q_type: str) -> List[str]:
        pool = self._get_pool(q_type)
        options = [x for x in pool if x != correct]
        if len(options) >= 4:
            distractors = random.sample(options, 4)
        else:
            distractors = options

        final_options = distractors + [correct]
        random.shuffle(final_options)
        return final_options

    def _format_question(self, template: Tuple[str, str], f: Factoid) -> Tuple[str, str, str]:
        """
        Formats the question string and retrieves the correct answer.
        Returns (question_text, correct_answer_text, answer_type_key)
        """
        pattern, answer_key = template

        article = self._get_article(f.gender)
        noun = self._get_patient_noun(f.gender)
        formatted_age = self._format_age(f.age)

        context = {
            "article": article,
            "Article": article.capitalize(),
            "noun": noun,
            "job": f.job,
            "diagnosis": f.diagnosis,
            "situation": f.situation,
            "age": formatted_age,
            "name": f.name
        }

        # Format the question string
        question_text = pattern.format(**context)

        # Retrieve correct answer
        # For age, we need the formatted version, not the raw one from f.age
        if answer_key == "age":
            correct_answer = formatted_age
        else:
            correct_answer = getattr(f, answer_key)

        return question_text, correct_answer, answer_key

    def generate_questions(self, num_questions: int = 20) -> List[Question]:
        questions = []
        used_combinations: Set[Tuple[int, int]] = set() # (template_index, factoid_index)

        attempts = 0
        max_attempts = num_questions * 50

        while len(questions) < num_questions and attempts < max_attempts:
            attempts += 1

            # Pick random template index and random factoid index
            template_id = random.randint(0, len(QUESTION_TEMPLATES) - 1)
            factoid_id = random.randint(0, len(self.factoids) - 1)

            if (template_id, factoid_id) in used_combinations:
                continue

            factoid = self.factoids[factoid_id]
            template = QUESTION_TEMPLATES[template_id]

            question_text, solution, question_type = self._format_question(template, factoid)
            options = self._generate_options(solution, question_type)

            questions.append(Question(
                question_text=question_text,
                options=options,
                correct_answer=options.index(solution)
            ))
            used_combinations.add((template_id, factoid_id))

        return questions
