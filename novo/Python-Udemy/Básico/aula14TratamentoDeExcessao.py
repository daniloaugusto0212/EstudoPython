try: #Se o usuário digitar um valor int o pragrama aceita
    idade = int(input('Digite sua idade: ')) 

except: #Caso o usuário digite um valor que não seja 'int', mostra a mesnsagem
    print("Você não digitou sua idade. ") 
    
else: #Caso não houver excessão, mostra a idade
    print(f'Sua idade é {idade}') 

finally: #exceculta o camando independente do que acontecer
    print('Muito obrigado, volte sempre! ') 

