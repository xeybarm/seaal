# coding=utf-8

from soz_analizi.shekilci import *
from soz_analizi.stringler import *

from soz_analizi.n_isim import *
from soz_analizi.n_feil import *
from soz_analizi.n_sifet import *
from soz_analizi.n_say import *
from soz_analizi.n_evezlik import *
from soz_analizi.n_zerf import *
sait=['a', 'ı', 'o', 'u','e', 'ə' , 'i', 'ö', 'ü']
istisna=['tale', 'mənbə', 'mövqe', 'mənşə', 'nə', 'mənafe']
istisna1=['isim', 'qisim', 'nəsil', 'fikir', 'ətir', 'səbir', 'qəbir','heyif','sətir','qədir','ömür', 'sinif',
 'eyib', 'şəkil', 'meyil', 'əsil', 'fəsil', 'xeyir', 'zehin']
istisna2=['beyin','ağıl','alın','burun','ağız','boyun','qoyun','çiyin','oğul','qarın','əyin','qayın']   #qoyun is omonim both versions should work but do not know how

#################################################
#############
