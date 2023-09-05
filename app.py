from flask import Flask, render_template

app = Flask("meu App")

posts = [
    {
        "titulo":"Primeira",
        "texto":"Postagem nesse blog daora pa carai"
    },
    {
        "titulo":"Segundo",
        "texto":"Mais uma postagem nesse blog daora pa carai"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts
    return render_template("entradas.html", entradas=entradas)