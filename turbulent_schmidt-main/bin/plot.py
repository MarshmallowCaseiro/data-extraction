#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plot.py
#  
#  Copyright 2021 Filipe Queiroz
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Libraries
import sys
from matplotlib import pyplot as plt

if __name__ == '__main__':
    sys.exit('This file should be executed as a module.')
    
def run(massProcess_V, massProcess_N):
    
    # Cria os gráficos
    fig, axis = plt.subplots(figsize = (9, 6), dpi = 300)
    axis2 = axis.twinx()
    
    # Eixos vegetados
    eixo_xv = massProcess_V.Schmidt_number
    eixo_yv = massProcess_V.K
    
    # Eixos não-vegetados
    eixo_yn = massProcess_N.K
    
    # Cria os pontos dos gráficos
    ln1 = axis.plot(eixo_xv, eixo_yv, lw = 0, ms = 5, label='Vegetated', color = 'r', marker = 'o')
    ln2 = axis2.plot(eixo_xv, eixo_yn, lw = 0, ms = 5, label='Non vegetated', color = 'b', marker = 's')
    
    # Adiciona legenda
    lns = ln1+ln2
    labs = [l.get_label() for l in lns]
    axis.legend(lns, labs, loc=7)
    
    # Adiciona nome dos eixos
    axis.set_xlabel('$Sc_{t}$', size=15)
    axis.set_ylabel('$k_{Vegetated}$', size=15)
    axis2.set_ylabel('$k_{NonVegetated}$', size=15)
    
    #plt.show()
    #plt.autoscale(enable=True, tight=True)
    #plt.grid()
    
    # Salva o gráfico
    plt.savefig('preTreatment/results/plot/massDecaySemiLogY.png', bbox_inches='tight')
