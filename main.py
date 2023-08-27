from flask import Flask, request, jsonify
import json

app = Flask(__name__)

history_file_path = "./history.json"


def load_history():
    try:
        with open(history_file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_history(history):
    with open(history_file_path, "w") as file:
        json.dump(history, file, indent=2)


history = load_history()


@app.before_request
def log_request():
    print(f"{request.method} request at {request.url}")


@app.route("/<int:operand1>/plus/<int:operand2>")
def addition(operand1, operand2):
    question = f"{operand1} + {operand2}"
    answer = operand1 + operand2

    history.append({"question": question, "answer": answer})
    save_history(history)

    response_data = {"question": question, "answer": answer}
    return jsonify(response_data)


@app.route("/<int:operand1>/minus/<int:operand2>")
def subtraction(operand1, operand2):
    question = f"{operand1} - {operand2}"
    answer = operand1 - operand2

    history.append({"question": question, "answer": answer})
    save_history(history)

    return jsonify({"question": question, "answer": answer})

@app.route("/<int:operand1>/into/<int:operand2>")
def multiply(operand1, operand2):
    question = f"{operand1} * {operand2}"
    answer = operand1 * operand2

    history.append({"question": question, "answer": answer})
    save_history(history)

    return jsonify({"question": question, "answer": answer})

@app.route("/<int:operand1>/div/<int:operand2>")
def divide(operand1, operand2):
    question = f"{operand1} / {operand2}"
    answer = operand1 / operand2

    history.append({"question": question, "answer": answer})
    save_history(history)

    return jsonify({"question": question, "answer": answer})


@app.route("/<int:operand1>/minus/<int:operand2>/plus/<int:operand3>")
def add_subtract(operand1, operand2, operand3):
    question = f"{operand1} - {operand2} + {operand3}"
    answer = operand1 - operand2 + operand3

    history.append({"question": question, "answer": answer})
    save_history(history)

    return jsonify({"question": question, "answer": answer})


@app.route("/<int:operand1>/into/<int:operand2>/plus/<int:operand3>/into/<int:operand4>")
def multiply_add(operand1, operand2, operand3, operand4):
    question = f"{operand1} * {operand2} + {operand3} * {operand4}"
    answer = (operand1 * operand2) + (operand3 * operand4)

    history.append({"answer": answer, "question": question})
    save_history(history)

    return jsonify({"answer": answer, "question": question})


@app.route("/history")
def get_history():
    return jsonify(history[-20:])


@app.route("/")
def welcome():
    return """<h1>MATH SERVER<br></h1>
      &nbsp<h2>Welcome to the Math Server. Use appropriate routes to perform calculations.</h2>
      + = <strong>plus</strong> <br>
      -  = <strong>minus</strong> <br>
      *  = <strong>into</strong> <br>
      / = <strong>divide </strong><br>
      
      <br>
      
      <marquee direction="right" scrollamount="10"> URLS </marquee>
      
      <strong>http://127.0.0.1:3000/num1/plus/num2 </strong>-  add two numbers <br>
      <strong> http://127.0.0.1:3000/num1/minus/num2</strong> -  subtarct two numbers <br> 
       <strong> http://127.0.0.1:3000/num1/into/num2</strong> -  multiply two numbers <br>
        <strong> http://127.0.0.1:3000/num1/div/num2 </strong>-  divide two numbers  <br>"""


if __name__ == "__main__":
    app.run(port=3000)
