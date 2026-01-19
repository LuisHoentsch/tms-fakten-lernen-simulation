from FactSheet import FactSheet
from questions import QuestionGenerator


def main() -> None:
    fs = FactSheet(5, 3)

    print(
        "Im Folgenden werden Ihnen 15 Patienten vorgestellt, die in fünf Altersgruppen "
        "(Patienten in den 20ern, 30ern, 40ern, 50ern und 60ern) eingeteilt sind. "
        "Zu jedem Patienten werden Ihnen der Name, das Alter, der Beruf, eine Eigenschaft "
        "sowie eine Diagnose genannt. Prägen Sie sich diese Informationen so gut wie möglich ein. "
        "Für das Einprägen haben Sie 6 Minuten Zeit. Während dieser Zeit dürfen Sie keine Notizen machen."
    )
    print()
    print(fs)
    input("Drücken Sie Enter, um fortzufahren...")
    print()
    print("*** Jetzt folgen 60 Minuten andere Aufgaben ***")
    input("Drücken Sie Enter, wenn die Zeit abgelaufen ist...")
    print()
    print(
        "Sie haben vorhin Informationen über 15 Patienten gelernt. "
        "Beantworten Sie nun die folgenden 20 Fragen dazu. "
        "Für die Beantwortung der Fragen haben Sie 7 Minuten Zeit."
    )
    print()

    qg = QuestionGenerator(fs.factoids)
    questions = qg.generate_questions(20)
    solutions = []

    for i, q in enumerate(questions, 1):
        print(f"{i}. {q.question_text}")
        for j, opt in enumerate(q.options):
            print(f"   {["A", "B", "C", "D", "E"][j]})\t{opt}")
        solutions.append(q.correct_answer)
        print()

    print()
    input("Drücken Sie Enter, um die Lösungen anzuzeigen...")
    print()

    for i, s in enumerate(solutions, 1):
        print(f"{i}.\t{["A", "B", "C", "D", "E"][s]}")


if __name__ == "__main__":
    main()
