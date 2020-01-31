from flask import Flask, render_template
import launch
import tw_nl

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    l = launch.Launch()
    return render_template("index.html",
                            net = l.net,
                            name = l.name,
                            stream_url = l.stream,
                            info_url = l.info,
                            lsp = l.lsp,
                            tweet = tw_nl.latest_tweet_text())

