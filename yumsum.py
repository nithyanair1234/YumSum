import streamlit as st
from PIL import Image

def clear_form():
	st.session_state["cuisine"] = ""
	st.session_state["location"] = ""
	st.session_state["results"] = 1

def callback():
	show_review = True


header = st.container()
cuisine, location, results = st.columns(3)

# title
with header:
	st.title('yumsum!')

# text input 
with cuisine:
	cuisine = st.text_input("cuisine", key="cuisine")

with location:
	location = st.text_input("location", key="location")

with results:
	results = st.number_input("results", min_value=1, max_value=5, key= "results")


# generate and reset buttons
if "show_review" not in st.session_state:
	st.session_state.show_review = False

generate = st.button("Generate", use_container_width = True, on_click = callback)
reset = st.button("Reset", use_container_width = True, on_click = clear_form)


# reviews
review1 = st.container(border = True)
review2 = st.container(border = True)
review3 = st.container(border = True)
review4 = st.container(border = True)
review5 = st.container(border = True)

arr = [review1, review2, review3, review4, review5]

# if generate is pressed
if generate or st.session_state.show_review:
	for i in range(0, results):
		with arr[i]:
			st.write("Tasty Noodle House")
			st.image('res1.jpeg', use_column_width = "always")
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
	

















