from elaw import app


if __name__ == "__main__":
    app.run(debug=True)

app.app_context().push()
