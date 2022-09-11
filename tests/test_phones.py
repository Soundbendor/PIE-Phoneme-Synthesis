import unittest

from src.app.phonology_options import *
from src.util.matcher import load_phonemes, phone_df


class TestPhonology(unittest.TestCase):
    def test_options(self):
        """
        Test that all options for phonology are contained in dataset of phones.
        """

        df = phone_df()

        opts = []
        opts += digrams
        opts += blb_vcd_nas_opt + alv_vcd_nas_opt
        opts += blb_vls_stp_opt + blb_vcd_stp_opt + blb_vcd_stp_asp_opt
        opts += avl_vls_stp_opt + avl_vcd_stp_opt + avl_vcd_stp_asp_opt
        opts += pal_vls_stp_opt + pal_vcd_stp_opt + pal_vcd_stp_asp_opt
        opts += vel_vls_stp_opt + vel_vcd_stp_opt + vel_vcd_stp_asp_opt
        opts += vel_vls_stp_lab_opt + vel_vcd_stp_lab_opt + vel_vcd_stp_lab_asp_opt
        opts += lary_h1_opt + lary_h2_opt + lary_h3_opt
        opts += alv_vls_sib_frc_opt + alv_vcd_trl_opt + alv_vcd_lat_apr_opt
        opts += avl_vcd_trl_syl_opt + alv_vcd_lat_apr_syl_opt + blb_vcd_nas_syl_opt + alv_vcd_nas_syl_opt
        opts += smv_y_opt + smv_w_opt
        opts += vwl_e_opt + vwl_ee_opt + vwl_o_opt + vwl_oo_opt
        opts += dip_ay_opt + dip_aay_opt + dip_ey_opt + dip_eey_opt + dip_oy_opt + dip_ooy_opt
        opts += dip_aw_opt + dip_aaw_opt + dip_ew_opt + dip_eew_opt + dip_ow_opt + dip_oow_opt

        for opt in opts:
            if opt in digrams:
                for symb in digrams[opt]:
                    self.assertIn(symb, df['curr'].values)
            else:
                self.assertIn(opt, df['curr'].values)
