import google.generativeai as genai

# Nhập API key của bạn
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Hàm gọi Gemini
def review_code(code_sample):
    model = genai.GenerativeModel("gemini-pro")  # Hoặc "gemini-1.5-pro" nếu có quyền
    response = model.generate_content(f"Review code sau: {code_sample}")
    return response.text

# Test thử
if __name__ == "__main__":
    code_sample = "def hello():\n    print('Hello, world!')"
    print(review_code(code_sample))
