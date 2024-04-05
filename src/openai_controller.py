from openai import OpenAI



class openai_controller:
    def __init__(self, OPENAI_API_KEY):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
    def chat(self, prompt):
        completion = self.client.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "response by Traditional Chinese"},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content


