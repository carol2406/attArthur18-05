from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    resultado_casa = ""
    resultado_portao = ""

    if request.method == "POST":

        # CASA INTELIGENTE
        presenca = request.form.get("presenca")
        noite = request.form.get("noite")
        temperatura = float(request.form.get("temperatura"))

        if presenca == "sim" and noite == "sim":
            luz = "💡 Luz Ligada"
        else:
            luz = "🌑 Luz Desligada"

        if temperatura > 28:
            ventilador = "🌀 Ventilador Ligado"
        else:
            ventilador = "❄️ Ventilador Desligado"

        if noite == "sim" and presenca == "nao":
            alarme = "🚨 Alarme Ativado"
        else:
            alarme = "✅ Alarme Desativado"

        resultado_casa = f"""
        {luz}<br>
        {ventilador}<br>
        {alarme}
        """

        # PORTÃO INTELIGENTE
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

        resultado_portao = f"""
        {estado}<br>
        {mensagem}
        """

    return render_template(
        "index.html",
        resultado_casa=resultado_casa,
        resultado_portao=resultado_portao
    )

if __name__ == "__main__":
    app.run(debug=True)