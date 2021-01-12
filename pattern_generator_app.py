from AJ_pattern_file_generator_lib_app import pattern_generator_files as pgf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import base64

from PIL import Image

import streamlit as st

def download_file(data, filename):
    testo = 'Download '+filename
    csv = data.to_csv(index=False, header = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.asc">'+testo+'</a>'
    st.markdown(href, unsafe_allow_html=True)

sample = str(st.sidebar.text_input('File Name','sample'))
num_elements_x = int(st.sidebar.text_input('Num doses on X',1))
num_elements_y = int(st.sidebar.text_input('Num doses on Y',2))
raggio_iniziale = float(st.sidebar.text_input('Starting Radius (um)',0.01))
raggio_finale = float(st.sidebar.text_input('Ending Radius (um)',0.1))
step_size = float(st.sidebar.text_input('Radius step size (um)',0.01))
distanza_tra_cerchi = int(st.sidebar.text_input('Distance between two arrays (um)',50))
dimArr = int(st.sidebar.text_input('Array dimension (um)',30))
distanza_dosi_x = int(st.sidebar.text_input('Distance between two set of doses on X (um)',100))
distanza_dosi_y = int(st.sidebar.text_input('Distance between two set of doses on Y (um)',100))
layer = int(st.sidebar.text_input('Layer',1))
step_dose = float(st.sidebar.text_input('Dose step',1))
dose_base = float(st.sidebar.text_input('First Dose',1))
text_label = str(st.sidebar.text_input('Label',''))
dose_marker = float(st.sidebar.text_input('Dose marker', 9))
marker_type = st.sidebar.selectbox('Marker type', ['Bracket','Cross'])

if st.checkbox('Legend'):
    st.write('---')
    image_legenda1 = Image.open('legenda1.jpg')
    st.image(image_legenda1, use_column_width=True)
    st.write('---')
    image_legenda2 = Image.open('legenda2.jpg')
    st.image(image_legenda2, use_column_width=True)
    st.write('---')


select_mode = st.selectbox('Mode', ['','Circle', 'Rectangle', 'Bowtie', 'Point', 'Elips', 'Bowtie multi-pitch', 'Triangle', 'Eight Shape', 'Waveguide'])

circle_check, bowtie_check, rectangle_check, point_check, bowtie_check_2, triangle_check, sandro_check, elips_check, waveguide_check = False, False, False, False, False, False, False, False, False
width, vertici, rotazione, lato_cost, altezza, base, elips_start_r, elips_rotatio, elips_vertex, elips_stop_r, elips_sep = 0, 100, 0, 0.1, 0.01, 0.03, 0.01, 0, 100, 0.1, 0.01
pitch_choice_text, bowtie_pitch_x, bowtie_pitch_y, starting_high, ending_high, high_step, angle, angle2 = 'range_on_X', 2, 2, 0.01, 0.1, 0.01, 60, 60
gap_len_min, gap_len_max, gap_len_step, y_size, x_size, distance_between_gat, base_triangle, distance_grating, deg_grating, size_grating, pitch_grating, number_of_grating, vertici_grating = 0.1,1,0.1,4.5,15,15,5.5,9,40,0.2,0.58,5,100

feature_check = ''

if select_mode == 'Circle':
    feature_check = 'circle'
    circle_check = True
    width = float(st.text_input('Inner Radius (um)',0))
    vertici = int(st.text_input('Num Vertex',100))
    rotazione = float(st.text_input('Rotation',0))

if select_mode == 'Rectangle':
    feature_check = 'rectangle'
    rectangle_check = True
    lato_cost = float(st.text_input('Constant edge length (um)',0.1))

if select_mode == 'Bowtie':
    feature_check = 'bowtie'
    bowtie_check = True
    altezza = float(st.text_input('High (um)',0.01))
    base = float(st.text_input('Base (um)',0.03))

if select_mode == 'Point':
    feature_check = 'point'
    point_check = True
    raggio_iniziale = 0.01
    raggio_finale = 0.02
    step_size = 0.01

if select_mode == 'Elips':
    feature_check = 'elips'
    elips_check = True
    elips_start_r = float(st.text_input('Radius2 (um)',0.01))
    elips_rotatio = float(st.text_input('Rotation (deg)',0))
    elips_vertex = int(st.text_input('Num Vertex',100))
    elips_stop_r = 0.1
    elips_sep = 0.01

if select_mode == 'Bowtie multi-pitch':
    feature_check = 'bowtie_multi'
    bowtie_check_2 = True
    pitch_choice_text = st.selectbox('Type of pitch', ['range_on_X','range_on_Y', 'range_on_XY'])
    bowtie_pitch_x = float(st.text_input('Pitch X (um)',2))
    bowtie_pitch_y = float(st.text_input('Pitch Y (um)',2))
    starting_high = float(st.text_input('Starting High (um)',0.01))
    ending_high = float(st.text_input('Ending High (um)',0.1))
    high_step = float(st.text_input('High step size (um)',0.01))
    angle = float(st.text_input('Angle (deg)',60))

if select_mode == 'Triangle':
    feature_check = 'triangle'
    triangle_check = True
    angle2 = float(st.text_input('Angle (deg)',60))

if select_mode == 'Eight Shape':
    feature_check = 'sandro'
    sandro_check = True
    raggio_iniziale = 0.01
    raggio_finale = 0.02
    step_size = 0.01

if select_mode == 'Waveguide':
    feature_check = 'waveguide'
    waveguide_check = True

    image_waveguide = Image.open('grating_image.jpg')
    st.image(image_waveguide, use_column_width=True)

    gap_len_min = float(st.text_input('Gap length min (um)', 0.1))
    gap_len_max = float(st.text_input('Gap length max (um)', 1))
    gap_len_step = float(st.text_input('Gap length step (um)', 0.1))
    y_size = float(st.text_input('Y size (um)', 4.5))
    x_size = float(st.text_input('X size (um)', 15))
    distance_between_gat = float(st.text_input('Distance between one waveguide and the next one on Y (um)', 15))
    base_triangle = float(st.text_input('Aperture size (um)', 5.5))
    distance_grating = float(st.text_input('Distance of the grating from the gap (um)', 9))
    deg_grating = float(st.text_input('Angle of the grating (deg)',40))
    size_grating = float(st.text_input('Single Grating thickness (um)', 0.2))
    pitch_grating = float(st.text_input('Grating pitch (um)', 0.58))
    number_of_grating = int(st.text_input('number of gratings', 5))
    vertici_grating = int(st.text_input('Num Vertex',100))


if st.button('Create'):
    pattern, name_pattern, markers, testo_cerchi, testo_dosi, name_markers, namefile_marker = pgf().lettura_variabili(sample, num_elements_x, num_elements_y,
                            raggio_iniziale, raggio_finale, step_size, distanza_tra_cerchi, dimArr, distanza_dosi_x, distanza_dosi_y, layer,
                            step_dose, dose_base, width, vertici, rotazione, altezza, base, lato_cost, text_label, bowtie_pitch_x, bowtie_pitch_y,
                            pitch_choice_text, dose_marker, starting_high, ending_high, high_step, angle, angle2, elips_start_r, elips_stop_r,
                            elips_sep, elips_rotatio, elips_vertex, gap_len_min, gap_len_max, gap_len_step, y_size, x_size, distance_between_gat,
                            base_triangle, distance_grating, deg_grating, size_grating, pitch_grating, number_of_grating, vertici_grating, feature_check, marker_type)

    pgf().preview_generator(sample, num_elements_x, num_elements_y, raggio_iniziale, raggio_finale, step_size, distanza_tra_cerchi, dimArr, distanza_dosi_x,
                            distanza_dosi_y, layer, step_dose, dose_base, width, vertici, rotazione, altezza, base, lato_cost, text_label, bowtie_pitch_x,
                            bowtie_pitch_y, pitch_choice_text, dose_marker, starting_high, ending_high, high_step, angle, feature_check)
    st.pyplot()
    st.write('Red line represents the writing fields')

    pattern = pd.DataFrame(np.array(pattern).reshape(-1,1))
    pattern.columns = [' ']
    download_file(pattern, name_pattern)

    markers = pd.DataFrame(np.array(markers).reshape(-1,1))
    only_markers = markers.copy()
    only_markers.columns = [' ']
    download_file(only_markers, namefile_marker)
    testo_cerchi = pd.DataFrame(np.array(testo_cerchi).reshape(-1,1))
    testo_dosi = pd.DataFrame(np.array(testo_dosi).reshape(-1,1))
    markers = pd.concat([markers,testo_cerchi])
    markers = pd.concat([markers,testo_dosi])
    markers.columns = [' ']
    download_file(markers, name_markers)
