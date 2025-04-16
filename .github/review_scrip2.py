def review_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-4-turdbo32SDSDSDSD3",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia code review."},
            {"role": "user", "content": f"Hãy kiểm tra code này và đưa ra nhận xét: {code}"}
        ]
    )
    return response["choices"][0]["message"]["content"]