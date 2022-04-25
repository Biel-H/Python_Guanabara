#ANSI escape sequence é o padrão de normalização internacional. Tudo nele começa com "contra barra" e um código
#Um código de cor bom para o python é o:
from tkinter.font import BOLD


\033[m 

#Entre o colchetes e o "M" você ira adicionar os códigos sendo a ordem -> style (estilo da fonte), -> text (Cor do texto), back (cor de fundo)
\033[0;33;44m

#Os melhores codigos para estilo no python são [0, 1, 4, 7] 
0 - None
1 - Bold
4 - Underline
7 - negative

#Em text você tem de 30 - 37 onde cada numero é uma cor. 
# site que mostra as cores e demais configurações: 
https://pythonhoje.wordpress.com/2018/01/28/python-3-cores/

#Já as cores de background vão de 40 - 47 e seguem a coloração própria mas isso também esta listado no site acima

#Enfim qualquer coisa também da pra ver a aula do guanabara
https://www.youtube.com/watch?v=0hBIhkcA8O8