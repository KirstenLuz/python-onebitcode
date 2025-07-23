"""
Agendamento de desligamento do pc
-> Crie duas funções em python para agendar o desligamento do computador
em um hora, meia hora e cancelar o cancelamento.
"""
import os

# 1 - Desligar o computador
# os.system("shutdown /s") - Desliga em 60s
# os.system("shutdown /s /t 0") - Desliga o computador imediatamente (em 0s)
# os.system("shutdown now") - Linux (desliga na mesma hora)

# 2 - Cancelar desligamento
# os.system("shutdown /a")


def turn_off_one_hour():
    os.system("shutdown /s /t 3600")


def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")


def cancel_shutdown():
    os.system("shutdown /a")


turn_off_one_hour()
cancel_shutdown()
