import g4f

def start_ai():
    print("\n--- 马来西亚 AI 文案工具 (免费版) ---")
    topic = input("你想卖什么产品? (例如: Nasi Lemak): ")
    
    prompt = f"你是一个大马营销专家，请为'{topic}'写一段地道的社交媒体文案，用一点点 lah, leh。"

    try:
        print("\n⏳ 正在呼叫 AI，请稍等...")
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        print("\n✨ 生成结果如下：\n")
        print(response)
    except Exception as e:
        print(f"\n❌ 错误: {e}")

if __name__ == "__main__":
    start_ai()