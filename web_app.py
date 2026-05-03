import streamlit as st
import g4f

st.set_page_config(page_title="大马 AI 文案大师", page_icon="MY")

# 侧边栏配置
with st.sidebar:
    st.title("🚀 工具箱")
    # 让用户选择文案风格
    style = st.selectbox("选择文案风格", ["地道大马风 (Lah/Leh)", "专业商务风", "搞笑幽默风", "深夜感性风"])
    # 选择发布的平台
    platform = st.radio("发布平台", ["小红书 (多 emoji)", "Facebook", "Instagram", "WhatsApp 群发"])
    st.divider()
    st.write("制作人：Vesper")

st.title("🇲🇾 大马地道文案大师")
st.subheader("一键生成最有“味道”的本地推广文案")

topic = st.text_input("你想卖什么产品?", placeholder="例如: 榴莲牙膏, 居家炸鱼饼...")

if st.button("✨ 生成爆款文案"):
    if topic:
        with st.spinner(f"正在为 {platform} 构思 {style} 文案..."):
            try:
                # 提示词进阶：加入了风格和平台限制
                prompt = (
                    f"你是一个大马营销专家。请为'{topic}'写一段文案。"
                    f"要求：1. 使用马来西亚华语加的英文别太刻意。 2. 风格必须是'{style}'。"
                    f"3. 针对'{platform}'的排版特点（比如小红书多加 emoji，Facebook 要有吸引力的第一行）。"
                    f"4. 适当加入地道的助词。"
                )
                
                response = g4f.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                )
                
                st.success("文案已出炉！")
                st.markdown("### 📋 生成结果")
                st.info(response)
                st.balloons()
            except Exception as e:
                st.error(f"AI 走丢了: {e}")
    else:
        st.warning("老板，还没输入产品名称哦！")