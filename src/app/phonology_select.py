"""
This module contains the widgets to select the Phonology.
"""
import streamlit as st

from src.app.phonology_options import *
from src.phone.phonology import Phonology

phonology = None

def update_map(label):
    value = st.session_state[label]
    key = label.replace('*', '').replace('[', '').replace(']', '').strip()
    if value in digrams:
        phonology.set(key, digrams[value])
    else:
        phonology.set(key, value)


def add_selectbox(label, options):
    sb = st.selectbox(label, options, key=label, on_change=update_map, args=(label,))
    if label not in st.session_state:
        st.session_state[label] = sb
    return sb


def add_phonology(phonology_map: repr(Phonology)):
    global phonology
    phonology = phonology_map
    tab_Nasals, tab_Stops, tab_Fricatives, tab_Liquids, tab_Laryngeals, tab_Sonorants, tab_Semivowels, tab_Vowels, tab_Diphthongs, tab_Color = st.tabs(
        ['Nasals', 'Stops', 'Fricatives', 'Liquids', 'Laryngeals', 'Sonorants', 'Semivowels', 'Vowels', 'Diphthongs',
         'Color'])

    # Nasals
    with tab_Nasals:
        add_nasals()

    # Stops
    with tab_Stops:
        add_stops()

    # Fricatives
    with tab_Fricatives:
        add_fricatives()

    # Liquids
    with tab_Liquids:
        add_liquids()

    # Laryngeals
    with tab_Laryngeals:
        add_laryngeals()

    # Sonorants
    with tab_Sonorants:
        add_sonorants()

    # Semivowels
    with tab_Semivowels:
        add_semivowels()

    # Vowels
    with tab_Vowels:
        add_vowels()

    # Diphthongs
    with tab_Diphthongs:
        add_diphthongs()

    # Color
    with tab_Color:
        add_color()


def add_nasals():
    row_N = st.columns(6)
    with row_N[1]:
        st.caption('**Labial**')
        option_nasal_lab = add_selectbox(blb_vcd_nas, blb_vcd_nas_opt)

    with row_N[2]:
        st.caption('**Coronal**')
        option_nasal_cor = add_selectbox(alv_vcd_nas, alv_vcd_nas_opt)


def add_stops():
    # Voiced Stops
    row_VCL = st.columns(6)
    with row_VCL[0]:
        st.caption('Voiceless')
    with row_VCL[1]:
        st.caption('**Labial**')
        option_stop_vls_lab = add_selectbox(blb_vls_stp, blb_vls_stp_opt)
    with row_VCL[2]:
        st.caption('**Coronal**')
        option_stop_vls_cor = add_selectbox(avl_vls_stp, avl_vls_stp_opt)
    with row_VCL[3]:
        st.caption('**Palatal Dorsal**')
        option_stop_vls_dor_pal = add_selectbox(pal_vls_stp, pal_vls_stp_opt)
    with row_VCL[4]:
        st.caption('**Plain Dorsal**')
        option_stop_vls_dor_pln = add_selectbox(vel_vls_stp, vel_vls_stp_opt)
    with row_VCL[5]:
        st.caption('**Labial Dorsal**')
        option_stop_vls_dor_lab = add_selectbox(vel_vls_stp_lab, vel_vls_stp_lab_opt)

    # Voiced Stops
    row_VCD = st.columns(6)
    with row_VCD[0]:
        st.caption('Voiced')
    with row_VCD[1]:
        option_stop_vcd_lab = add_selectbox(blb_vcd_stp, blb_vcd_stp_opt)
    with row_VCD[2]:
        option_stop_vcd_cor = add_selectbox(avl_vcd_stp, avl_vcd_stp_opt)
    with row_VCD[3]:
        option_stop_vcd_dor_pal = add_selectbox(pal_vcd_stp, pal_vcd_stp_opt)
    with row_VCD[4]:
        option_stop_vcd_dor_pln = add_selectbox(vel_vcd_stp, vel_vcd_stp_opt)
    with row_VCD[5]:
        option_stop_vcd_dor_lab = add_selectbox(vel_vcd_stp_lab, vel_vcd_stp_lab_opt)

    # Aspirated Stops
    row_ASP = st.columns(6)
    with row_ASP[0]:
        st.caption('Aspirated')
    with row_ASP[1]:
        option_stop_asp_lab = add_selectbox(blb_vcd_stp_asp, blb_vcd_stp_asp_opt)
    with row_ASP[2]:
        option_stop_asp_cor = add_selectbox(avl_vcd_stp_asp, avl_vcd_stp_asp_opt)
    with row_ASP[3]:
        option_stop_asp_dor_pal = add_selectbox(pal_vcd_stp_asp, pal_vcd_stp_asp_opt)
    with row_ASP[4]:
        option_stop_asp_dor_pln = add_selectbox(vel_vcd_stp_asp, vel_vcd_stp_asp_opt)
    with row_ASP[5]:
        option_stop_asp_dor_lab = add_selectbox(vel_vcd_stp_lab_asp, vel_vcd_stp_lab_asp_opt)


def add_laryngeals():
    row_H = st.columns(6)
    # with row_H[0]:
    #    st.caption('Laryngeals')
    with row_H[1]:
        option_lary_h1 = add_selectbox(lary_h1, lary_h1_opt)
    with row_H[2]:
        option_lary_h2 = add_selectbox(lary_h2, lary_h2_opt)
    with row_H[3]:
        option_lary_h3 = add_selectbox(lary_h3, lary_h3_opt)


def add_fricatives():
    row_Fhead = st.columns(6)
    with row_Fhead[2]:
        st.caption('**Coronal**')

    # Fricatives
    row_F = st.columns(6)
    # with row_F[0]:
    #    st.caption('Fricative')
    with row_F[2]:
        option_fric_cor = add_selectbox(alv_vls_sib_frc, alv_vls_sib_frc_opt)


def add_liquids():
    row_Lhead = st.columns(6)
    with row_Lhead[2]:
        st.caption('**Coronal**')

    row_L = st.columns(7)
    # with row_L[0]:
    #    st.caption('Liquids')
    with row_L[2]:
        option_liq_r = add_selectbox(alv_vcd_trl, alv_vcd_trl_opt)
    with row_L[3]:
        option_liq_l = add_selectbox(alv_vcd_lat_apr, alv_vcd_lat_apr_opt)


def add_sonorants():
    row_SN = st.columns(6)
    # with row_SN[0]:
    #    st.caption('Sonorants')
    with row_SN[1]:
        option_sonr_m = add_selectbox(blb_vcd_nas_syl, blb_vcd_nas_syl_opt)
    with row_SN[2]:
        option_sonr_n = add_selectbox(alv_vcd_nas_syl, alv_vcd_nas_syl_opt)
    with row_SN[3]:
        option_sonr_l = add_selectbox(alv_vcd_lat_apr_syl, alv_vcd_lat_apr_syl_opt)
    with row_SN[4]:
        option_sonr_r = add_selectbox(avl_vcd_trl_syl, avl_vcd_trl_syl_opt)


def add_semivowels():
    row_SV = st.columns(6)
    # with row_SV[0]:
    #    st.caption('Semivowels')
    with row_SV[3]:
        st.caption('**Palatal Dorsal**')
        option_semv_y = add_selectbox(smv_y, smv_y_opt)
    with row_SV[5]:
        st.caption('**Labial Dorsal**')
        option_semv_w = add_selectbox(smv_w, smv_w_opt)


def add_vowels():
    row_Vhead = st.columns(6)
    # with row_Vhead[0]:
    #    st.caption('Vowels')

    with row_Vhead[1]:
        st.caption('**front**')
    with row_Vhead[2]:
        st.caption('**back**')

    with row_Vhead[4]:
        st.caption('**accent**')

    row_V1 = st.columns(6)
    with row_V1[0]:
        st.caption('short')
    with row_V1[1]:
        option_vowel_e = add_selectbox(vwl_e, vwl_e_opt)
    with row_V1[2]:
        option_vowel_o = add_selectbox(vwl_o, vwl_o_opt)

    with row_V1[4]:
        accent_opt = ['stress', 'pitch', 'none']
        label = 'accent'
        accent_button = st.radio('', accent_opt, on_change=update_map,
                                 args=(label,), horizontal=True)
        if label not in st.session_state:
            st.session_state[label] = accent_button

    row_V2 = st.columns(6)
    with row_V2[0]:
        st.caption('long')
    with row_V2[1]:
        option_vowel_ee = add_selectbox(vwl_ee, vwl_ee_opt)
    with row_V2[2]:
        option_vowel_oo = add_selectbox(vwl_oo, vwl_oo_opt)


def add_diphthongs():
    row_Dheader = st.columns(7)

    with row_Dheader[0]:
        st.caption('**short**')
    with row_Dheader[1]:
        st.caption('$-$w')
    with row_Dheader[2]:
        st.caption('$-$y')

    with row_Dheader[4]:
        st.caption('**long**')
    with row_Dheader[5]:
        st.caption('$-$w')
    with row_Dheader[6]:
        st.caption('$-$y')

    # 'aw' and 'ay' diphthongs
    row_Da = st.columns(7)
    with row_Da[0]:
        st.caption('a$-$')
    with row_Da[1]:
        option_diph_aw = add_selectbox(dip_aw, dip_aw_opt)
    with row_Da[2]:
        option_diph_ay = add_selectbox(dip_ay, dip_ay_opt)
    with row_Da[4]:
        st.caption('ā$-$')
    with row_Da[5]:
        option_diph_aaw = add_selectbox(dip_aaw, dip_aaw_opt)
    with row_Da[6]:
        option_diph_aay = add_selectbox(dip_aay, dip_aay_opt)

    # 'ew' and 'ey' diphthongs
    row_De = st.columns(7)
    with row_De[0]:
        st.caption('e$-$')
    with row_De[1]:
        option_diph_ew = add_selectbox(dip_ew, dip_ew_opt)
    with row_De[2]:
        option_diph_ey = add_selectbox(dip_ey, dip_ey_opt)
    with row_De[4]:
        st.caption('ē$-$')
    with row_De[5]:
        option_diph_eew = add_selectbox(dip_eew, dip_eew_opt)
    with row_De[6]:
        option_diph_eey = add_selectbox(dip_eey, dip_eey_opt)

    # 'ow' and 'oy' diphthongs
    row_Do = st.columns(7)
    with row_Do[0]:
        st.caption('o$-$')
    with row_Do[1]:
        option_diph_ow = add_selectbox(dip_ow, dip_ow_opt)
    with row_Do[2]:
        option_diph_oy = add_selectbox(dip_oy, dip_oy_opt)
    with row_Do[4]:
        st.caption('ō$-$')
    with row_Do[5]:
        option_diph_oow = add_selectbox(dip_oow, dip_oow_opt)
    with row_Do[6]:
        option_diph_ooy = add_selectbox(dip_ooy, dip_ooy_opt)


def add_color():
    row_Sound = st.columns(4)
    #with row_Sound[0]:
    #    st.caption('Color')

    with row_Sound[1]:
        option_color_h1e = add_selectbox(color_h1e, color_h1e_opt)
        option_color_eh1 = add_selectbox(color_eh1, color_eh1_opt)
    with row_Sound[2]:
        option_color_h2e = add_selectbox(color_h2e, color_h2e_opt)
        option_color_eh2 = add_selectbox(color_eh2, color_eh2_opt)
    with row_Sound[3]:
        option_color_h3e = add_selectbox(color_h3e, color_h3e_opt)
        option_color_eh3 = add_selectbox(color_eh3, color_eh3_opt)