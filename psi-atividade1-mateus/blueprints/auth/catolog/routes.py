from flask import render_template, abort, request
import catalog_bp
import models

@catalog_bp.route("/")
def index():
    livros = models.buscar_livros()
    busca = request.args.get("busca", "")

    if busca:
        livros = [
            livro for livro in livros
            if busca.lower() in livro["titulo"].lower()
        ]

    return render_template("catalog/index.html", livros=livros, busca=busca)

@catalog_bp.route("/livro/<int:livro_id>")
def ver_livro(livro_id):
    livro = models.buscar_livro(livro_id)

    if not livro:
        abort(404)

    criticas = models.buscar_criticas(livro_id)
    return render_template("catalog/livro.html", livro=livro, criticas=criticas)