from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/summary")
def summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(sales), SUM(profit) FROM sales")
    result = cursor.fetchone()

    conn.close()

    return jsonify({
        "total_sales": result[0] if result[0] else 0,
        "total_profit": result[1] if result[1] else 0
    })

if __name__ == "__main__":
    app.run(debug=True)