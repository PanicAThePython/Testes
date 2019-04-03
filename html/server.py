from flask import Flask, render_template, request
from pessoa import *

app = Flask(__name__)

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route("/listar")
def listar():
    return render_template("listar.html", pessoas = lista)

@app.route("/inserir")
def inserir():
    return render_template("inserir.html")

@app.route("/adicionar")
def adicionar():
    
    nome = request.args.get("nome")
    cpf  = request.args.get("cpf")

    lista.append(Pessoa(nome, cpf))

    return listar()

@app.route("/excluir")
def excluir():

    excluir = None

    cpf  = int(request.args.get("cpf"))

    for p in lista:
        if p.cpf == cpf:
            excluir = p
            break
    if excluir != None:
        lista.remove(excluir)

    return listar()

app.run()