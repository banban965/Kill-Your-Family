from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from pathlib import Path
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "enity-koj-secret-key"

ROOT = Path(__file__).resolve().parent
DB = ROOT / "DataBase.json"
CHATS = ROOT / "SaveChat.json"
USERS = ROOT / "UserLoginSaver.json"


def read_json(path, default):
    try:
        return json.loads(
            path.read_text(encoding="utf-8")
        )
    except Exception:
        path.write_text(
            json.dumps(
                default,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )
        return default


def write_json(path, data):
    path.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


def find_answer(text):
    database = read_json(
        DB,
        {"answers": {}}
    )

    answers = database.get(
        "answers",
        {}
    )

    text = text.strip().casefold()

    for key, val in answers.items():
        if key.casefold() == text:
            return val

    return "I don't know yet."


def render_page(name, active=None, **ctx):
    return render_template(
        name,
        active=active,
        username=session.get(
            "username",
            "Guest"
        ),
        **ctx
    )


@app.get("/")
def home():
    return render_page(
        "index.html",
        "home"
    )


@app.get("/chat")
def chat():
    return render_page(
        "chat.html",
        "home"
    )


@app.post("/api/chat")
def api_chat():

    data = request.get_json(
        silent=True
    ) or {}

    msg = str(
        data.get(
            "message",
            ""
        )
    ).strip()

    if not msg:
        return jsonify(
            answer="Please enter a message."
        )

    ans = find_answer(msg)

    store = read_json(
        CHATS,
        {
            "chats": []
        }
    )

    if not isinstance(store, dict):
        store = {
            "chats": []
        }

    store.setdefault(
        "chats",
        []
    )

    store["chats"].append(
        {
            "user": session.get(
                "username",
                "Guest"
            ),
            "message": msg,
            "answer": ans,
            "time": datetime.now().isoformat(
                timespec="seconds"
            )
        }
    )

    write_json(
        CHATS,
        store
    )

    return jsonify(
        answer=ans
    )


@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "GET":
        return render_page(
            "login.html"
        )

    u = request.form.get(
        "username",
        ""
    ).strip()

    p = request.form.get(
        "password",
        ""
    )

    users = read_json(
        USERS,
        {
            "users": []
        }
    ).get(
        "users",
        []
    )

    if any(
        x.get("username") == u
        and x.get("password") == p
        for x in users
    ):
        session["username"] = u

        return redirect(
            url_for("chat")
        )

    return render_page(
        "login.html",
        error="Invalid username or password."
    )


@app.route(
    "/signup",
    methods=["GET", "POST"]
)
def signup():

    if request.method == "GET":
        return render_page(
            "signup.html"
        )

    u = request.form.get(
        "username",
        ""
    ).strip()

    p = request.form.get(
        "password",
        ""
    )

    c = request.form.get(
        "confirm_password",
        ""
    )

    if not u or not p:
        return render_page(
            "signup.html",
            error="Please fill in all fields."
        )

    if p != c:
        return render_page(
            "signup.html",
            error="Passwords do not match."
        )

    data = read_json(
        USERS,
        {
            "users": []
        }
    )

    data.setdefault(
        "users",
        []
    )

    if any(
        x.get("username") == u
        for x in data["users"]
    ):
        return render_page(
            "signup.html",
            error="Username already exists."
        )

    data["users"].append(
        {
            "username": u,
            "password": p
        }
    )

    write_json(
        USERS,
        data
    )

    session["username"] = u

    return redirect(
        url_for("chat")
    )


@app.get("/history")
def history():

    u = session.get(
        "username",
        "Guest"
    )

    items = [
        x
        for x in read_json(
            CHATS,
            {
                "chats": []
            }
        ).get(
            "chats",
            []
        )
        if x.get("user") == u
    ]

    return render_page(
        "history.html",
        "history",
        chats=items
    )


@app.get("/settings")
def settings():
    return render_page(
        "settings.html",
        "settings"
    )


@app.get("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("home")
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )