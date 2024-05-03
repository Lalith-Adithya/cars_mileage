import streamlit as st
import pandas as pd
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

st.set_page_config(layout="wide",page_title="GAS MILEAGE",initial_sidebar_state="expanded",page_icon="🚗",)

def set_bg_animation(animation_url):
  page_bg_img = f'''
  <style>
      .stApp {{
          background-image: url("{animation_url}");
          background-size: cover;
          background-position: center center;
          margin: 0;
          padding: 0;
          height: 100vh;
          animation: animate 10s linear infinite;
      }}
      @keyframes animate {{
          from {{ background-position: 0% 0%; }}
          to {{ background-position: 100% 0%; }}
      }}
  </style>
  '''
  st.markdown(page_bg_img, unsafe_allow_html=True)

# Backgroung Gif
animation_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG9paG16aXRyNW12czlodmJkeHRkY241a2F0NzN6ZHFvd2RhcjhodCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/feOLsVVsYft04/giphy.gif"
set_bg_animation(animation_url)

#whole page
st.markdown("""
    <style>
    .block-container.st-emotion-cache-z5fcl4.ea3mdgi5 {
        padding:0;
    }
    </style>
    """, unsafe_allow_html=True)

#sidebar background
st.sidebar.markdown("""
    <style>
    [data-testid="stSidebar"] {
      background-image: url("https://static.vecteezy.com/system/resources/previews/009/443/753/non_2x/city-night-highway-illustration-with-a-car-and-starry-sky-vector.jpg");
      background-size: cover;
      background-position: 2px 2px;
    }
    </style>
    """, unsafe_allow_html=True)

#title
styled_text = """
<div style="background-color:transparent; padding:0px; border-radius:0px; margin:0px;">
<h1 style="color:#9EA49D ; font-family: Arial; font-weight: bold; font-size:75px; margin: 0px; text-shadow: 3px 5px 5px #FF4B4B; text-align:center;">Mileage <span style="color:white;">Predictor</span> ⛽️</h1>
<p style="color:white ; font-weight: bold; font-size:22px; text-align:center; margin:0px; text-shadow: 1.5px 1.5px 5px #FF4B4B; ;">This app predicts the mileage of any car based on 'Engine Fuel Type', 'Engine HP', 'Engine Cylinders',
  'Transmission Type', 'Driven_Wheels', 'Market Category', 'Vehicle Size', 'Vehicle Style'!</p>
</div>
"""
st.markdown(styled_text, unsafe_allow_html=True)


#sidebar heading
st.sidebar.markdown("""
    <style>
      .stHeadingContainer h2 {
        font-family: Arial;
        color:white;
        text-shadow: 1.5px 1.5px 5px #FF4B4B;
        font-weight:bold;
        font-size:28px;
        text-align:center;
        margin:0;
        padding:0;
    }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.header('Enter Your CAR Specifications')


def user_input_features():

    #title-selectbox
    st.sidebar.markdown("""
    <style>
      .row-widget.stSelectbox p {
        color:white;
        font-family: Arial;
        font-weight:bold;
        font-size:19px;
    }
    </style>
    """, unsafe_allow_html=True)

    #title-numberinput
    st.sidebar.markdown("""
    <style>
      .stNumberInput p {
        color:white;
        font-family: Arial;
        font-weight:bold;
        font-size:19px;
    }
    </style>
    """, unsafe_allow_html=True)

    #title-slider
    st.sidebar.markdown("""
    <style>
      .stSlider p {
        color:white;
        font-family: Arial;
        font-weight:bold;
        font-size:19px;
    }
    </style>
    """, unsafe_allow_html=True)

    #title-radio
    st.sidebar.markdown("""
    <style>
      .st-emotion-cache-l9bjmx.e1nzilvr5 p {
        color:white;
        font-family: Arial;
        font-weight:bold;
        font-size:19px;
    }
    </style>
    """, unsafe_allow_html=True)
    
#select-box 
    st.sidebar.markdown("""
    <style>
      .st-br {
        color:#FF4B4B;
        font-family: Arial;
        font-weight:bold;
        font-size:17px;
    }
    </style>
    """, unsafe_allow_html=True)

#numberinput
    st.sidebar.markdown("""
    <style>
      .st-d3 {
        color:#FF4B4B;
        font-family: Arial;
        font-weight:bold;
        font-size:17px;
    }
    </style>
    """, unsafe_allow_html=True)

#line draw
    st.sidebar.markdown("""
    <style>
      .st-emotion-cache-1inwz65 {
        color:#FF4B4B;
        font-weight:bold;
        font-size:17px;
    }
    </style>
    """, unsafe_allow_html=True)

    #Multiselect
    st.sidebar.markdown("""
    <style>
      .stMultiSelect p {
        color:white;
        font-family: Arial;
        font-weight:bold;
        font-size:19px;
    }
    </style>
    """, unsafe_allow_html=True)

    #Multiselect inner
    st.sidebar.markdown("""
    <style>
      .st-f7 {
        color:#FF4B4B;
        font-family: Arial;
        font-weight:bold;
        font-size:17px;
    }
    </style>
    """, unsafe_allow_html=True)

    #radio
    st.sidebar.markdown("""
    <style>
      .stRadio p {
        color:#FF4B4B;
        font-family: Arial;
        font-weight:bold;
        font-size:17px;
    }
    </style>
    """, unsafe_allow_html=True)
    

    fuel_dic={
        'premium unleaded (required)':0.85714286, 
        'regular (unleaded)': 1.,
        'premium unleaded (recommended)':0.71428571 ,
        'flex-fuel (unleaded)':0.57142857 ,
        'diesel':0.,
        'flex-fuel (recommended)': 0.28571429,
        'electric': 0.14285714,
        'flex-fuel (required)': 0.42857143

    }
    options_fuel = list(fuel_dic.keys())
    Engine_Fuel = st.sidebar.selectbox('Engine Fuel Type ⏲', options=options_fuel)
    
    Engine_HP = st.sidebar.number_input('Engine HP 🗜️')
    Engine_hp1 = (Engine_HP - 55) / (1001 - 55)
    
    cylinder_dic={
        '0': 0.0,
        '3': 0.1875,
        '4': 0.25,
        '5':0.3125,
        '6':0.375,  
        '8':0.5, 
        '10': 0.625,
        '12':0.75, 
        '16': 1.0
    }

    Engine_Cylinders = st.sidebar.select_slider('Engine Cylinders 🎛️',options=list(cylinder_dic.keys()))

    transmission_dic={
        'manual': 0.75 ,
        'automatic': 0.25  ,
        'automated_manual': 0. ,
        'direct_drive': 0.5 ,
        'unknown':1.
    }
    st.markdown(
    """
    <style>
    .sidebar .stRadio label span {
        font-weight: bold;  
        color:deepblue;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    Transmission_Type = st.sidebar.radio('Transmission Type ⚙️', options=list(transmission_dic.keys()))
    
    driven_dic={
        'rear wheel drive':1. ,
        'front wheel drive': 0.66666667 ,
        'all wheel drive':0.,
        'four wheel drive': 0.33333333 
    }
    Driven_Wheels = st.sidebar.radio('Driven_Wheels 🔘', options=list(driven_dic.keys()))

    mc_dic={
        'exotic':1. ,
        'factory tuner': 0.89 ,
        'hybrid':0.78,
        'hatchback': 0.67 ,
        'flex fuel':0.56 ,
        'high-performance': 0.44 ,
        'luxury':0.33,
        'crossover': 0.22 ,
        'diesel':0.11,
        'performance': 0
    }

    Market_Category = st.sidebar.multiselect('Market Category ✨', options=list(mc_dic.keys()))
    
    # Calculate the sum of values for selected market categories
    selected_values_sum = sum(mc_dic[category] for category in Market_Category)

# Calculate the average
    if Market_Category:
      average_value = selected_values_sum / len(Market_Category)
    else:
      average_value = 0

    size_dic={'compact': 0.,
              'midsize': 1.,
              'large': 0.5
    }
    
    Vehicle_Size = st.sidebar.radio('Vehicle Size 🚙', options=list(size_dic.keys()))

    style_dic={
               '2dr hatchback': 0.,
               '4dr hatchback': 0.13333333,
               'sedan': 0.93333333,
               '2dr suv': 0.06666667,
               '4dr suv': 0.2,
               'convertible suv': 0.46666667,
               'wagon': 1.,
               'coupe': 0.53333333,
               'convertible': 0.4, 
               'passenger minivan': 0.73333333,
               'cargo minivan': 0.26666667,
               'passenger van': 0.8,
               'cargo van': 0.33333333,
               'regular cab pickup': 0.86666667,
               'crew cab pickup': 0.6, 
               'extended cab pickup': 0.66666667          

    }
    Vehicle_Style = st.sidebar.selectbox('Vehicle Style 🚗', options=list(style_dic.keys()))


    data = {'Engine Fuel Type' : fuel_dic[Engine_Fuel],
            'Engine HP' : Engine_hp1, 
            'Engine Cylinders' : cylinder_dic[Engine_Cylinders],
           'Transmission Type' : transmission_dic[Transmission_Type], 
           'Driven_Wheels' : driven_dic[Driven_Wheels], 
           'Market Category' : average_value,
           'Vehicle Size' : size_dic[Vehicle_Size], 
           'Vehicle Style' : style_dic[Vehicle_Style]}
    features = pd.DataFrame(data, index=[0])

    data1 = {'Engine Fuel Type' : Engine_Fuel,
            'Engine HP' : Engine_HP, 
            'Engine Cylinders' : Engine_Cylinders,
           'Transmission Type' : Transmission_Type, 
           'Driven_Wheels' : Driven_Wheels, 
           'Market Category' : Market_Category,
           'Vehicle Size' : Vehicle_Size, 
           'Vehicle Style' : Vehicle_Style}
    
    Market_category_str=','.join(data1['Market Category'])
    data1['Market Category'] = Market_category_str

    features1 = pd.DataFrame(data1, index=[0])
    return features, features1


#details table column names
st.markdown("""
    <style>
      .dataframe th {
        color:white ;
        font-family: Arial;
        text-shadow: 1.5px 1.5px 2px #FF4B4B;  ;
        font-weight:bold;
        font-size:17px;
        border: 1px solid #EBDFF1 ;
    }
    </style>
    """, unsafe_allow_html=True)

#details table column details
st.markdown("""
    <style>
      .dataframe td {
        color:#FF4B4B;
        font-family: Arial;
        text-shadow: 1.5px 1.5px 2px #FF4B4B   ;
        font-weight:bold;
        font-size:17px;
        border: 1px solid #EBDFF1 ;
    }
    </style>
    """, unsafe_allow_html=True)

def center_dataframe(df2): 
  return f"""
  <style>
  .container {{
    text-align:center;
    margin: 0 auto;
    width: fit-content;  # Adjust width if needed
  }}

  .dataframe {{
    border: 1px solid #EBDFF1 ;
    text-align:center;
    padding: 0;
  }}
  </style>
  <div class="container">
    <div class="dataframe">{df2.to_html(index=False)}</div>
  </div>
  """

# User input features
df, df1 = user_input_features()

st.markdown("""
        <style>
        .row-widget.stButton p {
            box-shadow: 3.5px 3.5px 4px #94D7F8
            background-color:red;
            text-align:center;
            position: relative;
            color:#FF4B4B ;
            font-family: Arial;
            font-weight:bold;
            font-size:18px;
        }
        </style>
        """, unsafe_allow_html=True)

st.markdown("""
        <style>
        .row-widget.stButton {
            margin-top: 10px;
            box-shadow: 3.5px 3.5px 4px #94D7F8
            background-color:red;
            text-align:center;
            position: relative;
            color:#FF4B4B ;
            font-family: Arial;
            font-weight:bold;
            font-size:18px;
        }
        </style>
        """, unsafe_allow_html=True)

if st.sidebar.button('Predict Mileage'):

    #check_specifications
    styled_check_text="""
    <div>
    <h2 style="text-align:center; color:white ; font-family: Arial; margin-top:30px; text-shadow: 1.5px 1.5px 5px #FF4B4B; font-weight: bold; font-size:37px; "> Check Your Car's Specifications Below 👇</h2>
    </div>
    """
    st.markdown(styled_check_text, unsafe_allow_html=True)

    

    # Display centered dataframe
    st.write(center_dataframe(df1), unsafe_allow_html=True)



    # Read the CSV file from the raw GitHub URL
    data = pd.read_csv(r'https://raw.githubusercontent.com/Lalith-Adithya/cars_mileage/main/df_10.csv')

    # Now you can use the 'data' DataFrame for further analysis or processing


    X = data[['Engine Fuel Type', 'Engine HP', 'Engine Cylinders',
            'Transmission Type', 'Driven_Wheels', 'Market Category',
            'Vehicle Size', 'Vehicle Style']]
    Y = data['Average MPG']

    #support vector
    clf = SVR()
    clf.fit(X, Y)
    prediction_SVR = clf.predict(df)

    #Linear regression
    Lreg = LinearRegression()
    Lreg.fit(X, Y)
    prediction_LR = Lreg.predict(df)

    #Random Forest
    Rreg = RandomForestRegressor()
    Rreg.fit(X, Y)
    prediction_RF = Rreg.predict(df)

    #KNN
    Kreg = KNeighborsRegressor()
    Kreg.fit(X, Y)
    prediction_KNN = Kreg.predict(df)

    #decision trees
    Dreg = DecisionTreeRegressor()
    Dreg.fit(X, Y)
    prediction_D = Dreg.predict(df)

    #total prdiction
    prediction_array = ( prediction_SVR + prediction_LR + prediction_RF + prediction_KNN + prediction_D ) / 5
    prediction = prediction_array.reshape(-1)[0]
    prediction = round(prediction, 2)
    #final result
    styled_result_text="""
    <div>
    <h2 style="text-align:center; color:white ; font-family: Arial; margin-top:30px; text-shadow: 1.5px 1.5px 4px #FF4B4B ; font-size:40px;"> Your, car mileage is:</h2>
    </div>
    """
    st.markdown(styled_result_text, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .stMarkdown code {
            background-color:transparent;
            font-family: Arial;
            box-shadow: 1.5px 1.5px 4px #94D7F8
            padding-top:9px;
            color:#FF4B4B;
            font-weight:bold;
            font-size:28px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        .stMarkdown p {
            box-shadow: 3.5px 3.5px 4px #94D7F8
            background-color:transparent;
            text-align:center;
            color:#FF4B4B ;
            font-family: Arial;
            font-weight:bold;
            font-size:28px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.write(prediction,"Miles per Gallon!!!")
else:
   #check_specifications
    styled_check_text="""
    <div>
    <h2 style="text-align:center; color:white ; font-family: Arial; margin-top:30px; text-shadow: 1.5px 1.5px 5px #FF4B4B; font-weight: bold; font-size:37px; "> 👈 PLEASE ENTER YOUR CAR'S SPECIFICATION </h2>
    </div>
    """
    st.markdown(styled_check_text, unsafe_allow_html=True)




   
