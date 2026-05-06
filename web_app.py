import streamlit as st
import g4f

# --- 1. 页面整体设置 ---
st.set_page_config(page_title="MY 大马地道文案大师", page_icon="🚀")

# --- 2. 侧边栏：工具箱与变现引流 ---
with st.sidebar:
    st.markdown("###  工具箱")
    style = st.selectbox("选择文案风格", ["地道大马风 (Lah/Leh)", "专业商务风", "幽默搞笑风"])
    platform = st.radio("发布平台", ["小红书 (多 emoji)", "Facebook", "Instagram", "WhatsApp 群发"])
    
    st.markdown("---")
    st.markdown("### 👨‍💻 关于制作人")
    st.write("我是 **Vesper**，专注于本地 AI 工具开发。")
    
    # 变现测试点 1：广告位
    st.info("📢 **广告位招租**\n\n你的产品想出现在这里吗？联系我获取每月流量报价。")
    st.write("如有技术合作需求，请联系我。")

# --- 3. 主页面 UI ---
st.title("MY 大马地道文案大师")
st.markdown("### 一键生成最有“味道”的本地推广文案")

topic = st.text_input("你想卖什么产品？", placeholder="例如：榴莲牙膏, 居家炸鱼饼...")

# --- 4. 核心逻辑与变现功能 ---
if st.button("✨ 生成爆款文案"):
    if topic:
        with st.spinner(f"正在为 {platform} 构思 {style} 文案..."):
            try:
                # 准备提示词
                prompt = (
                    f"你是一个大马营销专家。请为'{topic}'写一段文案。"
                    f"要求：1. 使用马来西亚华语加英文别太刻意。 2. 风格必须是'{style}'。"
                    f"3. 针对'{platform}'的排版特点。 4. 适当加入地道的助词。"
                )
                
                # 调用 AI 生成
                response = g4f.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                )
                
                # --- 5. 结果展示区 ---
                st.success("文案已出炉！")
                st.markdown("### 📋 生成结果")
                st.info(response)
                st.balloons()  # 撒花特效
                
                # --- 6. 变现测试点 2：高价值定制服务 ---
                # 注意：这段代码被放在了 try 里面，确保只有成功生成文案后才会显示！
                st.markdown("---")
                st.subheader("🚀 想要更地道、转化率更高的文案？")
                st.write("基础版 AI 生成仅供参考，我提供 **RM 30/篇** 的深度人工校对与排版服务。")
                
                # WhatsApp 链接优化：去掉了0，加上了马来西亚区号 60，这样直接点击才能跳转！
                whatsapp_link = "https://wa.me/601112192661?text=你好Vesper，我从文案大师网站过来，想咨询文案定制服务。"
                st.link_button("📱 点击 WhatsApp 直接联系我", whatsapp_link)
                
            except Exception as e:
                st.error(f"AI 走丢了: {e}")
    else:
        st.warning("老板，还没输入产品名称哦！")