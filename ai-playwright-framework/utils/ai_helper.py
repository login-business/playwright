from openai import OpenAI

client = OpenAI()

def generate_test_cases(feature):

    prompt = f"Write test cases for {feature} in simple points"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content