#####
#   BA    Amadou     16 187 314 
#   YING  Xu         18 205 032
#   ABOU Hamza       17 057 836
###

import os, sys

sys.path.append(os.path.dirname(os.path.join(os.getcwd())))
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from classifiers.abstract_classifier import AbstractClassifier


class  LinearDiscriminantClassifier(AbstractClassifier):
	def __init__(self, approch='0'):
		 super().__init__(LinearDiscriminantAnalysis(solver='lsqr',shrinkage=4.7e-06),approch)

