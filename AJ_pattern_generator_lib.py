# import sys
# sys.path.insert(0, 'C:/Users/ajacassi/OneDrive/ponte/programmi/python/progetto2/AJ_lib')
# sys.path.insert(0, 'C:/Users/ajacassi/OneDrive/ponte/programmi/python/progetto2/EBL_stand_alone')

import numpy as np
from AJ_draw import disegna as ds
from AJ_function_4_analysis import size_manipulator as sm

class pattern:


    # ██████   ██████  ████████
    # ██   ██ ██    ██    ██
    # ██   ██ ██    ██    ██
    # ██   ██ ██    ██    ██
    # ██████   ██████     ██


    def dot(self, x, y, dose, layer):
        dose = dose*100
        testo0 = 'P ' + str(dose) + ' ' + str(layer)
        testo1 = str(x) + ' ' + str(y)
        testo2 = '#'
        return testo0, testo1, testo2


        # ██████   ██████  ██     ██ ████████ ██ ███████
        # ██   ██ ██    ██ ██     ██    ██    ██ ██
        # ██████  ██    ██ ██  █  ██    ██    ██ █████
        # ██   ██ ██    ██ ██ ███ ██    ██    ██ ██
        # ██████   ██████   ███ ███     ██    ██ ███████


    def bowtai(self, x, y, dose, layer, gap, altezza, base):
        dose = dose*100
        gap = gap/2
        testoi = ['' for i in range(12)]
        testoi[0] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[1] = str(x-gap) + ' ' + str(y)
        testoi[2] = str(x-gap-altezza) + ' ' + str(y+base/2)
        testoi[3] = str(x-gap-altezza) + ' ' + str(y-base/2)
        testoi[4] = str(x-gap) + ' ' + str(y)
        testoi[5] = '#'
        testoi[6] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[7] = str(x+gap) + ' ' + str(y)
        testoi[8] = str(x+gap+altezza) + ' ' + str(y+base/2)
        testoi[9] = str(x+gap+altezza) + ' ' + str(y-base/2)
        testoi[10] = str(x+gap) + ' ' + str(y)
        testoi[11] = '#'
        return testoi

        # testoi = ['' for i in range(11)]
        # testoi[0], testoi[1], testoi[2], testoi[3], testoi[4] = self.circle(x,y,dose,layer,0, altezza/2, 100, 0)
        # testoi[5] = '#'
        # testoi[6], testoi[7], testoi[8], testoi[9], testoi[10] = self.circle(x+altezza+gap,y,dose,layer,0, altezza/2, 100, 0)
        # return testoi

        # ████████ ██████  ██  █████  ███    ██  ██████  ██      ███████
        #    ██    ██   ██ ██ ██   ██ ████   ██ ██       ██      ██
        #    ██    ██████  ██ ███████ ██ ██  ██ ██   ███ ██      █████
        #    ██    ██   ██ ██ ██   ██ ██  ██ ██ ██    ██ ██      ██
        #    ██    ██   ██ ██ ██   ██ ██   ████  ██████  ███████ ███████


    def triangle(self, x, y, dose, layer, altezza, base):
        dose = dose*100
        testoi = ['' for i in range(6)]
        testoi[0] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[1] = str(x) + ' ' + str(y)
        testoi[2] = str(x-altezza) + ' ' + str(y+base/2)
        testoi[3] = str(x-altezza) + ' ' + str(y-base/2)
        testoi[4] = str(x) + ' ' + str(y)
        testoi[5] = '#'
        return testoi


        #  ██████ ██ ██████   ██████ ██      ███████
        # ██      ██ ██   ██ ██      ██      ██
        # ██      ██ ██████  ██      ██      █████
        # ██      ██ ██   ██ ██      ██      ██
        #  ██████ ██ ██   ██  ██████ ███████ ███████

    def circle(self, x, y, dose, layer, width, raggio, vertici, rotazione):
        dose = dose*100
        if width == 0:
            testo0 = 'C ' + str(dose) + ' ' + str(layer)
        else:
            testo0 = 'C ' + str(dose) + ' ' + str(layer) + ' ' + str(raggio-width)
        testo1 = str(x) + ' ' + str(y)
        if width == 0:
            testo2 = str(raggio)
        else:
            testo2 = str((raggio+width)/2)
        testo3 = str(vertici)
        testo4 = str(rotazione)
        testo5 = '#'
        return testo0, testo1, testo2, testo3, testo4, testo5


#  █████  ██████   ██████
# ██   ██ ██   ██ ██
# ███████ ██████  ██
# ██   ██ ██   ██ ██
# ██   ██ ██   ██  ██████

    def arc(self, x, y, dose, layer, width, raggio, ang1, ang2, vertici, rotazione):
        dose = dose*100
        if width == 0:
            testo0 = 'A ' + str(dose) + ' ' + str(layer)
        else:
            testo0 = 'A ' + str(dose) + ' ' + str(layer) + ' ' + str(width)
        testo1 = str(x) + ' ' + str(y)
        testo2 = str(raggio)
        testo3 = str(vertici)
        testo4 = str(rotazione)+' '+str(ang1)+' '+str(ang2)
        testo5 = '#'
        return testo0, testo1, testo2, testo3, testo4, testo5

        # ███████ ██      ██ ██████  ███████
        # ██      ██      ██ ██   ██ ██
        # █████   ██      ██ ██████  ███████
        # ██      ██      ██ ██           ██
        # ███████ ███████ ██ ██      ███████

    def elips(self, x, y, dose, layer, raggio2, raggio, vertici, rotazione):
        dose = dose*100
        testo0 = 'E ' + str(dose) + ' ' + str(layer)
        testo1 = str(x) + ' ' + str(y)
        testo2 = str(raggio) + ' ' + str(raggio2)
        testo3 = str(vertici)
        testo4 = str(rotazione)
        testo5 = '#'
        return testo0, testo1, testo2, testo3, testo4, testo5


        # ██████  ███████  ██████ ████████  █████  ███    ██  ██████  ██      ███████
        # ██   ██ ██      ██         ██    ██   ██ ████   ██ ██       ██      ██
        # ██████  █████   ██         ██    ███████ ██ ██  ██ ██   ███ ██      █████
        # ██   ██ ██      ██         ██    ██   ██ ██  ██ ██ ██    ██ ██      ██
        # ██   ██ ███████  ██████    ██    ██   ██ ██   ████  ██████  ███████ ███████


    def rettangolo(self, x, y, dose, layer, lato_x, lato_y):
        dose = dose*100
        testoi = ['' for i in range(7)]
        testoi[0] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[1] = str(x) + ' ' + str(y)
        testoi[2] = str(x+lato_x) + ' ' + str(y)
        testoi[3] = str(x+lato_x) + ' ' + str(y+lato_y)
        testoi[4] = str(x) + ' ' + str(y+lato_y)
        testoi[5] = str(x) + ' ' + str(y)
        testoi[6] = '#'
        return testoi


        # ██████   █████  ████████ ██   ██
        # ██   ██ ██   ██    ██    ██   ██
        # ██████  ███████    ██    ███████
        # ██      ██   ██    ██    ██   ██
        # ██      ██   ██    ██    ██   ██

    def automatic_marker(self, x, y, dose, layer, lenght, width, distance):
        dose = dose*100
        testoi = ['' for i in range(8)]
        testoi[0] = 'L ' + str(dose) + ' ' + str(layer)+ ' ' + str(width)
        testoi[1] = str(x-(lenght/2)) + ' ' + str(y+distance)
        testoi[2] = str(x+(lenght/2)) + ' ' + str(y+distance)
        testoi[3] = '#'
        testoi[4] = 'L ' + str(dose) + ' ' + str(layer)+ ' ' + str(width)
        testoi[5] = str(x+distance) + ' ' + str(y-(lenght/2))
        testoi[6] = str(x+distance) + ' ' + str(y+(lenght/2))
        testoi[7] = '#'
        return testoi

        # ██     ██  █████  ██    ██ ███████  ██████  ██    ██ ██ ██████  ███████
        # ██     ██ ██   ██ ██    ██ ██      ██       ██    ██ ██ ██   ██ ██
        # ██  █  ██ ███████ ██    ██ █████   ██   ███ ██    ██ ██ ██   ██ █████
        # ██ ███ ██ ██   ██  ██  ██  ██      ██    ██ ██    ██ ██ ██   ██ ██
        #  ███ ███  ██   ██   ████   ███████  ██████   ██████  ██ ██████  ███████


    def waveguide(self, x, y, dose, layer, lato_x, lato_y, gap):
        H = 0.06
        gap = gap + lato_x
        dose = dose*100
        testoi = ['' for i in range(22)]
        testoi[0] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[1] = str(x) + ' ' + str(y)
        testoi[2] = str(x+lato_x) + ' ' + str(y)
        testoi[3] = str(x+lato_x) + ' ' + str(y+lato_y)
        testoi[4] = str(x) + ' ' + str(y+lato_y)
        testoi[5] = str(x) + ' ' + str(y+lato_y-H)
        testoi[6] = str(x + (lato_x - H)) + ' ' + str(y+lato_y-H)
        testoi[7] = str(x + (lato_x - H)) + ' ' + str(y+H)
        testoi[8] = str(x) + ' ' + str(y+H)
        testoi[9] = str(x) + ' ' + str(y)
        testoi[10] = '#'

        x = x + gap
        testoi[11] = '1 ' + str(dose) + ' ' + str(layer+20)
        testoi[12] = str(x) + ' ' + str(y)
        testoi[13] = str(x+lato_x) + ' ' + str(y)
        testoi[14] = str(x+lato_x) + ' ' + str(y+H)
        testoi[15] = str(x+H) + ' ' + str(y+H)
        testoi[16] = str(x+H) + ' ' + str(y+lato_y-H)
        testoi[17] = str(x+lato_x) + ' ' + str(y+lato_y-H)
        testoi[18] = str(x + lato_x) + ' ' + str(y+lato_y)
        testoi[19] = str(x) + ' ' + str(y+lato_y)
        testoi[20] = str(x) + ' ' + str(y)
        testoi[21] = '#'
        return testoi


        # ███    ██ ██  ██████ ██   ██  ██████  ██       █████  ███████     ██     ██  █████  ██    ██ ███████
        # ████   ██ ██ ██      ██   ██ ██    ██ ██      ██   ██ ██          ██     ██ ██   ██ ██    ██ ██
        # ██ ██  ██ ██ ██      ███████ ██    ██ ██      ███████ ███████     ██  █  ██ ███████ ██    ██ █████
        # ██  ██ ██ ██ ██      ██   ██ ██    ██ ██      ██   ██      ██     ██ ███ ██ ██   ██  ██  ██  ██
        # ██   ████ ██  ██████ ██   ██  ██████  ███████ ██   ██ ███████      ███ ███  ██   ██   ████   ███████

    def waveguide_nic(self, x, y, dose, layer, gap, gap_len, y_size, x_size, base_triangle,
                      distance_grating, deg_grating, size_grating, pitch_grating, number_of_grating, vertici):
        rotazione = 0
        dose = dose*100
        testoi = []

        testoi.append('1 ' + str(dose) + ' ' + str(layer))
        testoi.append(str(x) + ' ' + str(y))
        testoi.append(str(x+x_size) + ' ' + str(y))
        testoi.append(str(x+x_size) + ' ' + str(y+y_size))
        testoi.append(str(x+(x_size/2)+(gap_len/2)) + ' ' + str(y+y_size+(base_triangle/2)-(gap/2)))
        testoi.append(str(x+(x_size/2)-(gap_len/2)) + ' ' + str(y+y_size+(base_triangle/2)-(gap/2)))
        testoi.append(str(x) + ' ' + str(y+y_size))
        testoi.append(str(x) + ' ' + str(y))
        testoi.append('#')

        testoi.append('1 ' + str(dose) + ' ' + str(layer+20))
        testoi.append(str(x) + ' ' + str(y+y_size+base_triangle+y_size))
        testoi.append(str(x+x_size) + ' ' + str(y+y_size+base_triangle+y_size))
        testoi.append(str(x+x_size) + ' ' + str(y+y_size+base_triangle))
        testoi.append(str(x+(x_size/2)+(gap_len/2)) + ' ' + str(y+y_size+(base_triangle/2)+(gap/2)))
        testoi.append(str(x+(x_size/2)-(gap_len/2)) + ' ' + str(y+y_size+(base_triangle/2)+(gap/2)))
        testoi.append(str(x) + ' ' + str(y+y_size+base_triangle))
        testoi.append(str(x) + ' ' + str(y+y_size+base_triangle+y_size))
        testoi.append('#')
        for j in range(number_of_grating):
            testo_temp = self.arc(x+(x_size/2), y+y_size+(base_triangle/2), dose/100, layer+30,
                     size_grating, distance_grating+pitch_grating*j, 180-deg_grating/2, 180+deg_grating/2, vertici, rotazione)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])

            testo_temp =  self.arc(x+(x_size/2), y+y_size+(base_triangle/2), dose/100, layer+30,
                     size_grating, -distance_grating-pitch_grating*j, -deg_grating/2, deg_grating/2, vertici, rotazione)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])
        return testoi

        # ██████   █████  ██████      ██████  ██ ███    ███ ███████ ██████  ███████
        # ██   ██ ██   ██ ██   ██     ██   ██ ██ ████  ████ ██      ██   ██ ██
        # ██████  ███████ ██████      ██   ██ ██ ██ ████ ██ █████   ██████  ███████
        # ██   ██ ██   ██ ██   ██     ██   ██ ██ ██  ██  ██ ██      ██   ██      ██
        # ██████  ██   ██ ██   ██     ██████  ██ ██      ██ ███████ ██   ██ ███████

    def bar_dimer(self, x, y, dose, layer, lato_y, gap):
        H = 0.06
        dose = dose*100
        testoi = ['' for i in range(14)]
        testoi[0] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[1] = str(x) + ' ' + str(y)
        testoi[2] = str(x+H) + ' ' + str(y)
        testoi[3] = str(x+H) + ' ' + str(y+lato_y)
        testoi[4] = str(x) + ' ' + str(y+lato_y)
        testoi[5] = str(x) + ' ' + str(y)
        testoi[6] = '#'

        x = x + gap + H
        testoi[7] = '1 ' + str(dose) + ' ' + str(layer+20)
        testoi[8] = str(x) + ' ' + str(y)
        testoi[9] = str(x+H) + ' ' + str(y)
        testoi[10] = str(x+H) + ' ' + str(y+lato_y)
        testoi[11] = str(x) + ' ' + str(y+lato_y)
        testoi[12] = str(x) + ' ' + str(y)
        testoi[13] = '#'
        return testoi

        # ███    ███  █████  ██████  ██   ██ ███████ ██████
        # ████  ████ ██   ██ ██   ██ ██  ██  ██      ██   ██
        # ██ ████ ██ ███████ ██████  █████   █████   ██████
        # ██  ██  ██ ██   ██ ██   ██ ██  ██  ██      ██   ██
        # ██      ██ ██   ██ ██   ██ ██   ██ ███████ ██   ██

    def marker(self, x, y, dose, layer, dimArr):
        dose = dose*100
        testoi = ['' for i in range(36)]
        testoi[0] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[1] = str(x-7) + ' ' + str(y-7)
        testoi[2] = str(x) + ' ' + str(y-7)
        testoi[3] = str(x) + ' ' + str(y-10)
        testoi[4] = str(x-10) + ' ' + str(y-10)
        testoi[5] = str(x-10) + ' ' + str(y)
        testoi[6] = str(x-7) + ' ' + str(y)
        testoi[7] = str(x-7) + ' ' + str(y-7)
        testoi[8] = '#'

        testoi[9] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[10] = str(x+7+dimArr) + ' ' + str(y-7)
        testoi[11] = str(x+dimArr) + ' ' + str(y-7)
        testoi[12] = str(x+dimArr) + ' ' + str(y-10)
        testoi[13] = str(x+dimArr+10) + ' ' + str(y-10)
        testoi[14] = str(x+dimArr+10) + ' ' + str(y)
        testoi[15] = str(x+dimArr+7) + ' ' + str(y)
        testoi[16] = str(x+dimArr+7) + ' ' + str(y-7)
        testoi[17] = '#'

        testoi[18] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[19] = str(x+7+dimArr) + ' ' + str(y+dimArr+7)
        testoi[20] = str(x+dimArr) + ' ' + str(y+dimArr+7)
        testoi[21] = str(x+dimArr) + ' ' + str(y+dimArr+10)
        testoi[22] = str(x+dimArr+10) + ' ' + str(y+dimArr+10)
        testoi[23] = str(x+dimArr+10) + ' ' + str(y+dimArr)
        testoi[24] = str(x+dimArr+7) + ' ' + str(y+dimArr)
        testoi[25] = str(x+dimArr+7) + ' ' + str(y+dimArr+7)
        testoi[26] = '#'

        testoi[27] = '1 ' + str(dose) + ' ' + str(layer)
        testoi[28] = str(x-7) + ' ' + str(y+dimArr+7)
        testoi[29] = str(x) + ' ' + str(y+dimArr+7)
        testoi[30] = str(x) + ' ' + str(y+dimArr+10)
        testoi[31] = str(x-10) + ' ' + str(y+dimArr+10)
        testoi[32] = str(x-10) + ' ' + str(y+dimArr)
        testoi[33] = str(x-7) + ' ' + str(y+dimArr)
        testoi[34] = str(x-7) + ' ' + str(y+dimArr+7)
        testoi[35] = '#'
        return testoi

    def marker_cross(self, x, y, dose, layer, dimArr, sizex1 = 1, sizey1 = 3, sizex2 = 0.1, sizey2 = 4, size_readerx = 0.5, size_readery = 6):

        cross_dimension = sizey1 + sizey1 + sizey2
        dimArr = dimArr + cross_dimension

        def single_cross(testoi, dimArrx, dimArry):
            # large reptangle
            testo_temp = self.rettangolo(x-(sizex1/2)+dimArrx, y-((sizey2/2)+sizey1)+dimArry, dose, layer, sizex1, sizey1)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])
            testo_temp = self.rettangolo(x-(sizex1/2)+dimArrx, y+(sizey2/2)+dimArry, dose, layer, sizex1, sizey1)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])
            testo_temp = self.rettangolo(x-((sizey2/2)+sizey1)+dimArrx, y-(sizex1/2)+dimArry, dose, layer, sizey1, sizex1)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])
            testo_temp = self.rettangolo(x+(sizey2/2)+dimArrx, y-(sizex1/2)+dimArry, dose, layer, sizey1, sizex1)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])

            # thin reptangle
            testo_temp = self.rettangolo(x-(sizex2/2)+dimArrx, y-(sizey2/2)+dimArry, dose, layer, sizex2, sizey2)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])
            testo_temp = self.rettangolo(x-(sizey2/2)+dimArrx, y-(sizex2/2)+dimArry, dose, layer, sizey2, sizex2)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])

            # autoalignment
            testo_temp = self.automatic_marker(x+dimArrx, y+dimArry, dose, 61, 6, 0.5, 3.5)
            for i in range(len(testo_temp)):
                testoi.append(testo_temp[i])

            return testoi

        testoi = []
        testoi = single_cross(testoi, 0-(cross_dimension/2), 0-(cross_dimension/2))
        testoi = single_cross(testoi, 0-(cross_dimension/2), dimArr-(cross_dimension/2))
        testoi = single_cross(testoi, dimArr-(cross_dimension/2), 0-(cross_dimension/2))
        testoi = single_cross(testoi, dimArr-(cross_dimension/2), dimArr-(cross_dimension/2))

        # testoi = single_cross(testoi, 0, 0)
        # testoi = single_cross(testoi, 0, dimArr)
        # testoi = single_cross(testoi, dimArr, 0)
        # testoi = single_cross(testoi, dimArr, dimArr)


        return testoi

        # ████████ ███████ ██   ██ ████████
        #    ██    ██       ██ ██     ██
        #    ██    █████     ███      ██
        #    ██    ██       ██ ██     ██
        #    ██    ███████ ██   ██    ██



    def generatore_testo(self, x, y, dose, layer, testo):
        dose = dose*100
        testo0 = 'T ' + str(dose) + ' ' + str(layer) + ' ' + str(0.5)
        testo1 = str(x) + ' ' + str(y)
        testo2 = str(3) + ' ' + str(0)
        testo3 = str(0) + ' ' + str(0)
        testo4 = str(testo)
        testo5 = '#'
        return testo0, testo1, testo2, testo3, testo4, testo5

        # ███████  █████  ██    ██ ███████
        # ██      ██   ██ ██    ██ ██
        # ███████ ███████ ██    ██ █████
        #      ██ ██   ██  ██  ██  ██
        # ███████ ██   ██   ████   ███████



    def salva(self, num_elements, cerchio, namefile):
        file = open(namefile, 'w')
        for i in range(num_elements):
            for j in range(len(cerchio[i])):
                file.write(cerchio[i][j]+'\n')
            # file.write('#'+'\n')
        file.close()

        # ██████  ██████   █████  ██     ██
        # ██   ██ ██   ██ ██   ██ ██     ██
        # ██   ██ ██████  ███████ ██  █  ██
        # ██   ██ ██   ██ ██   ██ ██ ███ ██
        # ██████  ██   ██ ██   ██  ███ ███



    def disegna_pattern(self, x, y, dimArr, colore="#00A3E0"):
        x_tot = np.zeros(5)
        y_tot = np.zeros(5)
        x_tot[0] = x
        x_tot[1] = x + dimArr
        x_tot[2] = x + dimArr
        x_tot[3] = x
        x_tot[4] = x
        y_tot[0] = y
        y_tot[1] = y
        y_tot[2] = y + dimArr
        y_tot[3] = y + dimArr
        y_tot[4] = y

        ds().nuova_fig(1)
        ds().titoli(titolo="design preview", xtag="um", ytag="um")
        ds().dati(x_tot, y_tot, colore = colore, larghezza_riga = 0.5)

    def disegna_marker(self, x, y, x_wide, y_wide, colore="#00A3E0"):
        x_wide = x_wide/2
        y_wide = y_wide/2
        x_tot = np.zeros(5)
        y_tot = np.zeros(5)
        x_tot[0] = x-x_wide
        x_tot[1] = x+x_wide
        x_tot[2] = x+x_wide
        x_tot[3] = x-x_wide
        x_tot[4] = x-x_wide
        y_tot[0] = y-y_wide
        y_tot[1] = y-y_wide
        y_tot[2] = y+y_wide
        y_tot[3] = y+y_wide
        y_tot[4] = y-y_wide
        ds().nuova_fig(1)
        ds().titoli(titolo="design preview", xtag="um", ytag="um")
        ds().dati(x_tot, y_tot, colore = colore, larghezza_riga = 0.5)
        x_tot[0] = x-y_wide
        x_tot[1] = x+y_wide
        x_tot[2] = x+y_wide
        x_tot[3] = x-y_wide
        x_tot[4] = x-y_wide
        y_tot[0] = y-x_wide
        y_tot[1] = y-x_wide
        y_tot[2] = y+x_wide
        y_tot[3] = y+x_wide
        y_tot[4] = y-x_wide
        ds().dati(x_tot, y_tot, colore = colore, larghezza_riga = 0.5)


        # ███████  █████  ███    ██ ██████  ██████   ██████
        # ██      ██   ██ ████   ██ ██   ██ ██   ██ ██    ██
        # ███████ ███████ ██ ██  ██ ██   ██ ██████  ██    ██
        #      ██ ██   ██ ██  ██ ██ ██   ██ ██   ██ ██    ██
        # ███████ ██   ██ ██   ████ ██████  ██   ██  ██████



    def sandro(self, x, y, dose, layer, aa1,bb1,cc1,gg1,dd1, aa2,bb2,cc2,gg2,dd2,mm2):

        def funzione(x):
            aa = aa1
            bb = bb1
            cc = cc1
            gg = gg1
            dd = dd1

            uno = (np.abs(np.sin(x)/cc)**dd + gg)**2
            due = (x/bb)**2
            return np.sqrt((aa**2)*(uno - due*uno))

        def funzione2(x):
            aa = aa2
            bb = bb2
            cc = cc2
            gg = gg2
            dd = dd2
            multi = mm2

            uno = (np.abs(np.sin(x)/cc)**dd + gg/multi)**2
            due = (x/bb)**2
            return np.sqrt((aa**2)*(uno - due*uno))

        dose = dose*100
        risoluzione = 250

        coordX_old = np.linspace(-2, 2, risoluzione)
        coordY_old = funzione(coordX_old)
        coordY2_old = funzione2(coordX_old)

        coordX_old = coordX_old*1.78
        coordY_old = coordY_old*1.59
        coordY2_old = coordY2_old*1.59

        coorXnew, coordYnew = sm(coordY_old).nanremoval(coordX_old, data_time = 'no')
        coordXnew2, coordYnew2 = sm(coordY2_old).nanremoval(coordX_old, data_time = 'no')

#######################################################################

        testoi = ['' for i in range(len(coorXnew)+len(coordXnew2)+2)]
        testoi[0] = '1 ' + str(dose) + ' ' + str(layer)
        for i in range(len(coorXnew)):
            testoi[i+1] = str(coorXnew[i]+x) + ' ' + str(coordYnew[i]+y)

        for i in range(len(coordXnew2)):
            testoi[len(coorXnew)+i+1] = str(coordXnew2[len(coordXnew2)-1-i]+x) + ' ' + str(coordYnew2[len(coordXnew2)-1-i]+y)

        testoi[-1] =  str(coorXnew[0]+x) + ' ' + str(coordYnew[0]+y)

#######################################################################

        testoi2 = ['' for i in range(len(coorXnew)+len(coordXnew2)+3)]
        testoi2[0] = '#'
        testoi2[1] = '1 ' + str(dose) + ' ' + str(layer)
        for i in range(len(coorXnew)):
            testoi2[i+2] = str(coorXnew[i]+x) + ' ' + str(-coordYnew[i]+y)

        for i in range(len(coordXnew2)):
            testoi2[len(coorXnew)+i+2] = str(coordXnew2[len(coordXnew2)-1-i]+x) + ' ' + str(-coordYnew2[len(coordXnew2)-1-i]+y)


        testoi2[-1] =  str(coorXnew[0]+x) + ' ' + str(-coordYnew[0]+y)

#######################################################################

        testoi3 = ['' for i in range(7)]
        testoi3[0] = '#'
        testoi3[1] = '1 ' + str(dose) + ' ' + str(layer)
        testoi3[2] = str(coorXnew[0]+x) + ' ' + str(coordYnew[0]+y)
        testoi3[3] = str(coordXnew2[0]+x) + ' ' + str(coordYnew2[0]+y)
        testoi3[4] = str(coordXnew2[0]+x) + ' ' + str(-coordYnew2[0]+y)
        testoi3[5] = str(coorXnew[0]+x) + ' ' + str(-coordYnew[0]+y)
        testoi3[6] = str(coorXnew[0]+x) + ' ' + str(coordYnew[0]+y)

        testoi4 = ['' for i in range(8)]
        testoi4[0] = '#'
        testoi4[1] = '1 ' + str(dose) + ' ' + str(layer)
        testoi4[2] = str(coorXnew[-1]+x) + ' ' + str(coordYnew[-1]+y)
        testoi4[3] = str(coordXnew2[-1]+x) + ' ' + str(coordYnew2[-1]+y)
        testoi4[4] = str(coordXnew2[-1]+x) + ' ' + str(-coordYnew2[-1]+y)
        testoi4[5] = str(coorXnew[-1]+x) + ' ' + str(-coordYnew[-1]+y)
        testoi4[6] = str(coorXnew[-1]+x) + ' ' + str(coordYnew[-1]+y)
        testoi4[7] = '#'


        test_tot = testoi+testoi2+testoi3+testoi4

        return test_tot



        # ██   ██ ██  █████   ██████  ███████ ███████ ██
        #  ██ ██  ██ ██   ██ ██    ██ ██      ██      ██
        #   ███   ██ ███████ ██    ██ █████   █████   ██
        #  ██ ██  ██ ██   ██ ██    ██ ██      ██      ██
        # ██   ██ ██ ██   ██  ██████  ██      ███████ ██


    def xiaofei1(self, L1, L2, L3, W, gap, dose):
        uno = []
        uno.append(self.rettangolo(0,                     0, dose, 1, L1, W))
        uno.append(self.rettangolo(L1+gap,                0, dose, 1, L3, W))
        uno.append(self.rettangolo(L1+gap+L3+gap,         0, dose, 1, L1, W))
        uno.append(self.rettangolo(L1+gap+(L3/2)-(W/2),   W+gap, dose, 1, W, L2))
        return uno

    def xiaofei2(self, L1, L2, L3, W, gap, dose):
        uno = []
        uno.append(self.rettangolo(0,                     0, dose, 1, L1, L2))
        uno.append(self.rettangolo(L1+gap,                L2-(W/2), dose, 1, L3, W))
        uno.append(self.rettangolo(L1+gap+L3+gap,         0, dose, 1, L1, L2))
        return uno
