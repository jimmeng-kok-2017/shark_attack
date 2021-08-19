import streamlit as st
import sklearn
import pickle
import numpy as np
import pandas as pd

rf_model = pickle.load(open('rf_model.pkl', 'rb'))

df = pd.read_csv('shark_attacks.csv')

st.title("Would You Survive A Shark Attack?")
st.image('gerald-schombs-GBDkr3k96DE-unsplash.jpg')
'''
No matter what, you would face a shark attack. The question is would you survive or would you not?
'''
'''
*Top Photo by Gerald Schömbs on Unsplash*
'''
st.sidebar.write("Machine Learning is applied in this app!")
st.sidebar.write("It uses a Random Forest Classification model trained with Kaggle's Shark attack dataset. "
                 "The model uses the latest 10 years worth of the data (2008 to 2018 inclusive). "
                 "This model was correct about 88% of the time when it came to predicting whether a person would survive a shark attack as he/she would face it.")
st.sidebar.write("Have fun using this app to check your risk!")
st.sidebar.subheader("Jim Meng Kok")
st.sidebar.markdown(
    'Please feel free to connect with me on LinkedIn: [www.linkedin.com/in/jimmengkok](www.linkedin.com/in/jimmengkok)')
st.sidebar.markdown('Medium: [https://medium.com/@jimintheworld](https://medium.com/@jimintheworld)')

places = sorted(df['Destination'].unique())
years = sorted(df['Year'].unique())
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] # sorted(df['Month'].unique()) # haven't sort by month names as this is in alphabetical order
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] # sorted(df['Day'].unique()) # haven't sort by days names as this is in alphabetical order
times = ["Morning","Afternoon","Evening","Night","Midnight"] # sorted(df['Time'].unique())
activities = sorted(df['Activity'].unique())

# Age
age = st.number_input("What is your age?", value=1, step=1)

# Gender
st.text("Please choose your gender:")
col1, col2, col3 = st.beta_columns(3)
with col1:
    male = st.checkbox('M')
with col2:
    female = st.checkbox('F')

# Place
destination = st.selectbox("Where would you prefer to visit?", options=places)

# Year
year_st = st.selectbox("Select the Year you preferred to travel in the past", options=years)

# Month
month_st = st.selectbox("Choose the Month you preferred to travel in the past", options = months)

# Day
day_st = st.selectbox("Choose the Day you preferred to travel in the past", options = days)

# Time of the Day
time_st = st.selectbox("Choose the Time of the Day you preferred to travel in the past", options = times)

# Activity
activity_st = st.selectbox("Select your preferred Activity at the beach", options = activities)

# Create functions for the encoding and stuffs
def check_activity(response):
    if response == 'Body boarding':
        return 0
    if response == 'Body surfing':
        return 1
    if response == 'Boogie boarding':
        return 2
    if response == 'Feeding':
        return 3
    if response == 'Fishing':
        return 4
    if response == 'Floating':
        return 5
    if response == 'Jet skiing':
        return 6
    if response == 'Kayak fishing':
        return 7
    if response == 'Kayaking':
        return 8
    if response == 'Kite boarding':
        return 9
    if response == 'Kite surfing':
        return 10
    if response == 'Kneeling':
        return 11
    if response == 'Measuring sharks':
        return 12
    if response == 'Night bathing':
        return 13
    if response == 'Paddle boarding':
        return 14
    if response == 'Paddle-skiing':
        return 15
    if response == 'Paddling':
        return 16
    if response == 'Photographing fish':
        return 17
    if response == 'Playing':
        return 18
    if response == 'Rescuing':
        return 19
    if response == 'Rowing':
        return 20
    if response == 'Scuba diving':
        return 21
    if response == 'Sitting':
        return 22
    if response == 'Skimboarding':
        return 23
    if response == 'Snorkeling':
        return 24
    if response == 'Spearfishing':
        return 25
    if response == 'Stand-Up Paddleboarding':
        return 26
    if response == 'Stand-Up Paddleboarding Foil boarding':
        return 27
    if response == 'Standing':
        return 28
    if response == 'Surf fishing':
        return 29
    if response == 'Surf skiing':
        return 30
    if response == 'Surfing':
        return 31
    if response == 'Swimming':
        return 32
    if response == 'Treading water':
        return 33
    if response == 'Wading':
        return 34
    if response == 'Wakeboarding':
        return 35
    if response == 'Walking':
        return 36
    if response == 'Windsurfing':
        return 37

def sex_decider(male: object) -> object:
    if male:
        return 1
    else:
        return 0

def check_time(response):
    if response == 'Afternoon':
        return 0
    if response == 'Evening':
        return 1
    if response == 'Midnight':
        return 2
    if response == 'Morning':
        return 3
    if response == 'Night':
        return 4

def check_day(response):
    if response == 'Friday':
        return 0
    if response == 'Monday':
        return 1
    if response == 'Saturday':
        return 2
    if response == 'Sunday':
        return 3
    if response == 'Thursday':
        return 4
    if response == 'Tuesday':
        return 5
    if response == 'Wednesday':
        return 6

def check_month(response):
    if response == 'April':
        return 0
    if response == 'August':
        return 1
    if response == 'December':
        return 2
    if response == 'February':
        return 3
    if response == 'January':
        return 4
    if response == 'July':
        return 5
    if response == 'June':
        return 6
    if response == 'March':
        return 7
    if response == 'May':
        return 8
    if response == 'November':
        return 9
    if response == 'October':
        return 10
    if response == 'September':
        return 11

def dep_dest(response):
    if response == 'Abaco Islands, BAHAMAS':
        return 0
    if response == 'Alabama, USA':
        return 1
    if response == 'Alicante Province, SPAIN':
        return 2
    if response == 'Alifu Alifu Atoll, MALDIVES':
        return 3
    if response == 'Antsiranana Province, MADAGASCAR':
        return 4
    if response == 'Ascension Island, ST HELENA, British overseas territory':
        return 5
    if response == 'Atsumi peninsula, JAPAN':
        return 6
    if response == 'Baie de Sainte-Marie, NEW CALEDONIA':
        return 7
    if response == 'Baja California Sur, MEXICO':
        return 8
    if response == 'Bali, INDONESIA':
        return 9
    if response == 'Batangas province, PHILIPPINES':
        return 10
    if response == 'Bay of Biscay, FRANCE':
        return 11
    if response == 'Binh Dinh Province, VIETNAM':
        return 12
    if response == 'Bocas, PANAMA':
        return 13
    if response == 'Bois-Blanc, REUNION':
        return 14
    if response == 'Bora Bora, FRENCH POLYNESIA':
        return 15
    if response == 'California, USA':
        return 16
    if response == 'Central Province, PAPUA NEW GUINEA':
        return 17
    if response == 'Cocos Island, COSTA RICA':
        return 18
    if response == 'Cornwall, ENGLAND':
        return 19
    if response == 'Delaware, USA':
        return 20
    if response == 'Devon, UNITED KINGDOM':
        return 21
    if response == 'Dubai, UNITED ARAB EMIRATES (UAE)':
        return 22
    if response == 'Eastern Cape Province, SOUTH AFRICA':
        return 23
    if response == 'Exuma Islands, BAHAMAS':
        return 24
    if response == 'Fernando de Noronha, BRAZIL':
        return 25
    if response == 'Fife, SCOTLAND':
        return 26
    if response == 'Florida, USA':
        return 27
    if response == 'Galapagos Islands, ECUADOR':
        return 28
    if response == 'Georgia, USA':
        return 29
    if response == 'Grand Bahama Island, BAHAMAS':
        return 30
    if response == 'Grand Canary Island, SPAIN':
        return 31
    if response == 'Grand Terre, NEW CALEDONIA':
        return 32
    if response == 'Guanacaste, COSTA RICA':
        return 33
    if response == 'Guantanamo Province, CUBA':
        return 34
    if response == 'Guerrero, MEXICO':
        return 35
    if response == "Ha'api, TONGA":
        return 36
    if response == 'Hawaii, USA':
        return 37
    if response == 'Holquin Province, CUBA':
        return 38
    if response == 'Ibiza Island, SPAIN':
        return 39
    if response == 'Inhambane Province, MOZAMBIQUE':
        return 40
    if response == 'Isla Provedencia, COLUMBIA':
        return 41
    if response == 'Jeju Province, SOUTH KOREA':
        return 42
    if response == 'Kochi Prefecture, JAPAN':
        return 43
    if response == 'KwaZulu-Natal, SOUTH AFRICA':
        return 44
    if response == 'Le Port, REUNION':
        return 45
    if response == 'Louisiana, USA':
        return 46
    if response == 'Loyalty Islands, NEW CALEDONIA':
        return 47
    if response == 'Luzon, PHILIPPINES':
        return 48
    if response == 'Maine, USA':
        return 49
    if response == 'Maputo Province, MOZAMBIQUE':
        return 50
    if response == 'Massachusetts, USA':
        return 51
    if response == 'Middle Caicos, TURKS & CAICOS':
        return 52
    if response == 'New Jersey, USA':
        return 53
    if response == 'New Providence, BAHAMAS':
        return 54
    if response == 'New South Wales, AUSTRALIA':
        return 55
    if response == 'New York, USA':
        return 56
    if response == 'North Carolina, USA':
        return 57
    if response == 'North Island, NEW ZEALAND':
        return 58
    if response == 'North Province, NEW CALEDONIA':
        return 59
    if response == 'North Region, GUAM':
        return 60
    if response == 'Northern Bahamas, BAHAMAS':
        return 61
    if response == 'Northern Territory, AUSTRALIA':
        return 62
    if response == 'Off Green Island, TAIWAN':
        return 63
    if response == 'Off Vanua Levu, FIJI':
        return 64
    if response == 'Oregon, USA':
        return 65
    if response == 'Palmyra Atoll, USA':
        return 66
    if response == 'Pernambuco, BRAZIL':
        return 67
    if response == 'Phuket, THAILAND':
        return 68
    if response == 'Praslin, SEYCHELLES':
        return 69
    if response == 'Puerto Rico, USA':
        return 70
    if response == 'Queensland, AUSTRALIA':
        return 71
    if response == 'Quintana Roo, MEXICO':
        return 72
    if response == 'Rangiroa, FRENCH POLYNESIA':
        return 73
    if response == 'Saint-Andre, REUNION':
        return 74
    if response == 'Saint-Benoit, REUNION':
        return 75
    if response == 'Saint-Gilles, REUNION':
        return 76
    if response == 'Saint-Leu, REUNION':
        return 77
    if response == 'Saint-Paul, REUNION':
        return 78
    if response == 'Santa Cruz Island, ECUADOR':
        return 79
    if response == 'Santa Elena, ECUADOR':
        return 80
    if response == 'Sharjah, UNITED ARAB EMIRATES':
        return 81
    if response == 'Shizuoka Prefecture, JAPAN':
        return 82
    if response == 'Sinai Peninsula, EGYPT':
        return 83
    if response == 'Sinaloa, MEXICO':
        return 84
    if response == 'Society Islands, FRENCH POLYNESIA':
        return 85
    if response == 'South Australia, AUSTRALIA':
        return 86
    if response == 'South Carolina, USA':
        return 87
    if response == 'South Island, NEW ZEALAND':
        return 88
    if response == 'South Province, NEW CALEDONIA':
        return 89
    if response == 'South Sinai Peninsula, EGYPT':
        return 90
    if response == 'Southern District, ISRAEL':
        return 91
    if response == 'Split-Dalmatia Count, CROATIA':
        return 92
    if response == 'St. Catherine, JAMAICA':
        return 93
    if response == 'St. Johns Reef, EGYPT':
        return 94
    if response == 'Sucre, COLUMBIA':
        return 95
    if response == 'Suez, EGYPT':
        return 96
    if response == 'Tasmania, AUSTRALIA':
        return 97
    if response == 'Telyakovsky Bay, Khasan,  Primorsky Krai (Far East), RUSSIA':
        return 98
    if response == 'Texas, USA':
        return 99
    if response == 'Trois-Bassins, REUNION':
        return 100
    if response == 'Tuamotus, FRENCH POLYNESIA':
        return 101
    if response == 'US Virgin Islands, USA':
        return 102
    if response == 'Vanua Levu, Fiji':
        return 103
    if response == 'Victoria, AUSTRALIA':
        return 104
    if response == 'Virginia, USA':
        return 105
    if response == 'Vitu Levu, FIJI':
        return 106
    if response == 'West End, BAHAMAS':
        return 107
    if response == 'Western Australia, AUSTRALIA':
        return 108
    if response == 'Western Cape Province, SOUTH AFRICA':
        return 109
    if response == 'Western Province, SOUTH AFRICA':
        return 110
    if response == 'Yasawa Islands, FIJI':
        return 111
    if response == 'd’Étang-Salé, REUNION':
        return 112

# Click button
if st.button("Click to discover your fate"):
    fate_list = [year_st, check_activity(activity_st), sex_decider(male), age, check_time(time_st), check_day(day_st), check_month(month_st), dep_dest(destination)]
    prediction = rf_model.predict([fate_list])

    if prediction == np.array([0]):
        st.image('survived.png', use_column_width=True)
        st.write("You would definitely injured but, fortunately, you would have survived the shark attack! King Shark would have spared you!")

    if prediction == np.array([1]):
        st.image('fatal.png', use_column_width=True)
        st.write("I am sorry, you would have been killed by the shark whose name is Bruce.")