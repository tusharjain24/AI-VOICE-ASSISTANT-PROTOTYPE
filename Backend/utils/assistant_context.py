class AssistantFnc:
    def __init__(self):
        self.ai_functions = []

    def is_on_topic(self, user_query):
        allowed_keywords = [
            "cosmos", "universe", "space", "Carl Sagan", "planets",
            "stars", "galaxies", "cosmic", "KCET", "science", "astronomy"
        ]
        return any(keyword.lower() in user_query.lower() for keyword in allowed_keywords)

    def ask_question(self, question):
        return question['question']
