import flask


server = flask.Flask(__name__)


@server.route('/')
@server.route('/main')
@server.route('/index')
def index() -> str:
    return flask.render_template('index.html')


@server.route('/account')
def account() -> str:
    return flask.render_template('account.html')


@server.route('/help')
def help() -> str:
    return flask.render_template('help.html')


@server.route('/about')
def about() -> str:
    return flask.render_template('about.html')


if __name__ == '__main__':
    server.run(debug=True, port=5000)
