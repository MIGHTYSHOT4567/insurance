import streamlit as st
import numpy as np
import joblib
from predict_cost import predict

st.set_page_config(page_title="Insurance App", page_icon = ":house_with_garden:")


st.write('# <span style = "color: blue; text-align: center;">Insurance App.</span>',unsafe_allow_html = True)
st.write('### <span style = "color: lightgreen;">Fill in the details below to get an estimate of the price of your Insurance</span>',unsafe_allow_html = True)
st.write('___')

st.header('Age')
Age = st.slider('Select the area of the house (in sq. ft.)', 0, 100, 30)

st.header('Country')
Country = st.selectbox('Select the town/city where the house is located',("Canada", "Nigeria", "USA"))
if Country == "Canada":
	country_values = (1, 0)
	st.image("Canada flag.png",caption = "" , width = 150 , use_column_width = False)

elif Country == "Nigeria":
	country_values = (0,1)
	st.image("Niger flag.png",caption = "" , width = 150 , use_column_width = False)

elif  Country == 'USA':
	country_values = (0,0)
	st.image("USA flag.png",caption = "" , width = 150 , use_column_width = False)





st.header('Salary')
Salary = st.number_input('Enter your salary earned in years (highest $50,000)', min_value=10, step=1000)
st.image("1 dollar.jpg",caption = "" , width = 150 , use_column_width = False)



input_data = np.array([[Age, Salary] + list(country_values)])


if st.button('Predict Insurance Purchase'):
	cost = predict(input_data)
	st.subheader('Purchase Insurance')
	#st.write(cost[0])
	if cost[0] == 1:
		st.write("Purchase Insurance.")
		st.image("insurance.png",caption = "" , width = 150 , use_column_width = False)
	else:
		st.write("Insurance was not purchased")
		st.image("No insurance.jfif",caption = "" , width = 150 , use_column_width = False)