# Change and configure your own app !
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for expenses
expenses = []


@app.route("/")
def home():
    return "Welcome to the Personal Expense Tracker!"


# Add a new expense
@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json
    if "description" not in data or "amount" not in data or "date" not in data:
        return (
            jsonify({"error": "Expense must have a description, amount, and date"}),
            400,
        )

    expense = {
        "id": len(expenses) + 1,
        "description": data["description"],
        "amount": data["amount"],
        "date": data["date"],
    }
    expenses.append(expense)
    return jsonify(expense), 201


# Get all expenses
@app.route("/expenses", methods=["GET"])
def get_expenses():
    return jsonify(expenses)


# Delete an expense by ID
@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    global expenses
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    return jsonify({"message": "Expense deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
