import streamlit
import pandas
import plotly.express

streamlit.title("India's Overview")

streamlit.set_page_config(layout = "wide")

#python -m streamlit run app.py
#py -m streamlit run app.py

data = pandas.read_csv("india_info.csv")

# streamlit.dataframe(data)

streamlit.sidebar.title("India's Dashbaord")


streamlit.sidebar.subheader("Filters")

states = data["State"].unique().tolist()

states.insert(0, "India")


choose_state = streamlit.sidebar.selectbox("Choose your state", states)

gender = streamlit.sidebar.radio("Choose Gender", ["Male", "Female"])

sizes = streamlit.sidebar.selectbox("Choose what to show with size", data.columns[6 : ])

colorr = streamlit.sidebar.selectbox("Choose what to show using color", data.columns[6 : ])


if choose_state == "India":
    fig = plotly.express.scatter_map(data, lat = "Latitude", lon = "Longitude", height = 800, zoom = 4, size = sizes, hover_name = "District", color = colorr, color_continuous_scale = "viridis",  center={"lat": 22.5, "lon": 80.0})

else:
    data = data[data["State"] == choose_state]
    center_lat = data["Latitude"].mean()
    center_lon = data["Longitude"].mean()
    fig = plotly.express.scatter_map(data, lat = "Latitude", lon = "Longitude", height = 800, zoom = 6, size = sizes, hover_name = "District", color = colorr, color_continuous_scale = "viridis", center={
            "lat": center_lat,
            "lon": center_lon
        })

streamlit.plotly_chart(fig)
