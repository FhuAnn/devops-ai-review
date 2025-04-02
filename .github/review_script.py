import openai
import os

# Lấy API key từ GitHub Secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def review_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia code review."},
            {"role": "user", "content": f"Hãy kiểm tra code này và đưa ra nhận xét: {code}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Ví dụ review code
code_sample = """
def add(a, b):
return a + b  # Lỗi thụt lề
"""


"tôi là ai"

review_result = review_code(code_sample)
print("🔍 AI Code Review Resul2222222222t:\n", review_result)
