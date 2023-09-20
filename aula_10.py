# -*- coding: utf-8 -*-
"""Aula 10

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A-yFi7__burMXYyR20nM0-9RwJ940p-3

Em Python, um dicionário é uma estrutura de dados que permite armazenar e recuperar valores associados a chaves únicas. Os dicionários são conhecidos como "dicts" e são muito úteis quando você precisa mapear chaves para valores. Eles são implementados como tabelas de hash, o que os torna eficientes para pesquisa e recuperação de valores.

Aqui está uma introdução básica sobre como usar dicionários em Python:

### **Criando um dicionário:**

Você pode criar um dicionário usando chaves **`{}`** ou a função **`dict()`**. Aqui está um exemplo simples:
"""

# Usando chaves {}
my_dict = {'nome': 'Alice', 'idade': 30, 'cidade': 'Nova York'}
print(my_dict)

# Usando a função dict()
my_dict = dict(nome='Alice', idade=30, cidade='Nova York')
print(my_dict)

"""FUNÇÕES COM LOOP:"""

def imprimir_numeros(n):
    for i in range(1, n + 1):
        print(i)

# Exemplo de uso
imprimir_numeros(5)

#Este código calculará a soma dos números de 1 a 5 e imprimirá o resultado.