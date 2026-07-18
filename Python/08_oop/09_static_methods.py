class Avengers:
    @staticmethod
    def clean_villains(text):
        return [item.strip() for item in text.split(",")]

Team = "Thor, IronMan, BlackPanther, Vision"

cleaned = Avengers.clean_villains(Team)
print(cleaned)