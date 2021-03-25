import math
import numpy as np

def generate_random_samples(K, N, R, seed):
    '''
    Generates K random numpy N x N matrices which are cost matrices (i.e symmetric, with main diagonal all zeros)
    with integer costs in the range 0 to 2*R
    Will always generate the same K matrices given a constant seed
    '''
    np.random.seed(seed)
    matrixList = list()
    for i in range(K):
        mat = np.random.random_integers(0,R,size=(N, N))
        skewsym_mat = (mat - mat.T)/2 # To ensure the diagonal is all zero values
        sym_mat = abs(skewsym_mat) # To ensure the matrix is now symmetric
        sym_mat *= 2 # To ensure all integer distances
        matrixList.append(sym_mat)
    return matrixList

def make_dist_matrix(n):
    """ Utility function to make triangular distance matrices
        Input: n is a list of tuples corresponding to points in 2D Euclidean space
        Output: Symmetric distance matrix giving distances between all pairs of points 
                (using Euclidean distance)
    """
    distMat = [ [0 for j in range(len(n))]
             for i in range(len(n))]
    for i in range(len(n)):
        for j in range(i, len(n)):
           dist = math.sqrt((n[i][0] - n[j][0])**2 + (n[i][1] - n[j][1])**2)
           distMat[i][j] = distMat[j][i] = dist
    return distMat

mat1 = [[  0,   1, 1, 1.5],
       [  1,   0, 1.5, 1],
       [  1, 1.5,   0, 1],
       [1.5,   1,   1, 0]]  # Distance Matrix

example2 = [(10.0, 20.0),
(15.0, 3.0),
(25.0, 12.0),
(17.0, 42.0),
(67.0, 25.0),
(35.0, 27.0)]

example3 = [(565.0, 575.0),
(25.0, 185.0),
(345.0, 750.0),
(945.0, 685.0),
(845.0, 655.0),
(880.0, 660.0),
(25.0, 230.0),
(525.0, 1000.0),
(580.0, 1175.0),
(650.0, 1130.0),
(1605.0, 620.0),
(1220.0, 580.0),
(1465.0, 200.0),
(1530.0, 5.0),
(845.0, 680.0),
(725.0, 370.0),
(145.0, 665.0),
(415.0, 635.0),
(510.0, 875.0),  
(560.0, 365.0),
(300.0, 465.0),
(520.0, 585.0),
(480.0, 415.0),
(835.0, 625.0),
(975.0, 580.0),
(1215.0, 245.0),
(1320.0, 315.0),
(1250.0, 400.0),
(660.0, 180.0),
(410.0, 250.0),
(420.0, 555.0),
(575.0, 665.0),
(1150.0, 1160.0),
(700.0, 580.0),
(685.0, 595.0),
(685.0, 610.0),
(770.0, 610.0),
(795.0, 645.0),
(720.0, 635.0),
(760.0, 650.0),
(475.0, 960.0),
(95.0, 260.0),
(875.0, 920.0),
(700.0, 500.0),
(555.0, 815.0),
(830.0, 485.0),
(1170.0, 65.0),
(830.0, 610.0),
(605.0, 625.0),
(595.0, 360.0),
(1340.0, 725.0),
(1740.0, 245.0)]

example4 = [(155.42, 150.65),
(375.92, 164.65),
(183.92, 150.65),
(205.42, 1,50.65),
(205.42, 171.65),
(226.42, 171.65),
(226.42, 186.15),
(226.42, 207.15),
(226.42, 235.65),
(226.42, 264.15),
(226.42, 292.65),
(226.42, 314.15),
(226.42, 335.65),
(205.42, 335.65),
(190.92, 335.65),
(190.92, 328.15),
(176.92, 328.15),
(176.92, 299.65),
(155.42, 299.65),
(155.42, 328.15),
(155.42, 356.65),
(183.92, 356.65),
(219.42, 356.65),
(240.92, 356.65),
(269.42, 356.65),
(290.42, 356.65),
(387.42, 136.15),
(318.92, 356.65),
(318.92, 335.65),
(318.92, 328.15),
(318.92, 299.65),
(297.92, 299.65),
(290.42, 328.15),
(290.42, 335.65),
(297.92, 328.15),
(254.92, 335.65),
(254.92, 314.15),
(254.92, 292.65),
(254.92, 271.65),
(254.92, 243.15),
(254.92, 221.65),
(254.92, 193.15),
(254.92, 171.65),
(276.42, 171.65),
(296.42, 150.65),
(276.42, 150.65),
(375.92, 150.65),
(308.92, 150.65),
(354.92, 164.65),
(338.42, 174.65),
(354.92, 174.65),
(338.42, 200.15),
(338.42, 221.65),
(354.92, 221.65),
(354.92, 200.15),
(361.92, 200.15),
(361.92, 186.15),
(383.42, 186.15),
(383.42, 179.15),
(404.42, 179.15),
(404.42, 186.15),
(418.92, 186.15),
(418.92, 200.15),
(432.92, 200.15),
(432.92, 221.65),
(418.92, 221.65),
(418.92, 235.65),
(397.42, 235.65),
(397.42, 243.15),
(375.92, 243.15),
(375.92, 257.15),
(368.92, 257.15),
(368.92, 264.15),
(347.42, 264.15),
(347.42, 278.65),
(336.42, 278.65),
(336.42, 328.15),
(347.42, 328.15),
(347.42, 342.65),
(368.92, 342.65),
(368.92, 353.65),
(418.92, 353.65),
(418.92, 342.65),
(432.92, 342.65),
(432.92, 356.65),
(447.42, 356.65),
(447.42, 321.15),
(447.42, 292.65),
(432.92, 292.65),
(432.92, 314.15),
(418.92, 314.15),
(418.92, 321.15),
(397.42, 321.15),
(397.42, 333.65),
(375.92, 333.65),
(375.92, 321.15),
(361.92, 321.15),
(361.92, 299.65),
(375.92, 299.65),
(375.92, 285.65),
(397.42, 285.65),
(397.42, 271.65),
(418.92, 271.65),
(418.92, 264.15),
(439.92, 264.15),
(439.92, 250.15),
(454.42, 250.15),
(454.42, 243.15),
(461.42, 243.15),
(461.42, 214.65),
(461.42, 193.15),
(447.42, 193.15),
(447.42, 179.15),
(439.92, 179.15),
(439.92, 167.65),
(419.92, 167.65),
(419.92, 150.65),
(439.92, 150.65),
(454.42, 150.65),
(475.92, 150.65),
(475.92, 171.65),
(496.92, 171.65),
(496.92, 193.15),
(496.92, 214.65),
(496.92, 243.15),
(496.92, 271.65),
(496.92, 292.65),
(496.92, 317.15),
(496.92, 335.65),
(470.42, 335.65),
(470.42, 356.65),
(496.92, 356.65),
(347.42, 150.65),
(539.92, 356.65),
(560.92, 356.65),
(589.42, 356.65),
(589.42, 342.65),
(603.92, 342.65),
(610.92, 342.65),
(610.92, 335.65),
(610.92, 321.15),
(624.92, 321.15),
(624.92, 278.65),
(610.92, 278.65),
(610.92, 257.15),
(589.42, 257.15),
(589.42, 250.15),
(575.42, 250.15),
(560.92, 250.15),
(542.92, 250.15),
(542.92, 264.15),
(560.92, 264.15),
(575.42, 264.15),
(575.42, 271.65),
(582.42, 271.65),
(582.42, 285.65),
(596.42, 285.65),
(560.92, 335.65),
(596.42, 314.15),
(582.42, 314.15),
(582.42, 321.15),
(575.42, 321.15),
(575.42, 335.65),
(525.42, 335.65),
(525.42, 314.15),
(525.42, 299.65),
(525.42, 281.65),
(525.42, 233.15),
(525.42, 214.65),
(525.42, 193.15),
(525.42, 171.65),
(546.92, 171.65),
(546.92, 150.65),
(568.42, 150.65),
(475.92, 160.65),
(603.92, 150.65),
(624.92, 150.65),
(624.92, 136.15),
(596.42, 136.15),
(575.42, 136.15),
(553.92, 136.15),
(532.42, 136.15),
(575.42, 356.65),
(489.92, 136.15),
(468.42, 136.15),
(447.42, 136.15),
(425.92, 136.15),
(404.42, 136.15),
(370.42, 136.15),
(361.92, 150.65),
(340.42, 136.15),
(326.42, 136.15),
(301.92, 136.15),
(276.42, 136.15),
(254.92, 136.15),
(315.92, 136.15),
(212.42, 136.15),
(190.92, 136.15),
(338.92, 150.65),
(155.42, 136.15),
(624.92, 299.65),
(318.92, 321.65),
(155.42, 314.15),
(311.92, 356.65),
(355.42, 136.15),
(318.92, 314.15),
(362.92, 164.65),
(254.92, 356.65),
(383.42, 333.65),
(447.42, 335.65),
(470.42, 345.65),
(525.42, 250.15),
(546.92, 335.65),
(525.42, 261.15),
(525.42, 356.65),
(336.42, 298.65),
(336.42, 313.15),
(293.42, 136.15),
(336.42, 306.15),
(425.92, 264.15),
(391.42, 353.65),
(482.92, 335.65),
(429.92, 167.65),
(330.92, 150.65),
(368.42, 150.65)]

example5 = [(1.75, 3.00),
(2.50, 4.00),
(1.00, 1.00),
(7.95, 10.0),
(11.2, 100),
(85.1, 0.00),
(25.2, 9.50),
(76.3, 11.2),
(95.0, 55.3),
(10.5, 93.6),
(15.2, 12.1),
(50.6, 51.2),
(47.1, 99.9),
(100, 0.00),
(123, 10.0),
(43.1, 12.5),
(99.1, 65.9),
(35.2, 77.6),
(34.6, 12.0),
(11.1, 11.1),
(89.4, 150),
(95.1, 1.25),
(10.5, 77.5),
(30.0, 70.0),
(11.1, 99.9),
(17.5, 87.5),
(24.1, 19.2),
(88.3, 88.3),
(100, 1.23),
(7.14, 9.99),
(15.2, 23.1),
(19.4, 67.1),
(98.0, 2.95),
(12.4, 19.6),
(196, 15.0),
(34.1, 52.1),
(11.4, 24.1),
(56.4, 125 ),
(44.4, 66.6),
(65.1, 96.4),
(14.9, 76.3),
(64.1, 88.8),
(35.0, 24.0),
(85.5, 99.0),
(4.59, 11.0),
(79.3, 12.3),
(55.5, 1.27),
(36.1, 0.00),
(59.0, 23.0),
(1.00, 99.0)]

example6 = [(100,73),
(25,250),
(500,10),
(0,45),
(16,20),
(75,57),
(420,69),
(245,145),
(139,29),
(90,470),
(134,224),
(234,567),
(145,354),
(64,256),
(125,225),
(11.1, 99.9),
(17.5, 87.5),
(24.1, 19.2),
(88.3, 88.3),
(100, 1.23),
(7.14, 9.99),
(15.2, 23.1),
(19.4, 67.1),
(98.0, 2.95)]