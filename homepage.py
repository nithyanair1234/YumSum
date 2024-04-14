import streamlit as st
from PIL import Image



st.set_page_config(
    page_title="Multipage App",
    page_icon= "hello",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")



def scroll_to_bottom():
    # Inject JavaScript code to scroll to the bottom of the page
    st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

# Add a button to trigger the scroll
if st.button("Scroll to Bottom"):
    scroll_to_bottom()


    

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)



#####scrolling through images####

# Define a list of image paths or URLs
image_urls = ['drinks.jpeg', 'food.jpeg', 'yelp.jpeg']

# Load images from file paths
images = [Image.open(image_url) for image_url in image_urls]

# Get the current index from session state
current_index = st.session_state.get("current_index", 0)

# Display the current image and the button/arrow image side by side
col1, col2 = st.columns([4, 1])  # Adjust the widths as needed

# Display the current image in the first column
col1.image(images[current_index], caption="Image", use_column_width=True)

# Create a button/arrow image to advance to the next image in the second column
if col2.button("Next"):
    # Increment the current index to move to the next image
    current_index += 1
    # Check if the current index exceeds the length of the image list
    if current_index >= len(images):
        # Reset the index to 0 to start the slideshow from the beginning
        current_index = 0
    # Update the current index in session state
    st.session_state["current_index"] = current_index

