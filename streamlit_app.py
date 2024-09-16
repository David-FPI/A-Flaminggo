import streamlit as st

# Hình ảnh đầu tiên (giữ nguyên nhưng không có margin)
st.image("https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6")

# Custom CSS to set the galaxy-themed background and full-width layout
st.markdown(
    """
    <style>
    /* Reset Streamlit's default padding */
    .stApp {
        padding: 0;
    }
    
    /* Apply the galaxy image as the background to the whole body */
    body {
        background-image: url('https://img.freepik.com/premium-photo/pastel-clouds-background-pastel-cloud-background-dreamy-clouds-background-pastel-sky-background-ai-generative_703884-13035.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
        margin: 0;
        padding: 0;
    }
    
    /* Ensure that all Streamlit content has proper visibility with some transparency */
    .stApp > header {
        background-color: rgba(0, 0, 0, 0.6);
    }
    
    .stApp > div:has(section) {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
    }
    
    /* Remove any margin or padding between images */
    img {
        margin: 0;
        padding: 0;
        width: 100%;
        height: auto;
    }
    
    /* Make the text stand out with a shadow effect */
    h1 {
        color: #ff69b4; /* Bright pink to match galaxy theme */
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* Style for the container holding image and description */
    .container {
        display: flex;
        align-items: center;
        margin: 0;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 0;
    }
    
    /* Circular image styling */
    .icon {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
        border: 3px solid white;
    }
    
    /* Styling the text next to the image */
    .description {
        font-size: 22px;
        font-weight: bold;
    }
    
    /* Full-width for all elements */
    .stApp > div:has(section) > div {
        width: 100%;
        max-width: none;
        padding: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the image and description in a container
st.markdown(
    """
    <div class="container">
        <img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ7kNvgHLiqBW&_nc_ht=scontent.fsgn5-8.fna&_nc_gid=AWVa4ylzPoVZW2g61tLsXxo&oh=00_AYCzt7Ed6xiewhnBUFT4nEFDwYj9gjdXoQBX_fyHNLYGEw&oe=66EDA697" class="icon">
        <div class="description">
            <strong>California Housing Data</strong><br>
            Explore the housing data in California with visualizations and insights!
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Call to action link
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
