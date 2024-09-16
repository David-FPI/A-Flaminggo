import streamlit as st

# Set the title for the app
st.title("🎈 A-Flamingo Club")

# Custom CSS to set the galaxy-themed background
st.markdown(
    """
    <style>
    /* Apply the galaxy image as the background to the whole body */
    body {
        background-image: url('https://thepositiveedge.net/wp-content/uploads/2017/10/Nebula-flipped-e1524510729796.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    /* Ensure that all Streamlit content has proper visibility with some transparency */
    .stApp {
        background-color: rgba(0, 0, 0, 0.6); /* Transparent dark overlay for content visibility */
        padding: 20px;
        border-radius: 15px;
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
        margin-top: 50px;
        background-color: rgba(255, 255, 255, 0.1); /* Slight white transparent background for container */
        padding: 20px;
        border-radius: 15px;
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
