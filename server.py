from flask import Flask

app = Flask(__name__)

instruction = "WAIT"

@app.route("/")
def home():
    return "Instruction server is running"

@app.route("/instruction")
def get_instruction():
    return instruction

@app.route("/set/<text>")
def set_instruction(text):
    global instruction
    instruction = text
    return f"Instruction set to: {instruction}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
