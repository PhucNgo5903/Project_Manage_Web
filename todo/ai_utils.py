import google.generativeai as genai
from local_settings import API_KEY

# Cấu hình API với khóa API của bạn
genai.configure(api_key=API_KEY)

# Tạo một đối tượng model từ Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

def summarize_text(paragraph):
    PROMPT = f"""
    If there is not enough information, Please say I dont have enough information, else explain what is
    "{paragraph}"
    
    in 2 sentences
    """
    
    # Gọi API để tóm tắt văn bản
    response = model.generate_content(PROMPT)
    
    # Trả về kết quả tóm tắt
    return response.text.strip()