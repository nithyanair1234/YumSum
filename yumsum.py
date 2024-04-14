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

pic1, pic2 = st.columns(2)
pic3, pic4, pic5 = st.columns(3)

if done:
	with pic1:
		st.image('res1.jpeg', caption = "restaurant 1")
		st.write('"Grandma loved the food so much she told me she was proud of me! That never happens!"')

	with pic2:
		st.image('res1.jpeg', caption = "restaurant 2")
		st.write('"Very yummy. Invited my alien friends to partake in this meal."')

	with pic3:
		st.image('res1.jpeg', caption = "restaurant 3")
		st.write('"Talking seafood run this restaurant. Are you telling me a shrimp fried this rice?"')

	with pic4:
		st.image('res1.jpeg', caption = "restaurant 4")
		st.write('"This food is bussing on god fr"')

	with pic5:
		st.image('res1.jpeg', caption = "restaurant 5")
		st.write('"If you see bug in your food, just treat it like extra protein!!!!"')
