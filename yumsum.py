import streamlit as st
from PIL import Image

header = st.container()
cuisine, location, results = st.columns(3)

# title
with header:
	st.title('yumsum!')

# text input 
with cuisine:
	cuisine = st.text_input("cuisine")

with location:
	location = st.text_input("location")

with results:
	results = st.number_input("results", value=1, min_value=1, max_value=5)


# generate and reset buttons
generate = st.button("Generate", use_container_width = True)
reset = st.button("Reset", use_container_width = True)

if 'generate' not in st.session_state:
	st.session_state['generate'] = False

if 'reset' not in st.session_state:
	st.session_state['reset'] = False

# reviews

review1 = st.container(border = True)
review2 = st.container(border = True)

## ~~~~~~~~ new stuff ~~~~~~~~~~~

image_urls = ['res1.jpeg', 'res2.jpeg']

# Load images from file paths
images = [Image.open(image_url) for image_url in image_urls]

# Get the current index from session state
current_index = st.session_state.get("current_index", 0)

# Display the current image and the button/arrow image side by side
col1, col2 = st.columns([4, 1])  # Adjust the widths as needed

# Display the current image in the first column


with review1:
	st.write("Tasty Noodle House")

	# st.image('res1.jpeg', use_column_width = "always")
	st.image(images[current_index], use_column_width=True)

	# Create a button/arrow image to advance to the next image in the second column
	if st.button("Next", use_container_width = True):
	    # Increment the current index to move to the next image
	    current_index += 1
	    # Check if the current index exceeds the length of the image list
	    if current_index >= len(images):
	        # Reset the index to 0 to start the slideshow from the beginning
	        current_index = 0
	    # Update the current index in session state
	    st.session_state["current_index"] = current_index
	    
	with st.expander("Review"):
		st.write("Tasty Noodle House, a new addition to Carlsbad, \
			offers authentic and flavorful Chinese cuisine. \
			The expansive menu features dishes like the popular \
			eggplant/mushroom, XLBs, and crab noodle soup, \
			though the wontons were a disappointment. \
			Despite a casual atmosphere and friendly service, \
			some portions are smaller than at other locations, and \
			communication issues have been noted. \
			Overall, Tasty Noodle House provides a solid \
			dining experience with highlights including the \
			pan-fried pork buns, spicy beef chow mein, and \
			Hunan-style lamb.")

with review2:
	st.write("Go for Gourmet!")
	st.image('res2.jpeg', use_column_width = "always")
	with st.expander("Review"):
		st.write("Go for Gourmet offers delicious Gourmet pizza for \
			all of your pizza needs!")















