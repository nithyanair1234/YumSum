import streamlit as st

header = st.container()
cuisine, location, results = st.columns(3)

with header:
	st.title('yumsum!')

with cuisine:
	cuisine = st.text_input("cuisine")

with location:
	location = st.text_input("location")

with results:
	results = st.number_input("results", value=1, min_value=1, max_value=5)

done = st.button("Done", use_container_width = True)
reset = st.button("Reset", use_container_width = True)

if done:
	st.write("You wanted ", cuisine, " from ", location)