## Desafio-de-Programação
Esses códigos tem como objetivo solucionar as questões do desafio de programação da Capgemini. A linguagem de programação escolhida para responder às questões foi Python. Contém 3 arquivos .py os quais cada um é uma função que responde diretamente a cada questão do desafio.

## Instalação
Após o download pode ser executado com qualquer software que leia python.

## Uso
Cada arquivo corresponde à resolução de uma questão, tais estão enumerados de acordo com a questão que respondem.

            #Questão 1:
              escada(n) --- retorna a string em escada com "*".
                -> n : deve ser um inteiro.
                
            #Questão 2:
              senhaforte(senha) --- retorna uma string que corresponde a cada um dos casos para a senha inserida ser uma senha forte: 
                                            -O número de caracteres que faltam para a quantidade mínima;
                                            -Se faltam um dos seguintes caracteres: letra minúscula, letra maiúscula, dígito, caractere especial;
                                            -"Sua senha é forte!" caso cumpra todos os requisitos.
                -> senha : deve ser uma string.
                
            #Questão 3:
              anagrama(st)  --- retorna o número de pares de anagramas possíveis da string.
                -> st : deve ser uma string.
              
            
## Desenvolvimento
#Questão 1:
Foi usado um ciclo for, o qual se repete o mesmo número de vezes do inteiro (n) inserido para adicionar as linhas à string. Foi criada uma condição if para separar a primeira linha das demais, para não incluir a expressão '\n' que foi usada para fazer a quebra de linha das demais. Todas as linhas se alteram decrescendo o número de espaços " " e incrementando o número de "*".

#Questão 2:
O código retorna diretamente o número de caracteres extras necessários caso o tamanho da senha seja menor 6. Caso siga, cada caractere é analisado num ciclo for e passa por 4 condições as quais, caso verificadas aumentam a variável correspondente a cada condição em 1. Para que a senha seja forte, todas as variáveis precisam ter valores maiores do que 1. Caso contrário retorna qual incremento precisa ser feito.

#Questão 3:
Para definir os anagramas possíveis são feitos ciclos em cadeia, o primeiro ciclo (while), altera a quantidade de caracteres no anagrama. A comparação é feita definindo um conjunto de referência dentro de um ciclo for. Em seguida, inserido dentro deste ciclo, outro ciclo for é feito gerando as combinações de caracteres seguintes. São comparadas a string de referência e a sequente, caso contenham os mesmos caracteres, independente da ordem, são consideradas anagramas e incrementam o total de anagramas pares em 1. 
