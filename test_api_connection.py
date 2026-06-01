
import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")

print("=" * 50)
print("API 连接测试")
print("=" * 50)
print(f"API Base: {api_base}")
print(f"API Key: {api_key[:10]}..." if api_key else "API Key: None")
print()

try:
    # 测试 API 连接
    print("正在测试 API 连接...")
    client = OpenAI(
        api_key=api_key,
        base_url=api_base
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=10
    )
    
    print("✅ API 连接成功！")
    print(f"响应: {response.choices[0].message.content}")
    print()
    print("=" * 50)
    
except Exception as e:
    print("❌ API 连接失败！")
    print(f"错误类型: {type(e).__name__}")
    print(f"错误信息: {str(e)}")
    print()
    import traceback
    print("详细堆栈:")
    print(traceback.format_exc())
    print()
    print("=" * 50)

