from flask import Flask, render_template, request
from pessoa import *

app = Flask(__name__)

@app.route("/")
def iniciar(): 
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", lista = pe)

@app.route("/excluir_pessoa")
def excluir_pessoa():
    excluir = None
    cpf = request.args.get("cpf")
    for i in pe:
        if cpf == i.cpf:
            excluir = i
            break
    if excluir != None:
        pe.remove(excluir)

    return listar_pessoas()


@app.route("/inserir_pessoas")
def inserir_pessoas():
    return render_template("inserir_pessoas.html")

@app.route("/adicionar")
def adicionar():
    nomm = request.args.get("nome")
    ende = request.args.get("endereco")
    cpfe = request.args.get("cpf")
    tele = request.args.get("telefone")
    pe.append((Pessoa(nomm, ende, cpfe, tele)))
    return listar_pessoas()

    
app.run()