"""
This module contains the options to select for the Phonology.
"""

# phonemes represented by two+ phones
digrams = {
    'ʔp': ['ʔ', 'p'],
    'ʔt': ['ʔ', 't'],
    'bh': ['b', 'h'],
    'bʲ': ['b', 'ʲ'],
    'dh': ['d', 'h'],
    'gh': ['g', 'h'],
    'ʔkʲ': ['ʔ', 'kʲ'],
    'ʔk': ['ʔ', 'k'],
    'ʔkw': ['ʔ', 'k', 'w'],
    'kw': ['k', 'w'],
    'kwh': ['k', 'w', 'h'],
    'kʲh': ['kʲ', 'h'],
    'qu': ['q', 'u'],
    'gw': ['g', 'w'],
    'għ': ['g', 'ħ'],
    'gʰw': ['ɡʰ', 'w'],
    'ɡʲh': ['ɡʲ', 'h'],
    'gwh': ['g', 'w', 'h'],
    'gɣh': ['g', 'ɣ', 'h'],
    'gʰ': ['ɡʰ'],
    'ɣw': ['ɣ', 'w'],
    'ʕw': ['ʕ', 'w'],
    'ʔw': ['ʔ', 'w'],
    'eːʊ': ['eː', 'ʊ']
}

"""
Nasals
"""
blb_vcd_nas = '*m'
blb_vcd_nas_opt = ['m', 'mʲ']

alv_vcd_nas = '*n'
alv_vcd_nas_opt = ['n', 'n̪', 'ɳ', 'ɲ', 'ŋ', 'nʲ']

"""
Stops
"""
# Labial stops
blb_vls_stp = '*p'
blb_vls_stp_opt = ['p', 'p`', 'pʰ', 'ph', 'ʔp']

blb_vcd_stp = '[*b]'
blb_vcd_stp_opt = ['b', 'bʲ', 'ʔp', 'p`']

blb_vcd_stp_asp = '*bʰ'
blb_vcd_stp_asp_opt = ['bʰ', 'bh', 'pʰ', 'ph']

# Coronal stops
avl_vls_stp = '*t'
avl_vls_stp_opt = ['t', 't`', 'tʰ', 'th', 'θ', 't̪', 'ʈ', 'c', 'ɟ']

avl_vcd_stp = '*d'
avl_vcd_stp_opt = ['d', 'dʲ', 'ʔt', 'd̪', 'ɖ', 'ð', 'dˤ']

avl_vcd_stp_asp = '*dʰ'
avl_vcd_stp_asp_opt = ['dʰ', 'dh', 'ɖʰ', 'dˤ', 'dʒ', 'tʰ', 'th']

# Palatal Dorsal
pal_vls_stp = '*ḱ'
pal_vls_stp_opt = ['kʲ', 'k`', 'q`', 'c']

pal_vcd_stp = '*ǵ'
pal_vcd_stp_opt = ['ɡʲ', 'g', 'ɣ', 'ʔkʲ']

pal_vcd_stp_asp = '*ǵʰ'
pal_vcd_stp_asp_opt = ['ɡʲh', 'gʰ', 'ɡʲ', 'għ', 'gh', 'kʲh']

# Plain Dorsal
vel_vls_stp = '*k'
vel_vls_stp_opt = ['k', 'q', 'c', 'ɟ']

vel_vcd_stp = '*g'
vel_vcd_stp_opt = ['g', 'ʁ',  'ɣ', 'ʔk']

vel_vcd_stp_asp = '*gʰ'
vel_vcd_stp_asp_opt = ['gʰ', 'gh', 'kʰ', 'kh']

# Labial Dorsal
vel_vls_stp_lab = '*kʷ'
vel_vls_stp_lab_opt = ['kw', 'qu', 'kwh']

vel_vcd_stp_lab = '*gʷ'
vel_vcd_stp_lab_opt = ['gw', 'ɣw', 'ʔkw']

vel_vcd_stp_lab_asp = '*gʷʰ'
vel_vcd_stp_lab_asp_opt = ['gʰw', 'gwh', 'gɣh', 'kw', 'kwh']

"""
Glottal
"""
# Laryngeal
lary_h1 = '*h₁'
lary_h1_opt = ['h', 'ħ', 'ʕ', 'ʔ', 'χ', 'x']
lary_h2 = '*h₂'
lary_h2_opt = ['χ', 'ʰχ', 'x', 'h', 'ħ', 'ʕ', 'ʔ']
lary_h3 = '*h₃'
lary_h3_opt = ['ɣ', 'ɣw', 'ʕw', 'ʔw']

"""
Fricatives and Liquids
"""
# Fricative
alv_vls_sib_frc = '*s'
alv_vls_sib_frc_opt = ['s', 'ʃ', 'ʂ', 'ɕ', 's̺', 's̪', 's̻', 'z', 'ʑ', 'ʐ']

# Liquids
alv_vcd_trl = '*r'
alv_vcd_trl_opt = ['r', 'r̝', 'ɾ', 'ɽ', 'ɹ', 'ɻ', 'r.', 'r̝̊', 'ʁ']

alv_vcd_lat_apr = '*l'
alv_vcd_lat_apr_opt = ['l', 'ɭ', 'ɹ', 'ɻ']

"""
Sonorants and Semivowels
"""
# Sonorants: r̥, l̥, m̥, n̥
avl_vcd_trl_syl = '*r̥'
avl_vcd_trl_syl_opt = ['r̩', 'r̩ː', 'r̥', 'ɑːɹ', 'ər', 'ɛɹ', 'ɪɹ', 'ʊɹ', 'r', 'r.', 'r̝̊', 'ɾ', 'ɹ']

alv_vcd_lat_apr_syl = '*l̥'
alv_vcd_lat_apr_syl_opt = ['l̩', 'l̩ː', 'l̥', 'əl', 'l', 'ɭ', 'ɬ', 'ɫ', 'll']

blb_vcd_nas_syl = '*m̥'
blb_vcd_nas_syl_opt = ['m̩', 'm̥', 'm']

alv_vcd_nas_syl = '*n̥'
alv_vcd_nas_syl_opt = ['n̩', 'n̥', 'n', 'ŋ̊', 'ŋ̩']

# Semivowels
smv_y = '*y'
smv_y_opt = ['j', 'i', 'iː', 'y', 'yː']

smv_w = '*w'
smv_w_opt = ['u', 'uː', 'w', 'ʋ']

"""
Vowels and Diphthongs 
"""

# Vowels
vwl_e = '*e'
vwl_e_opt = ['e', 'ø', 'ə', 'ɛ', 'ɜ', 'ɪ', 'æ', 'œ']
vwl_ee = '*ē'
vwl_ee_opt = ['eː', 'øː', 'əː', 'ɛː', 'ɜː', 'ɪː', 'æː', 'œː']
vwl_o = '*o'
vwl_o_opt = ['o', 'o̞', 'ɔ', 'ɤ', 'ʌ', 'ʊ', 'ə', 'ɵ']
vwl_oo = '*ō'
vwl_oo_opt = ['oː', 'ɔː', 'ʊː', 'əː', 'ɵː']

# Diphthongs
dip_ay = 'ay'
dip_ay_opt = ['aɪ', 'ɑɪ', 'aɨ', 'æi']
dip_aay = 'āy'
dip_aay_opt = ['aɪː', 'æːɪ', 'ai', 'æy']

dip_ey = 'ey'
dip_ey_opt = ['eɪ', 'ei', 'əɪ', 'ɜɪ', 'ɛɪ', 'əɪ', 'əi']
dip_eey = 'ēy'
dip_eey_opt = ['eɪː', 'øyː']

dip_oy = 'oy'
dip_oy_opt = ['ɔɪ', 'oi', 'oɪ', 'oʊ', 'øi', 'øy']
dip_ooy = 'ōy'
dip_ooy_opt = ['œː', 'oʊː', 'oeː', 'øyː', 'œy']

dip_aw = 'aw'
dip_aw_opt = ['aʊ', 'au']
dip_aaw = 'āw'
dip_aaw_opt = ['aʊː', 'æːʊ']

dip_ew = 'ew'
dip_ew_opt = ['eʊ', 'əʊ', 'ɛʊ']
dip_eew = 'ēw'
dip_eew_opt = ['eu', ]

dip_ow = 'ow'
dip_ow_opt = ['əʊ', 'ɔɪ', 'ɔʊ', 'ʌʊ',  'oʊ']
dip_oow = 'ōw'
dip_oow_opt = ['œː', 'oʊː', 'ou']

# Sound Law
color_h1e = 'h₁e'
color_h1e_opt = ['h₁e', 'h₁a', 'h₁o']
color_eh1 = 'eh₁'
color_eh1_opt = ['ēh₁', 'āh₁', 'ōh₁']
color_h2e = 'h₂e'
color_h2e_opt = ['h₂a', 'h₂e', 'h₂o']
color_eh2 = 'eh₂'
color_eh2_opt = ['āh₂', 'ēh₂', 'ōh₂']
color_h3e = 'h₃e'
color_h3e_opt = ['h₃o', 'h₃e', 'h₃a']
color_eh3 = 'eh₃'
color_eh3_opt = ['ōh₃', 'ēh₃', 'āh₃']
