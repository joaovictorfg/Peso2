#! /usr/bin/env python
#-*- coding: UTF-8 -*-

import math
import os, sys

print( 'IMC')

peso = raw_input (' Digite seu peso e aperte enter: ')
altura = raw_input ('Digite a sua altura e aperte enter: ')
imc = float(peso)/(float(altura)*float(altura))

#print 'Seu IMC é : ', imc

if imc <= 17.0:
    print ("Atenção! Você está abaixo do peso ideal")
if imc > 17.0 and imc <= 18.49:
    print "Seu IMC é: ", imc
    print "Você está em seu peso normal"
if imc > 18.5 and imc <= 24.99:
     print "Seu IMC é: " , imc
     print "Atenção! Você está acima de seu peso(sobrepeso)"
if imc > 25.0 and imc <= 29.99:
    print "Seu IMC é: ", imc
    print "Atenção! Obesidade Grau I"
if imc > 35.0 and imc <= 39.9:
    print "Seu IMC é: ", imc
    print "Atenção! Obesidade Grau II"
if imc > 40.0:
    print "Seu IMC é: " , imc
    print "Atenção! Obesidade Grau III"
    print
    print "Fim do Programa"
