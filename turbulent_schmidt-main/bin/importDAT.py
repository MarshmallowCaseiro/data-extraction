#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  importDAT.py
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

# Libraries
import os
import sys
import re
import pandas as pd

if __name__ == '__main__':
    sys.exit('This file should be executed as a module.')

def run():
    
    # Base directory
    folder = "preTreatment/"
    files = os.listdir(folder)

    # Scan Files
    datFiles = list()

    for item in files:
        if re.search('.\.dat', item):
            datFiles.append(item)
            
    datFiles.sort()

    # Extraction of variable name and case number  #Este bloco não tem muita utilidade no momento, porém se colocar para importar mais variáveis ele pode ser útil.
    uniqueCase = list()

    for item in datFiles:
        re.search('.dat', item)
        numberCase = re.split('_', item)[1]
        numberCase = re.split('\.', numberCase)[0]
        if numberCase not in uniqueCase:    #Caso a simulação no exista na lista uniqueCase ela é adicionada
            uniqueCase.append(numberCase)

    mass = dict()
    for item in datFiles: #Loop entre todos os arquivos
        for item2 in uniqueCase: #Loop entre todas as simulações
            ii = re.split("_", item)[1]
            if re.split("\.", ii)[0] == item2:
                mass[item2] = pd.read_csv(folder+item, delimiter='\t', header = 3) #Importa o arquivo para o nome 
                mass[item2].columns = ['time', 'tracerVol']
                mass[item2].tracerVol[0] = 1 #Correção do valor inicial de traçador
                massTimeZero = mass[item2].time[0]   #Valor do primeiro tempo em que o traçador rodou (e.g. 150s)
                mass[item2].time = mass[item2].time - massTimeZero  #Correção do tempo inicial de traçador (e.g. 150s para 0s)
    return mass