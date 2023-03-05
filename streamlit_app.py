import streamlit
import pandas

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Fvorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥤thie Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')
                
streamlit.header('🍇🍉Build Your own Fruit Smoothie🍎🍍')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the name on the page
streamlit.dataframe(my_fruit_list)

