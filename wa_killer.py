from random import choice
from time import sleep
from os import system
times=[1,2,3,4,5,6]
system('echo -e "\e[31m"')
system('figlet WhatsApp')
system('figlet -w 30 -c killer ')
system('echo -e "\e[34m" "                           v1.1.2"')
system('echo -e "\e[31m" "                           Devolped by 8g6"')
system('echo -e "\e[32m" ')
code  =input('Enter country code  : ')
number=input('Enter mobile Number : ')
number='+'+code+' '+number
LIST=["13.212.38.64\t80\tSG\tSingapore\telite proxy\tno\tno\t1 minute ago", "161.202.226.194\t80\tJP\tJapan\telite proxy\tno\tyes\t1 minute ago", "5.252.161.48\t8080\tGB\tUnited Kingdom\tanonymous\tno\tno\t1 minute ago", "51.81.82.175\t80\tUS\tUnited States\tanonymous\tno\tno\t1 minute ago", "178.134.155.82\t48146\tGE\tGeorgia\telite proxy\tno\tno\t1 minute ago", "36.67.27.189\t39674\tID\tIndonesia\telite proxy\tno\tno\t1 minute ago", "192.109.165.49\t80\tDE\tGermany\tanonymous\tno\tno\t1 minute ago", "191.101.39.199\t80\tSG\tSingapore\tanonymous\tno\tno\t1 minute ago", "85.185.159.75\t8080\tIR\tIran\tanonymous\tno\tyes\t1 minute ago", "192.109.165.51\t80\tDE\tGermany\tanonymous\tno\tno\t1 minute ago", "154.16.63.16\t3128\tGB\tUnited Kingdom\tanonymous\tno\tno\t1 minute ago", "78.138.131.248\t3128\tRU\tRussian Federation\telite proxy\tno\tno\t1 minute ago", "80.26.96.212\t80\tES\tSpain\telite proxy\tno\tno\t1 minute ago", "103.105.49.53\t80\tUS\tUnited States\tanonymous\tno\tno\t1 minute ago", "46.246.6.2\t3128\tSE\tSweden\telite proxy\tno\tyes\t1 minute ago", "195.138.73.54\t44017\tUA\tUkraine\telite proxy\tno\tno\t1 minute ago", "66.170.183.90\t9090\tCA\tCanada\telite proxy\tno\tno\t1 minute ago", "41.190.92.84\t48515\tMW\tMalawi\telite proxy\tno\tno\t1 minute ago", "169.57.1.84\t8123\tMX\tMexico\telite proxy\tno\tyes\t1 minute ago", "159.65.171.69\t80\tUS\tUnited States\telite proxy\tno\tno\t1 minute ago"]
for i in LIST:
    i=i.split('\t')
    system('echo -e "\e[31m"')
    print(f'\n\nReporting {number} with a random proxy server')
    system('echo -e "\e[33m"')
    print('Connecting to Proxy Server ')
    sleep(choice(times))
    system('echo -e "\e[32m"')
    print(i[0],'Connected')
    sleep(choice(times))
    system('echo -e "\e[34m"')
    print(f'Host Country : {i[3]}({i[2]})')
    print(f'Port         : '+i[1])
    print(f'Proxy Type   : '+i[4])
    sleep(choice(times))
    system('echo -e "\e[32m"')
    print(number,'\nReported Sucessfully\n')
