import numpy as np
from AJ_pattern_generator_lib import pattern
from AJ_draw import disegna as ds

class pattern_generator_files:
    def lettura_variabili(self, sample, num_elements_x, num_elements_y, raggio_iniziale, raggio_finale, step_size,
                          distanza_tra_cerchi, dimArr, distanza_dosi_x, distanza_dosi_y, layer, step_dose, dose_base,
                          width, vertici, rotazione, altezza, base, lato_cost, text_label, pitch_object_x, pitch_object_y,
                          pitch_choice_text, dose_marker, starting_high, ending_high, high_step, angle, angle2, elips_start_r,
                          elips_stop_r, elips_sep, elips_rotatio, elips_vertex, gap_len_min, gap_len_max, gap_len_step, y_size,
                          x_size, distance_between_gat, base_triangle, distance_grating, deg_grating, size_grating, pitch_grating,
                          number_of_grating, vertici_grating, feature_check, marker_type,
                          aa1,bb1,cc1,gg1,dd1, aa2,bb2,cc2,gg2,dd2,mm2, H, X_min, X_max, Y_min, Y_max, X_step, Y_step, X, Y):


        if feature_check == 'circle':
            namefile = 'AAA_cirlce_' + sample + '.asc'
        if feature_check == 'bowtie':
            namefile_bowtai = 'AAA_bowtie_' + sample + '.asc'
        if feature_check == 'bowtie_multi':
            namefile_bowtai_2 = 'AAA_bowtie_multi_pitch_' + sample + '.asc'
        if feature_check == 'rectangle':
            namefile_rettangolo = 'AAA_rectangle_' + sample + '.asc'
        if feature_check == 'point':
            namefile_point = 'AAA_point_' + sample + '.asc'
        if feature_check == 'triangle':
            namefile_triangle = 'AAA_triangle_' + sample + '.asc'
        if feature_check == 'sandro':
            namefile_sandro = 'AAA_sandro_' + sample + '.asc'
        if feature_check == 'elips':
            namefile_elips = 'AAA_elips_' + sample + '.asc'
        if feature_check == 'waveguide':
            namefile_wave = 'AAA_wave_' + sample + '.asc'
        if feature_check == 'waveguide_T':
            namefile_waveT = 'AAA_waveT_' + sample + '.asc'
        if feature_check == 'Waveguide_T_dose_matrix':
            namefile_waveT_dose = 'AAA_waveT_' + sample + '.asc'


        namefile_marker = 'AAA_marker_' + sample + '.asc'
        namefile_testo = 'AAA_text_' + sample + '.asc'
        namefile_testo_dosi = 'AAA_text_dose_' + sample + '.asc'
        namefile_global = 'AAA_markers_and_labels_' + sample + '.asc'

        num_dosi = num_elements_x * num_elements_y

        if distanza_tra_cerchi < 30:
            distanza_tra_cerchi = 30


    # ███████  ██████  ██████      ████████ ██   ██ ███████     ███    ███  █████  ██████  ██   ██ ███████ ██████  ███████
    # ██      ██    ██ ██   ██        ██    ██   ██ ██          ████  ████ ██   ██ ██   ██ ██  ██  ██      ██   ██ ██
    # █████   ██    ██ ██████         ██    ███████ █████       ██ ████ ██ ███████ ██████  █████   █████   ██████  ███████
    # ██      ██    ██ ██   ██        ██    ██   ██ ██          ██  ██  ██ ██   ██ ██   ██ ██  ██  ██      ██   ██      ██
    # ██       ██████  ██   ██        ██    ██   ██ ███████     ██      ██ ██   ██ ██   ██ ██   ██ ███████ ██   ██ ███████



        if dimArr > distanza_tra_cerchi:
            dimArr = distanza_tra_cerchi-20  # size if the array which lay within the markers

        ############################################################
        num_raggio = round((raggio_finale - raggio_iniziale)/step_size)
        raggio = np.zeros(num_raggio)

        num_high = round((ending_high - starting_high)/high_step)
        high = np.zeros(num_high)

        num_r2 = round((elips_stop_r - elips_start_r)/elips_sep)
        r2 = np.zeros(num_r2)

        num_gap_len = round((gap_len_max - gap_len_min)/gap_len_step)
        gap_len = np.zeros(num_gap_len)

        dose = np.zeros(num_dosi)
        x = np.zeros(num_elements_x)
        y = np.zeros(num_elements_y)


# ██████  ██ ███████ ████████  █████  ███    ██  ██████ ███████     ██████  ███████ ████████ ██     ██ ███████ ███████ ███    ██     ████████ ██     ██  ██████      ██████  ██ ███████ ███████ ███████ ██████  ███████ ███    ██ ████████     ██████   ██████  ███████ ███████ ███████
# ██   ██ ██ ██         ██    ██   ██ ████   ██ ██      ██          ██   ██ ██         ██    ██     ██ ██      ██      ████   ██        ██    ██     ██ ██    ██     ██   ██ ██ ██      ██      ██      ██   ██ ██      ████   ██    ██        ██   ██ ██    ██ ██      ██      ██
# ██   ██ ██ ███████    ██    ███████ ██ ██  ██ ██      █████       ██████  █████      ██    ██  █  ██ █████   █████   ██ ██  ██        ██    ██  █  ██ ██    ██     ██   ██ ██ █████   █████   █████   ██████  █████   ██ ██  ██    ██        ██   ██ ██    ██ ███████ █████   ███████
# ██   ██ ██      ██    ██    ██   ██ ██  ██ ██ ██      ██          ██   ██ ██         ██    ██ ███ ██ ██      ██      ██  ██ ██        ██    ██ ███ ██ ██    ██     ██   ██ ██ ██      ██      ██      ██   ██ ██      ██  ██ ██    ██        ██   ██ ██    ██      ██ ██           ██
# ██████  ██ ███████    ██    ██   ██ ██   ████  ██████ ███████     ██████  ███████    ██     ███ ███  ███████ ███████ ██   ████        ██     ███ ███   ██████      ██████  ██ ██      ██      ███████ ██   ██ ███████ ██   ████    ██        ██████   ██████  ███████ ███████ ███████

        # distance between the elements with the same size
        pitch_x = (distanza_tra_cerchi)*(num_raggio) + distanza_dosi_x
        pitch_y = distanza_dosi_y

        for i in range(num_raggio):
            raggio[i] = raggio_iniziale + step_size*i

        for i in range(num_gap_len):
            gap_len[i] = gap_len_min + gap_len_step*i

        for i in range(num_high):
            high[i] = starting_high + high_step*i

        for i in range(num_r2):
            r2[i] = elips_start_r + elips_sep*i

        for i in range(num_dosi):
            dose[i] = dose_base+i*step_dose

        for i in range(num_elements_x):
            x[i] = i*pitch_x
        for j in range(num_elements_y):
            y[j] = j*pitch_y


        elips = []
        sandro = []
        triangolo = []
        rettangolo = []
        Waveguide_T_dose_matrix = []
        cerchio = []
        farfalle = []
        farfalle_2 = []
        markers = []
        testo_cerchi = []
        testo = []
        testo_dosi = []
        punti = []
        wave = []

        for i in range(num_raggio):
            # text written in the scketch (circles diametre)
            testo.append(round((raggio_iniziale + step_size*i)*1000))


            # ██████   █████  ████████ ████████ ███████ ██████  ███    ██      ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████
            # ██   ██ ██   ██    ██       ██    ██      ██   ██ ████   ██     ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██
            # ██████  ███████    ██       ██    █████   ██████  ██ ██  ██     ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████
            # ██      ██   ██    ██       ██    ██      ██   ██ ██  ██ ██     ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██
            # ██      ██   ██    ██       ██    ███████ ██   ██ ██   ████      ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██


        angle2 = angle2*(np.pi/180)
        for k in range(num_raggio):
            dose_i = 0
            for j in range(num_elements_y):
                for i in range(num_elements_x):
                    if feature_check == 'rectangle':
                        # create the rectangle array
                        rettangolo.append(pattern().rettangolo(x[i] + k*distanza_tra_cerchi, y[j], dose[dose_i], layer, raggio[k], lato_cost))
                    if feature_check == 'triangle':
                        # create the rectangle array
                        triangolo.append(pattern().triangle(x[i] + k*distanza_tra_cerchi, y[j], dose[dose_i], layer, raggio[k],  2*raggio[k]*np.tan(angle2/2)))
                    if feature_check == 'circle':
                        # create the circles array
                        cerchio.append(pattern().circle(x[i] + k*distanza_tra_cerchi, y[j], dose[dose_i], layer, width, raggio[k], vertici, rotazione))
                    if feature_check == 'bowtie':
                        # create the bowtie array
                        farfalle.append(pattern().bowtai(x[i] + k*distanza_tra_cerchi, y[j], dose[dose_i], layer, raggio[k], altezza, base))
                    if feature_check == 'Waveguide_T_dose_matrix':
                        # create the Waveguide_T_dose_matrix array
                        Waveguide_T_dose_matrix.append(pattern().waveguide(x[i] + k*distanza_tra_cerchi, y[j], dose[dose_i], layer, X, Y, raggio[k], H))

                    # create the markers array
                    if marker_type == 'Cross':
                        markers.append(pattern().marker_cross(x[i] + k*distanza_tra_cerchi, y[j], dose_marker, str(layer)+'1', dimArr))
                    else:
                        markers.append(pattern().marker(x[i] + k*distanza_tra_cerchi, y[j], dose_marker, str(layer)+'1', dimArr))

                    # create the label array
                    testo_cerchi.append(pattern().generatore_testo(x[i]+(dimArr/2) + k*distanza_tra_cerchi, y[j]+dimArr+30, dose_marker, str(layer)+'2', testo[k]))
                    dose_i = dose_i + 1

                    # ██     ██  █████  ██    ██ ███████  ██████  ██    ██ ██ ██████  ███████
                    # ██     ██ ██   ██ ██    ██ ██      ██       ██    ██ ██ ██   ██ ██
                    # ██  █  ██ ███████ ██    ██ █████   ██   ███ ██    ██ ██ ██   ██ █████
                    # ██ ███ ██ ██   ██  ██  ██  ██      ██    ██ ██    ██ ██ ██   ██ ██
                    #  ███ ███  ██   ██   ████   ███████  ██████   ██████  ██ ██████  ███████

        if feature_check == 'waveguide':
            dose_i = 0
            for j in range(num_elements_y):
                for i in range(num_elements_x):

                    for k in range(num_raggio):
                        for l in range(num_gap_len):
                            wave.append(pattern().waveguide_nic(x[i] + k*distanza_tra_cerchi, y[j] + l*distance_between_gat, dose[dose_i], layer, raggio[k], gap_len[l], y_size, x_size, base_triangle,
                                              distance_grating, deg_grating, size_grating, pitch_grating, number_of_grating, vertici_grating))

                    dose_i = dose_i + 1


# ██     ██  █████  ██    ██ ███████  ██████  ██    ██ ██ ██████  ███████     ██
# ██     ██ ██   ██ ██    ██ ██      ██       ██    ██ ██ ██   ██ ██          ██
# ██  █  ██ ███████ ██    ██ █████   ██   ███ ██    ██ ██ ██   ██ █████       ██
# ██ ███ ██ ██   ██  ██  ██  ██      ██    ██ ██    ██ ██ ██   ██ ██          ██
#  ███ ███  ██   ██   ████   ███████  ██████   ██████  ██ ██████  ███████     ██


        if feature_check == 'waveguide_T':
            lato_y = [i for i in np.linspace(Y_min, Y_max, round((Y_max-Y_min)/Y_step)+1)]
            lato_x = [i for i in np.linspace(X_min, X_max, round((X_max-X_min)/X_step)+1)]
            position = [i for i in np.linspace(0, 65, len(raggio))]

            waveT = []
            dimer = []
            tappo = []
            testo2 = []
            for k in range(len(lato_x)):
                for j in range(len(lato_y)):
                    if j == 0:
                        salto = 0
                    else:
                        salto = 26*j
                    for i in range(len(position)):
                        waveT.append(pattern().waveguide(100*k, position[i]+(position[-1]+position[1])*(j)+salto, dose=dose_marker, layer=layer, lato_x=lato_x[k], lato_y=lato_y[j], gap=raggio[i], H = H))
                        dimer.append(pattern().bar_dimer(100*k + lato_x[k]*2 + 5, position[i]+(position[-1]+position[1])*(j)+salto, dose=dose_marker, layer=layer, lato_y=lato_y[j], gap=raggio[i], H = H))
                        tappo.append(pattern().rettangolo(100*k+lato_x[k], position[i]+(position[-1]+position[1])*(j)+salto, dose = dose_marker, layer=layer+1, lato_x=raggio[i], lato_y=lato_y[j]))
                        testo2.append(pattern().generatore_testo(-50+100*k, position[i]+(position[-1]+position[1])*(j)+3+salto, dose = dose_marker, layer=str(layer)+'2', testo ='X ' + str(round(lato_x[k],2))
                                                                + ' Y ' + str(round(lato_y[j],2)) + ' G ' + str(round(raggio[i],2)) ))
            waveT_tot = []
            waveT = np.array(waveT).reshape(-1,1)
            dimer = np.array(dimer).reshape(-1,1)
            tappo = np.array(tappo).reshape(-1,1)

            for i in waveT:
                waveT_tot.append(i)
            for i in dimer:
                waveT_tot.append(i)
            for i in tappo:
                waveT_tot.append(i)


# ███    ███ ██    ██ ██   ████████ ██     ██████  ██ ████████  ██████ ██   ██     ██████   ██████  ██     ██ ████████ ██ ███████
# ████  ████ ██    ██ ██      ██    ██     ██   ██ ██    ██    ██      ██   ██     ██   ██ ██    ██ ██     ██    ██    ██ ██
# ██ ████ ██ ██    ██ ██      ██    ██     ██████  ██    ██    ██      ███████     ██████  ██    ██ ██  █  ██    ██    ██ █████
# ██  ██  ██ ██    ██ ██      ██    ██     ██      ██    ██    ██      ██   ██     ██   ██ ██    ██ ██ ███ ██    ██    ██ ██
# ██      ██  ██████  ███████ ██    ██     ██      ██    ██     ██████ ██   ██     ██████   ██████   ███ ███     ██    ██ ███████


        if feature_check == 'bowtie_multi':
            num_object_x = round(dimArr/pitch_object_x)
            num_object_y = round(dimArr/pitch_object_y)

            del testo, testo_cerchi, markers
            testo = []
            testo_cerchi = []
            markers = []

            for i in range(num_high):
                # text written in the scketch (high lenght)
                testo.append(round((starting_high + high_step*i)*1000))

            angle = angle*(np.pi/180)
            for k in range(num_high):
                base_2 = 2*high[k]*np.tan(angle/2)
                dose_i = 0
                for j in range(num_elements_y):
                    for i in range(num_elements_x):

                        # create the label array
                        testo_cerchi.append(pattern().generatore_testo(x[i]+(dimArr/2) + k*distanza_tra_cerchi, y[j]+dimArr+30, dose_marker, str(layer)+'2', testo[k]))

                        # create the markers array
                        if marker_type == 'Cross':
                            markers.append(pattern().marker_cross(x[i] + k*distanza_tra_cerchi, y[j], dose_marker, str(layer)+'1', dimArr))
                        else:
                            markers.append(pattern().marker(x[i] + k*distanza_tra_cerchi, y[j], dose_marker, str(layer)+'1', dimArr))
                        step_bowtie_gap = 0
                        for l in range(num_object_y):
                            for m in range(num_object_x):
                                # create the bowtie array
                                if pitch_choice_text == 'range_on_XY':
                                    farfalle_2.append(pattern().bowtai(
                                        x[i] + k*distanza_tra_cerchi + m*pitch_object_x, y[j] + l*pitch_object_y, dose[dose_i], layer, raggio_iniziale + step_size*step_bowtie_gap, high[k], base_2))
                                if pitch_choice_text == 'range_on_Y':
                                    farfalle_2.append(pattern().bowtai(
                                        x[i] + k*distanza_tra_cerchi + m*pitch_object_x, y[j] + l*pitch_object_y, dose[dose_i], layer, raggio_iniziale + step_size*l, high[k], base_2))
                                if pitch_choice_text == 'range_on_X':
                                    farfalle_2.append(pattern().bowtai(
                                        x[i] + k*distanza_tra_cerchi + m*pitch_object_x, y[j] + l*pitch_object_y, dose[dose_i], layer, raggio_iniziale + step_size*m, high[k], base_2))
                                step_bowtie_gap = step_bowtie_gap + 1

                        dose_i = dose_i + 1


                        # ███████ ██      ██ ██████  ███████
                        # ██      ██      ██ ██   ██ ██
                        # █████   ██      ██ ██████  ███████
                        # ██      ██      ██ ██           ██
                        # ███████ ███████ ██ ██      ███████


        if feature_check == 'elips':

            del testo, testo_cerchi, markers
            testo = []
            testo_cerchi = []
            markers = []

            # for i in range(num_r2):
            #     # text written in the scketch (high lenght)
            #     testo.append(round((elips_start_r + elips_sep*i)*1000))
            # for k in range(num_r2):
            #     dose_i = 0
            #     for j in range(num_elements_y):
            #         for i in range(num_elements_x):
            #
            #             # create the label array
            #             testo_cerchi.append(pattern().generatore_testo(x[i]+(dimArr/2) + k*distanza_tra_cerchi, y[j]+dimArr+30, dose_marker, str(layer)+'2', testo[k]))
            #
            #             # create the markers array
            #             markers.append(pattern().marker(x[i] + k*distanza_tra_cerchi, y[j], dose_marker, str(layer)+'1', dimArr))
            #
            #             for l in range(num_raggio):
            #                 for m in range(num_raggio):
            #                     elips.append(pattern().elips(x[i] + k*distanza_tra_cerchi + m*pitch_object_x, y[j] + l*pitch_object_y, dose[dose_i], layer, r2[k], raggio_iniziale + step_size*m, elips_vertex , elips_rotatio))
            #
            #             dose_i = dose_i + 1

            for i in range(num_raggio):
                # text written in the scketch (high lenght)
                testo.append(round((elips_start_r + elips_sep*i)*1000))

            for k in range(num_raggio):
                dose_i = 0
                for j in range(num_elements_y):
                    for i in range(num_elements_x):
                        # create the label array
                        testo_cerchi.append(pattern().generatore_testo(x[i]+(dimArr/2) + k*distanza_tra_cerchi, y[j]+dimArr+30, dose_marker, str(layer)+'2', testo[k]))
                        # create the markers array
                        if marker_type == 'Cross':
                            markers.append(pattern().marker_cross(x[i] + k*distanza_tra_cerchi, y[j], dose_marker, str(layer)+'1', dimArr))
                        else:
                            markers.append(pattern().marker(x[i] + k*distanza_tra_cerchi, y[j], dose_marker, str(layer)+'1', dimArr))
                        elips.append(pattern().elips(x[i] + k*distanza_tra_cerchi, y[j], dose[dose_i], layer, elips_start_r, raggio[k], vertici, rotazione))
                        dose_i = dose_i + 1


#################################################################################################



# ██████   ██████  ████████     ███████     ███████  █████  ███    ██ ██████  ██████   ██████
# ██   ██ ██    ██    ██        ██          ██      ██   ██ ████   ██ ██   ██ ██   ██ ██    ██
# ██   ██ ██    ██    ██        █████       ███████ ███████ ██ ██  ██ ██   ██ ██████  ██    ██
# ██   ██ ██    ██    ██        ██               ██ ██   ██ ██  ██ ██ ██   ██ ██   ██ ██    ██
# ██████   ██████     ██        ███████     ███████ ██   ██ ██   ████ ██████  ██   ██  ██████


        dose_i = 0
        for j in range(num_elements_y):
            for i in range(num_elements_x):
                if feature_check == 'point':
                    punti.append(pattern().dot(x[i], y[j], dose[dose_i], layer))
                if feature_check == 'sandro':
                    sandro.append(pattern().sandro(x[i], y[j], dose[dose_i], layer, aa1,bb1,cc1,gg1,dd1, aa2,bb2,cc2,gg2,dd2,mm2))
                    # print(dose[dose_i])


# ██████   ██████  ███████ ███████     ████████ ███████ ██   ██ ████████
# ██   ██ ██    ██ ██      ██             ██    ██       ██ ██     ██
# ██   ██ ██    ██ ███████ █████          ██    █████     ███      ██
# ██   ██ ██    ██      ██ ██             ██    ██       ██ ██     ██
# ██████   ██████  ███████ ███████        ██    ███████ ██   ██    ██

                # create the dose text
                if feature_check == 'bowtie_multi':
                    testo_dosi.append(pattern().generatore_testo(x[i] + (num_high)*distanza_tra_cerchi + 20, y[j] + dimArr/2, dose_marker, str(layer)+'2', 'D '+str(dose[dose_i])+' G'+str(round(raggio_iniziale*1000))+'to'+str(round(raggio_finale*1000))+' '+text_label))
                else:
                    testo_dosi.append(pattern().generatore_testo(x[i] + (num_raggio)*distanza_tra_cerchi + 20, y[j] + dimArr/2, dose_marker, str(layer)+'2', 'D '+str(dose[dose_i])+' '+text_label))

                dose_i = dose_i + 1


                # ███████  █████  ██    ██ ███████      ██████  ███    ██     ███████ ██ ██      ███████
                # ██      ██   ██ ██    ██ ██          ██    ██ ████   ██     ██      ██ ██      ██
                # ███████ ███████ ██    ██ █████       ██    ██ ██ ██  ██     █████   ██ ██      █████
                #      ██ ██   ██  ██  ██  ██          ██    ██ ██  ██ ██     ██      ██ ██      ██
                # ███████ ██   ██   ████   ███████      ██████  ██   ████     ██      ██ ███████ ███████

        if feature_check == 'circle':
            return cerchio, namefile, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'rectangle':
            return rettangolo, namefile_rettangolo, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'triangle':
            return triangolo, namefile_triangle, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'bowtie':
            return farfalle, namefile_bowtai, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'bowtie_multi':
            return farfalle_2, namefile_bowtai_2, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'point':
            return punti, namefile_point, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'sandro':
            return sandro, namefile_sandro, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'elips':
            return elips, namefile_elips, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'waveguide':
            return wave, namefile_wave, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'waveguide_T':
            return waveT_tot, namefile_waveT, testo2, markers, testo_dosi, namefile_global, namefile_marker
        if feature_check == 'Waveguide_T_dose_matrix':
            return Waveguide_T_dose_matrix, namefile_waveT_dose, markers, testo_cerchi, testo_dosi, namefile_global, namefile_marker




        # ██████  ██████   █████  ██     ██     ██████  ██████  ███████ ██    ██ ██ ███████ ██     ██
        # ██   ██ ██   ██ ██   ██ ██     ██     ██   ██ ██   ██ ██      ██    ██ ██ ██      ██     ██
        # ██   ██ ██████  ███████ ██  █  ██     ██████  ██████  █████   ██    ██ ██ █████   ██  █  ██
        # ██   ██ ██   ██ ██   ██ ██ ███ ██     ██      ██   ██ ██       ██  ██  ██ ██      ██ ███ ██
        # ██████  ██   ██ ██   ██  ███ ███      ██      ██   ██ ███████   ████   ██ ███████  ███ ███


    def preview_generator(self, sample, num_elements_x, num_elements_y, raggio_iniziale, raggio_finale, step_size, distanza_tra_cerchi, dimArr, distanza_dosi_x, distanza_dosi_y,
                          layer, step_dose, dose_base, width, vertici, rotazione, altezza, base, lato_cost, text_label, pitch_object_x, pitch_object_y, pitch_choice_text, dose_marker,
                          starting_high, ending_high, high_step, angle, feature_check):
        if distanza_tra_cerchi < 30:
            distanza_tra_cerchi = 30

        ############ for the markers ############

        if dimArr > distanza_tra_cerchi:
            dimArr = distanza_tra_cerchi-20  # size if the array which lay within the markers

        ############################################################

        num_raggio = round((raggio_finale - raggio_iniziale)/step_size)

        if feature_check == 'bowtie_multi':
            num_raggio = round((ending_high - starting_high)/high_step)

        x = np.zeros(num_elements_x)
        y = np.zeros(num_elements_y)

        # distance between the elements with the same size (distance between two different doses)
        pitch_x = (distanza_tra_cerchi)*(num_raggio) + distanza_dosi_x
        pitch_y = distanza_dosi_y

        for i in range(num_elements_x):
            x[i] = i*pitch_x
        for j in range(num_elements_y):
            y[j] = j*pitch_y

        for k in range(num_raggio):
            dose_i = 0
            for j in range(num_elements_y):
                for i in range(num_elements_x):
                    # draw the preview of the pattern
                    pattern().disegna_pattern(x[i] + k*distanza_tra_cerchi, y[j], dimArr)

                    # draw the preview of the markers
                    # pattern().disegna_pattern(x[i] + k*distanza_tra_cerchi - 10, y[j] - 10, dimArr+20, colore= 'black')
                    pattern().disegna_marker(x[i] + k*distanza_tra_cerchi - 5       , y[j] - 5, 1, 10, colore="#00A3E0")
                    pattern().disegna_marker(x[i] + k*distanza_tra_cerchi - 5+dimArr+10, y[j] - 5, 1, 10, colore="#00A3E0")
                    pattern().disegna_marker(x[i] + k*distanza_tra_cerchi - 5       , y[j] - 5+dimArr+10, 1, 10, colore="#00A3E0")
                    pattern().disegna_marker(x[i] + k*distanza_tra_cerchi - 5+dimArr+10, y[j] - 5+dimArr+10, 1, 10, colore="#00A3E0")


                    # draw the preview of the labels for each array
                    pattern().disegna_pattern(x[i]+(dimArr/2) + k * distanza_tra_cerchi, y[j]+dimArr+30, 1, colore='green')
                    dose_i = dose_i + 1


        dose_i = 0
        for j in range(num_elements_y):
            for i in range(num_elements_x):
                # draw the preview of the dose label
                pattern().disegna_pattern(x[i] + (num_raggio) * distanza_tra_cerchi + 20, y[j] + dimArr/2, 1)
                dose_i = dose_i + 1

        for k in range(round(num_raggio/2)):
            for j in range(num_elements_y+3):
                for i in range(num_elements_x+2):
                    # draw the preview of the writing field
                    pattern().disegna_pattern(x[0] - 10 + i*100 + k*100, y[0] - 10 + j*100, 100, colore='#db3f3f')

        ds().aggiusta_la_finestra()
