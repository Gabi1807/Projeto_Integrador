from flask import Flask, render_template, request, Response, url_for
import Banco
import json

app = Flask(__name__)
db = Banco


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    cnpj = db.Column(db.String(12))
    cidade = db.Column(db.String(20))
    estado = db.Column(db.String(20))
    ramo = db.Column(db.String(20))
    conduta = db.Column(db.String(20))

    def to_json(self):
        return {"id": self.id, "nome": self.nome_empresa, "cnpj": self.cnpj, "cidade": self.cidade,
                "estado": self.estado, "ramo": self.ramo, "conduta": self.conduta}


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if (mensagem):
        body["mensagem"] = mensagem

        return Response(json.dumps(body), status=status, mimetype="application/json")


@app.route("/", methods=["GET"])
def seleciona_empresas():
    empresas_objetos = Empresa.query.all();
    empresas_json = [empresa.to_json() for empresa in empresas_objetos]
    return  render_template("index.html", empresas=empresas_objetos)
