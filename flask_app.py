from flask import Flask, render_template
from flask_caching import Cache
import launch

app = Flask(__name__)
cache = Cache()

app.config["DEBUG"] = True
app.config["CACHE_TYPE"] = 'simple'

cache.init_app(app)

'''
Renders the index template and passes in the launch information.
'''
@app.route('/')
def index():
    l = launch_init()
    return render_template("index.html",
                            net = l.net,
                            mission = l.mission,
                            stream_url = l.stream,
                            lsp = l.lsp,
                            lsp_abbrev = l.lsp_abbrev,
                            lsp_country = l.lsp_country,
                            lsp_info_url = l.lsp_info_url,
                            launch_complex=l.launch_complex,
                            launch_complex_info_url=l.launch_complex_info_url,
                            launch_time_date = l.launch_time_date,
                            mission_description = l.mission_description,
                            rocket_name = l.rocket_name,
                            rocket_info_url = l.rocket_info_url)


@cache.cached(timeout=260, key_prefix='launch_init')
def launch_init():
    '''Caches the launch data that is updated every ~5 minutes.'''
    data = launch.Launch()
    return data