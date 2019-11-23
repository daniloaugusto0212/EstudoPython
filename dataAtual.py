#algoritmo que mostra data atual

from datetime import date, time
dia = date.today().day
mes = date.today().month
ano= date.today().year


print (f'{dia}/{mes}/{ano}')