import streamlit as st

# Ẩn main menu và footer của Streamlit
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS để thiết lập giao diện full màn hình không có khoảng trống
st.markdown(
    """
    <style>
    /* Reset toàn bộ margin và padding */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Thiết lập body và .stApp để full màn hình */
    body, .stApp, .element-container, .css-1d391kg, .css-1v3fvcr, .css-dm3055, .css-1q1n0ol {
        width: 100vw !important;
        max-width: 100vw !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow-x: hidden !important;
    }
    
    /* Ẩn thanh cuộn ngang */
    body::-webkit-scrollbar {
        display: none;
    }
    
    /* Thiết lập background */
    .stApp {
        background-image: url('https://img.freepik.com/premium-photo/pastel-clouds-background-pastel-cloud-background-dreamy-clouds-background-pastel-sky-background-ai-generative_703884-13035.jpg');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
    }
    
    /* Styling cho container chính */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        min-height: 100vh;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.6);
    }
    
    /* Styling cho hình ảnh */
    .full-width-image {
        width: 100%;
        height: auto;
        object-fit: cover;
    }
    
    /* Styling cho container chứa icon và mô tả */
    .icon-container {
        display: flex;
        align-items: flex-start;
        width: 100%;
        padding: 20px;
    }
    
    /* Circular image styling */
    .icon {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-right: 20px;
        border: 3px solid white;
        flex-shrink: 0;
    }
    
    /* Styling cho phần mô tả */
    .description {
        color: white;
        font-size: 16px;
        display: flex;
        flex-direction: column;
    }
    
    /* Styling cho tiêu đề */
    .title {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #ff69b4;
        display: flex;
        align-items: center;
    }
    
    /* Styling cho icon hồng hạc */
    .flamingo-icon {
        width: 40px;
        height: 40px;
        margin-right: 10px;
        fill: #ff69b4;
    }
    
    /* Styling cho caption */
    .caption {
        font-size: 14px;
        line-height: 1.5;
    }
    
    /* Styling cho link */
    .link-text {
        color: #ff69b4;
        font-size: 18px;
        margin-top: 20px;
        padding: 0 20px;
        text-align: center;
    }

.slogan {
    font-family: 'Montserrat', sans-serif;
    font-size: 12px;
    font-weight: bold;
    color: #fff;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    animation: fadeIn 1s ease-in-out;
    letter-spacing: 2px;
    margin-bottom: 40px;
}
    
    </style>
    """,
    unsafe_allow_html=True
)

# HTML structure cho layout full màn hình với tiêu đề nổi bật và caption, bao gồm icon con hạc
st.markdown(
    """
    <div class="main-container">
        <img src="https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6" class="full-width-image">
        <div class="icon-container">
            <img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ7kNvgHLiqBW&_nc_ht=scontent.fsgn5-8.fna&_nc_gid=AWVa4ylzPoVZW2g61tLsXxo&oh=00_AYCzt7Ed6xiewhnBUFT4nEFDwYj9gjdXoQBX_fyHNLYGEw&oe=66EDA697" class="icon">
            <div class="description">
                <div class="title">
  <img src="https://cdn-icons-png.flaticon.com/128/3807/3807146.png" alt="Icon flamingo" width="40" height="40" style="margin-right: 10px;">
                A-Flamingo Club
                </div>
                <div class="caption">
                    Câu lạc bộ âm nhạc A-Flamingo là nơi hội tụ của những tâm hồn yêu thích âm nhạc tại Trường Cao đẳng Anh Quốc BTEC FPT Hồ Chí Minh. Chúng tôi tự hào là một cộng đồng năng động và sáng tạo, nơi các thành viên có cơ hội thể hiện niềm đam mê âm nhạc của mình thông qua các buổi biểu diễn, workshop và các hoạt động giao lưu âm nhạc. A-Flamingo không chỉ
                    là nơi luyện tập kỹ năng âm nhạc mà còn là môi trường lý tưởng để các bạn trẻ phát triển khả năng làm việc nhóm, sáng tạo và kết nối với những người có cùng sở thích. Hãy gia nhập chúng tôi để cùng nhau tạo nên những bản nhạc tuyệt vời và những kỷ niệm đáng nhớ.
                </div>
                            <div class="slogan">
                A-Flamingo _ Kết nối đam mê _Tỏa sáng âm nhạc
            </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

