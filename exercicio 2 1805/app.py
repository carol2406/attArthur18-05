from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = ""

    if request.method == "POST":

        morador = request.form.get("morador")
        carro = request.form.get("carro")
        horario = request.form.get("horario")

        if morador == "sim" and carro == "sim" and horario == "sim":
            estado = "🚗 Portão Aberto"
            mensagem = "✨ Acesso liberado"

        else:
            estado = "🔒 Portão Fechado"

            if morador == "nao":
                mensagem = "❌ Acesso negado"

            elif carro == "sim" and horario == "nao":
                mensagem = "⏳ Aguardar liberação"

            else:
                mensagem = "⚠️ Condições não atendidas"

        resultado = f"""
        {estado}<br>
        {mensagem}
        """

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)