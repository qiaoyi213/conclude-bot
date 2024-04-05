from openai import OpenAI



class openai_controller:
    def __init__(self, OPENAI_API_KEY):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def chat(self, prompt):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "response by Traditional Chinese"},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def conclude(self, message):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "想像你現在是一個對話總結人員，請閱讀下列對話並進行重點總結，請注意並不是每個人說的話都有重點，請以繁體中文(Traditional Chinese)回答"},
                {"role": "user", "content": message}
            ]
        )

        return completion.choices[0].message.content

