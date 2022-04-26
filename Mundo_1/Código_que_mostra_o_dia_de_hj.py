from datetime import datetime
import locale
#função principal do programa
def main():
    #configurações do usuário
    locale.setlocale(locale.LC_ALL,'')
    #Obtém um datetime da data e hora atual
    hoje = datetime.today()
    #exibe o nome do dia da semana em formato longo
    print('O dia da semana é:', hoje.strftime('%A'))

if __name__=='__main__':
    main()
