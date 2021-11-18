import transformers as tr
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    user_input = input('Introduzca el inicio de su frase: ')

    generator = tr.pipeline("text-generation", model="PlanTL-GOB-ES/gpt2-base-bne")
    generator(
        text_inputs = user_input,
        max_length=200,
        num_return_sequences=10,
        framework = 'tf'
    )

    return render_template('main_page.html', user_output = generator)

if __name__ == '__main__':
    app.run(debug=False)