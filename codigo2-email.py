# _*_ coding: utf-8 _*_
# Iniciando à programação - Envio de Email
__author__ = "Tulio Dias"
__copyright__ = "Copyright 2019, Túlio Vilela Dias"
__credits__ = "Túlio"
__license__ = "MIT"
__maintainer__ = "Tulio Dias"
__email__ = "tuliovilela7@hotmail.com"

# Bibliotecas para envio de email
# Se não tiver instalada, será necessário instalar através do "pip install smtplib"
import email.message
import smtplib

email_sender = "tuliodias@inatel.br" #Coloque aqui seu Email Inatel
email_password = "sua_senha" #Coloque aqui sua Senha Inatel

destinatarios = []
#destinatarios.append("tuliovilela7@hotmail.com") #Adicionando destinatario(s)
#destinatarios.append("tuliovilela@gea.inatel.br") #Adicionando destinatario(s)
destinatarios.append("mellina@inatel.br") #Adicionando destinatario(s)

def send_email(assunto,message,destinatarios,meu_email,senha):  #FUNÇÃO PARA ENVIO DE EMAIL
    # Configuração do Envio do email
    msg = email.message.Message()
    msg['From'] = meu_email
    msg['Subject'] = assunto
    msg.add_header('Content-Type', 'text/html; charset=utf-8')
    msg.add_header('Content-Disposition', 'inline')
    msg.add_header('Content-Transfer-Encoding', '8bit')
    msg.set_payload(message.encode('utf-8'))
    # Configuração do Gerenciador de Email
    server = smtplib.SMTP('outlook.office365.com: 587')
    server.starttls()
    # Fazendo Login para enviar o email
    server.login(msg['From'], senha)
    # Enviando o email 
    server.sendmail(msg['From'], destinatarios, msg.as_string())
    # Trabalho feito, desconectando
    server.quit()

assunto_do_email = "UHULLLLLL" #Edite o Assunto
mensagem_do_email = "Mellina esta aprendendo a programar." #Edite a mensage

send_email(assunto_do_email,mensagem_do_email,destinatarios,email_sender,email_password) #Chamando função de envio de email.