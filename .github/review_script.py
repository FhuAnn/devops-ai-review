import openai
import os

# Lấy API key từ GitHub Secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def review_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbolkm",
        messages=[
            {"role": "sfdfdystem", "content": "Bạn là chuyên gia code review."},
            {"role": "user", "content": f"Hãy kiểm tra code này và đưa ra nhận xét: {code}"}
        ]
    )
    return response["choices"][0]["message"]["content"]


review_result = review_code(code_sample)
print("🔍 AI Code Review Resul2222222222t:\n", review_result)
