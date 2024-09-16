import streamlit as st

# Title of the app
st.title("🎈 A-Flamingo Club")

# Custom CSS to set a galaxy-themed background with pink highlights
st.markdown(
    """
    <style>
    /* Set the background image for the entire page */
    body {
        background-image: url('https://images.unsplash.com/photo-1568223288053-3cf3f6e915f3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1740&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    /* Ensure that the main content area also uses the same background */
    .stApp {
        background-color: rgba(0, 0, 0, 0.5); /* Add slight transparency for contrast */
    }

    /* Styling for the container holding image and description */
    .container {
        display: flex;
        align-items: center;
        margin-top: 50px;
        background-color: rgba(255, 255, 255, 0.1); /* Slight white transparent background for container */
        padding: 20px;
        border-radius: 15px;
    }

    /* Styling for the circular image */
    .icon {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
        border: 3px solid white;
    }

    /* Styling for the text description */
    .description {
        font-size: 22px;
        font-weight: bold;
    }

    /* Style the title to stand out */
    h1 {
        color: #ff69b4; /* Bright pink to match galaxy theme */
        text-shadow: 2px 2px 4px #000000;
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
