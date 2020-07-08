from flask import Flask, render_template
import launch

app = Flask(__name__)
app.config["DEBUG"] = True

'''
Renders the index template and passes in the launch information.
'''
@app.route('/')
def index():
    l = launch.Launch()
    return render_template("index.html",
                            net = l.net,
                            mission = l.mission,
                            stream_url = l.stream,
                            info_url = l.info,
                            lsp = l.lsp,
                            lsp_abbrev = l.lsp_abbrev,
                            lsp_info_url = l.lsp_info_url,
                            launch_time_date = l.launch_time_date)

