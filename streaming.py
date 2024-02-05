import streamlit as st
import pickle

pickle_in = open("xgboost_srbsn.pkl", 'rb')
regressor = pickle.load(pickle_in)

def predict_note_authentication(sintering_pressure, Oxygen, particle_size, Purity, Y, Yb, M, Mn, L, Eu, Al, N2_H2, nitriding_temp, nitriding_time, Sintering_temp, Sintering_time):

    predicition = regressor.predict([[sintering_pressure, Oxygen, particle_size, Purity, Y, Yb, M, Mn, L, Eu, Al, N2_H2, nitriding_temp, nitriding_time, Sintering_temp, Sintering_time]])
    return predicition


def main():

    st.title("SRBSN TC")

    sintering_pressure = st.number_input("Post Sintering Pressure")
    Oxygen = st.number_input('Oxygen')
    particle_size = st.number_input('Particle Size')
    Purity = st.number_input('Purity')
    Y = st.number_input('Y2O3')
    Yb = st.number_input('Yb2O3')
    M = st.number_input('MgO')
    Mn = st.number_input('MnSiN2')
    L = st.number_input('Li2CO3')
    Eu = st.number_input('Eu2O3')
    Al = st.number_input('Al impurity')
    N2_H2= st.number_input('N2/N2:H2')
    nitriding_temp = st.number_input('Nitriding Temp')
    nitriding_time = st.number_input('Nitriding Time')
    Sintering_temp = st.number_input('Post Sintering temp')
    Sintering_time = st.number_input('Post Sintering Time')

    result = ""

    if st.button('Predict'):
        result = predict_note_authentication(sintering_pressure, Oxygen, particle_size, Purity, Y, Yb, M, Mn, L, Eu, Al, N2_H2, nitriding_temp, nitriding_time, Sintering_temp, Sintering_time)
    st.success("Thermal COnductivity = {}".format(result))

if __name__ == '__main__':
    main()

