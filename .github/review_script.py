import google.generativeai as genai
import os

# Nhập API key từ biến môi trường
API_KEY = os.getenv("GEMINI_API_KEY")  # Lấy API key từ môi trường
if not API_KEY:
    raise ValueError("API key không hợp lệ. Hãy kiểm tra lại GEMINI_API_KEY.")

genai.configure(api_key=API_KEY)

# Hàm gọi Gemini
def review_code(code_sample):
    model = genai.GenerativeModel("gemini-pro")  # Hoặc "gemini-1.5-pro" nếu có quyền
    response = model.generate_content(f"Review code sau:\n{code_sample}")
    return response.text

# Test thử
if __name__ == "__main__":
    code_sample = "def hello():\n    print('Hello, world!')"
    print(review_code(code_sample))
