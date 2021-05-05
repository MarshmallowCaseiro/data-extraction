#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

"""
Main module

This script analyses the numerical solution of a pack of simulations altering
the Schmidt Value. The aim of this code is to analyse the impact of this value
on the mass exchange and mass behaviour within the solution.
"""

import sys	#Operações de sistema
import os	#Operações de sistema de arquivos e caminhos
import shutil	#Operações de sistema de arquivos e caminhos
import time	#Operações de tempo

# Imports modules
sys.path.append('bin/')  #Muda o caminho para os próximos módulos como importDAT.py ou o dataProcess.py
import importDAT	 #Indica qual módulo será importado
import dataProcess
import plot

start_time = time.time()

if __name__ == '__main__':	#Checa se está sendo rodado como módulo ou função principal (Verdadeiro se função principal)
    def cls():
        """
        Clears the prompt
        """
        os.system('cls' if os.name=='nt' else 'clear')

    # Check for necessary directories
    folder = 'preTreatment'
    if not os.path.exists(folder):
        os.makedirs(folder)
        print("The directory treatment/ was created, please populate with the "
            "desired csv files to be analysed.")
        sys.exit('The directory treatment/ did not exist.')
    elif not os.listdir(folder):
        sys.exit('The directory treatment/ is empty.')

    # Clear the previous results directories
    res = 'treatment/results'
    if os.path.exists(res):
        shutil.rmtree(res)
    os.makedirs(res)

    # Chama os módulos importados
    mass = importDAT.run()    #Note que no arquivo importDAT, todo o código está sob uma função chamada "run" e que a execução como módulo principal está bloqueada
    massProcess_V, massProcess_N = dataProcess.run(mass)	#Esta função irá requerer o resultado da anterior desta forma você pode alimentá-la desta forma ou fazer uma atrocidade como comentado abaixo:
    plot.run(massProcess_V, massProcess_N)    #Função retorna o plot

print("""All Done.
Check directory preTreatment/results
Execution Time %.3f seconds""" %(time.time() - start_time))
del start_time
