from flask import render_template, redirect, Flask

app = Flask(__name__)

@app.route("/")
def home():
    return(
        render_template(
            "index.html"
        )
    )

@app.route("/yt")
@app.route("/youtube")
def youtube():
    return(
        redirect(
            "https://www.youtube.com/@AlgoraKiko"
        )
    )

@app.route("/t")
@app.route("/x")
@app.route("/twt")
@app.route("/twitter")
def twitter():
    return(
        redirect(
            "https://twitter.com/AlgoraKiko"
        )
    )

@app.route("/ttv")
@app.route("/twitch")
def twitch():
    return(
        redirect(
            "https://twitch.tv/AlgoraKiko"
        )
    )

@app.route("/discord")
def discord():
    return(
        redirect(
            "https://discord.com/invite/cFVFG26"
        )
    )

@app.route("/insta")
@app.route("/instagram")
def instagram():
    return(
        redirect(
            "https://www.instagram.com/algorakiko/"
        )
    )

@app.route("/tiktok")
def tiktok():
    return(
        redirect(
            "https://www.tiktok.com/@algorakiko"
        )
    )

@app.route("/spotify")
def spotify():
    return(
        redirect(
            "https://open.spotify.com/user/jailenetalampas"
        )
    )

if(__name__ == "__main__"):
    app.run(host="0.0.0.0", debug=True)