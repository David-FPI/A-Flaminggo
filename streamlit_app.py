import streamlit as st

st.image("https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6")
# Title of the app
st.title("🎈 A-Flamingo Club")

# Custom CSS to make the image circular and align the image and description side by side
st.markdown(
    """
    <style>
    .container {
        display: flex;
        align-items: center;
    }
    .icon {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
    }
    .description {
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display image and description using HTML for layout
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
