import os
from openai import OpenAI

# Lấy API key từ GitHub Secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)  # Khởi tạo client

def review_code(code):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia code review."},
            {"role": "user", "content": f"Hãy kiểm tra code này và đưa ra nhận xét: {code}"}
        ]
    )
    return response.choices[0].message.content  # Truy xuất nội dung phản hồi

# Ví dụ review code
code_sample = """
def add(a, b):
return a + b  # Lỗi thụt lề
"""

review_result = review_code(code_sample)
print("🔍 AI Code Review Result:\n", review_result)
