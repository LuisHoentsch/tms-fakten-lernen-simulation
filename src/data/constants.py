from src.models.job import Job

NAME_GROUPS = (
    ("Bäcker", "Mahler", "Müller"),
    ("Sanchez", "Gonzales", "Martinez", "Silva"),
    ("Rahim", "Yldirim", "Özdak", "Shahin", "Ogris"),
    ("Althaus", "Hauser", "Neuhaus"),
    ("Rothstein", "Weißer", "Grüning"),
    ("Kreutzer", "Schiffer", "Fährmann"),
)

JOB_GROUPS = (
    (
        Job("Apotheker", "Apothekerin"),
        Job("Hausarzt", "Hausärztin"),
        Job("Hautarzt", "Hautärztin"),
        Job("Kardiologe", "Kardiologin"),
        Job("Neurologe", "Neurologin"),
        Job("Internist", "Internistin"),
        Job("Gastroenterologe", "Gastroenterologin"),
        Job("Augenarzt", "Augenärztin"),
        Job("Optiker", "Optikerin"),
        Job("Zahnarzt", "Zahnärztin"),
    ),
    (
        Job("Stylist", "Stylistin"),
        Job("Friseur", "Friseurin"),
        Job("MakeUp-Artist", "MakeUp-Artist"),
        Job("Designer", "Designerin"),
    ),
    (
        Job("Schreiner", "Schreinerin"),
        Job("Tischler", "Tischlerin"),
        Job("Maler", "Malerin"),
    ),
    (
        Job("Bauarbeiter", "Bauarbeiterin"),
        Job("Architekt", "Architektin"),
        Job("Bauleiter", "Bauleiterin"),
        Job("Klempner", "Klempnerin"),
    ),
    (
        Job("Hausmeister", "Hausmeisterin"),
        Job("Gärtner", "Gärtnerin"),
        Job("Fensterputzer", "Fensterputzerin"),
    ),
    (
        Job("Chemiker", "Chemikerin"),
        Job("Physiker", "Physikerin"),
        Job("Biologe", "Biologin"),
        Job("Mathematiker", "Mathematikerin"),
        Job("Informatiker", "Informatikerin"),
    ),
    (
        Job("Professor", "Professorin"),
        Job("Doktorand", "Doktorandin"),
        Job("HiWi", "HiWi"),
    ),
    (
        Job("CEO", "CEO"),
        Job("Investor", "Investorin"),
        Job("Manager", "Managerin"),
        Job("Personalchef", "Personalchefin"),
        Job("Filialleiter", "Filialleiterin"),
    ),
)

AGES = tuple(str(age) for age in (20, 30, 40, 50, 60, 70))

DIAGNOSES = (
    "Erkältung",
    "Mandelentzündung",
    "Cholera",
    "Gürtelrose",
    "Blutvergiftung",
    "Myokarditis",
    "Sehnenriss",
    "Armbruch",
    "Kieferbruch",
    "Mittelhandbruch",
    "Lungenentzündung",
    "Thrombose",
    "Embolie",
    "Herzinfarkt",
    "Migräne",
    "Ausschlag",
    "Husten",
    "Bandscheibenvorfall",
    "Durchfall",
    "Verstopfung",
    "Gallensteine",
    "Nierensteine",
    "Hepatitis",
    "HIV",
    "Zahnschmerzen",
    "Myalgie",
    "Schlaganfall",
)

SITUATIONS = (
    "in Ambulanz",
    "in Notaufnahme",
    "Notfall",
    "im Krankenwagen",
    "in Intensivstation",
    "in ReHa",
    "in Radiologie",
    "in OP",
    "fröhlich",
    "ehrgeizig",
    "nett",
    "ernst",
    "streng",
    "empfindlich",
    "kritisch",
    "uneinsichtig",
    "verwirrt",
    "unfreundlich",
    "zielstrebig",
    "egoistisch",
    "hilfsbereit",
    "verheiratet",
    "geschieden",
)

# Template structure: (Pattern, Answer Key)
# Placeholders: {article}, {Article}, {noun}, {job}, {diagnosis}, {situation}, {age}
QUESTION_TEMPLATES = (
    (
        "Wie heißt {article} {noun} mit {diagnosis}?",
        "name"
    ),
    (
        "Wie heißt {article} {job}?",
        "name"
    ),
    (
        "{Article} {noun} mit {diagnosis} ist?",
        "job"
    ),
    (
        "Welchen Beruf hat {article} {noun}, {article} {situation} ist?",
        "job"
    ),
    (
        "{Article} {noun} mit {diagnosis} ist?",
        "situation"
    ),
    (
        "{Article} {job} ist?",
        "situation"
    ),
    (
        "Welche Diagnose hat {article} {job}?",
        "diagnosis"
    ),
    (
        "Welche Diagnose hat {article} {noun}, {article} {situation} ist?",
        "diagnosis"
    ),
    (
        "Wie alt ist {article} {noun} mit {diagnosis}?",
        "age"
    ),
    (
        "Wie alt ist {article} {noun}, {article} {situation} ist?",
        "age"
    ),
)
