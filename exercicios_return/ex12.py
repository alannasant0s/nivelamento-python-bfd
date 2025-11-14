"""Crie uma função eh_bissexto(ano) que retorne True se o ano for bissexto.
"""


def eh_bissexto(ano):
    if (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0):
        return True
    else:
        return False
    
ano = eh_bissexto(2028)
print(f"O ano é bissexto? : {ano}")