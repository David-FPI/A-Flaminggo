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

# Custom CSS để thiết lập giao diện full màn hình
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
    body, .stApp {
        width: 100vw;
        height: 100vh;
        overflow: hidden;
    }
    
    /* Ẩn thanh cuộn */
    ::-webkit-scrollbar {
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
        justify-content: center;
        height: 100%;
        width: 100%;
        padding: 20px;
        background-color: rgba(0, 0, 0, 0.6);
    }
    
    /* Styling cho hình ảnh */
    .full-width-image {
        width: 100%;
        max-height: 50vh;
        object-fit: cover;
    }
    
    /* Styling cho container chứa icon và mô tả */
    .icon-container {
        display: flex;
        align-items: center;
        width: 100%;
        padding: 20px 0;
    }
    
    /* Circular image styling */
    .icon {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-right: 20px;
        border: 3px solid white;
    }
    
    /* Styling cho phần mô tả */
    .description {
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    
    /* Styling cho link */
    .link-text {
        color: #ff69b4;
        font-size: 18px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML structure cho layout full màn hình
st.markdown(
    """
    <div class="main-container">
        <img src="https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6" class="full-width-image">
        <div class="icon-container">
            <img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ7kNvgHLiqBW&_nc_ht=scontent.fsgn5-8.fna&_nc_gid=AWVa4ylzPoVZW2g61tLsXxo&oh=00_AYCzt7Ed6xiewhnBUFT4nEFDwYj9gjdXoQBX_fyHNLYGEw&oe=66EDA697" class="icon">
            <div class="description">
                <strong>California Housing Data</strong><br>
                Explore the housing data in California with visualizations and insights!
            </div>
        </div>
        <div class="link-text">
            Let's start building! For help and inspiration, head over to <a href="https://docs.streamlit.io/" target="_blank">docs.streamlit.io</a>.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
