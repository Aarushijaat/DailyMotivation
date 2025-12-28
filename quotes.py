from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

INSIGHTS = [
    {
        "title": "Believe in Yourself",
        "quote": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt",
        "reflection": "Self-belief builds confidence and helps overcome challenges."
    },
    {
        "title": "Consistency Matters",
        "quote": "Success comes from consistency.",
        "author": "Marie Forleo",
        "reflection": "Small daily actions create long-term success."
    }
]

@app.route("/")
def home():
    page = int(request.args.get("page", 1))
    total_pages = len(INSIGHTS)

    insight = INSIGHTS[page - 1]
    today = datetime.date.today()

    return render_template(
        "index.html",
        insight=insight,
        page=page,
        total_pages=total_pages,
        date=today
    )

if __name__ == "__main__":
   app.run(port=5001, debug=True)

