import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Fvorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥤thie Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')
                
streamlit.header('🍇🍉Build Your own Fruit Smoothie🍎🍍')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the name on the page
streamlit.dataframe(fruits_to_show)



#New section to display FruityVice display response

streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?','Jackfruit')
 if not fruit_choice:
  streamlit.error("Please select a fruit to get information");
 else:
     streamlit.write('The user entered ', fruit_choice)


      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

#Dont run anything past here we troubleshoot
except URLError as e:
streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add the fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('THanks for entering ', fruit_choice)

streamlit.write('Thanks for adding',add_my_fruit);

#this will not work correctly but just go with it for now
my_cur.execute("insert into fruit_load_list values('from streamlit')");
       


