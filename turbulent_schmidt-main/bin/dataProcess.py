#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dataProcess.py
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
import pandas as pd
from scipy import optimize
import numpy as np

if __name__ == '__main__':
    sys.exit('This file should be executed as a module.')

def run(mass):
    W = 0.15  #[m]
    U = 0.101 #[m/s] 
    
    def model(x, td):  
        # First Order Mass Decay Equation
        return np.exp(-x/td)

    def sch_number(): #Cria lista de schmidt numbers
        sch = list()
    
        for i in range(20, 0, -1):
            sch.append(i/10)
    
        return(sch)
    
    massProcessed = dict() #Dicionário com os valores de td de cada simulação

    for item in mass: #Loop entre as chaves do dicionario de simulações 'mass'
        td, pcov = optimize.curve_fit(model, mass[item].time, mass[item].tracerVol, p0=(40), maxfev=5000)
        massProcessed[item] = td
            
    #Cria um dataFrame com os valores de td e o index como número da simulação
    massProcess = pd.DataFrame(data = massProcessed)
    massProcess = massProcess.transpose()
    massProcess.columns = ['td']
    
        # Adiciona a culuna K e Schmidt_number caso ainda não existam
    try:
        massProcess.eval("K = @W / (td * @U)", inplace = True)
        massProcess.insert(loc=2, column='Schmidt_number', value=2*sch_number())
    except:
        pass
        
    # Separando em dois dataFrames pelo index row
    massProcess['caseNumber'] = massProcess.index # Adiciona coluna caseNumber
    massProcess = massProcess[['caseNumber', 'Schmidt_number', 'td', 'K']] # Muda a ordem das colunas
    massProcess_V = massProcess.iloc[:20,:] # massProcess_V: cavidade vegetada
    massProcess_N = massProcess.iloc[20:,:] # massProcess_N: cavidade não vegetada
        
######################################################################################    
    # # Define Fitting Function
    # def model(x, td):
    #     return np.exp(-x/td)
    
    # massProcessed = dict() #Dicionário com os valores de td de cada simulação
    
    # for item in mass: #Loop entre as chaves do dicionario de simulações 'mass'
    #     td, pcov = optimize.curve_fit(model, mass[item].time, mass[item].tracerVol, p0=(40), maxfev=5000)
    #     massProcessed[item] = td
            
    # massProcess = pd.DataFrame(data = massProcessed)
    # massProcess.transpose()
    # massProcess.columns = ['td']
    # breakpoint()
    # massProcess.eval("k = @W / (td * @U)", inplace = True) #Adiciona nova coluna com os valores de 'k' calculados
    
    return massProcess_V, massProcess_N
