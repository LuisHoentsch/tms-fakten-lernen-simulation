from FactSheet import FactSheet


def main():
    fs = FactSheet(5, 3)

    print(
        "Im Folgenden werden Ihnen 15 Patienten vorgestellt, die in fünf Altersgruppen (Patienten in den 20ern, 30ern, 40ern, 50ern und 60ern) eingeteilt sind. Zu jedem Patienten werden Ihnen der Name, das Alter, der Beruf, eine Eigenschaft sowie eine Diagnose genannt. Prägen Sie sich diese Informationen so gut wie möglich ein. Für das Einprägen haben Sie 6 Minuten Zeit. Während dieser Zeit dürfen Sie keine Notizen machen."
    )
    print()
    print(fs)
    input()
    print("*** Jetzt folgen 60 Minuten andere Aufgaben ***")
    input()
    print(
        "Sie haben vorhin Informationen über 15 Patienten gelernt. Beantworten Sie nun die folgenden 20 Fragen dazu. Für die Beantwortung der Fragen haben Sie 7 Minuten Zeit."
    )
    print()
    print("TODO: Fragen generieren")


if __name__ == "__main__":
    main()
