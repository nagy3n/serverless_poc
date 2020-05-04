from flask import Flask, request
from os import listdir, path, rename, remove
from os.path import isfile, join
import json
import importlib
import traceback
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
ALLOWED_EXTENSIONS = {'py'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
@cross_origin()
def scripts_list():
    scripts = [f for f in listdir('scripts') if isfile(join('scripts', f))]
    return json.dumps(scripts)


@app.route('/upload/', methods=['POST'])
@cross_origin()
def upload_script():
    # validating script file
    try:
        script_request_file = request.files['script']
    except KeyError:
        return 'No script file attached', 400

    if not allowed_file(script_request_file.filename):
        return 'File extension must be .py', 400

    # checking if there's no syntax errors/wrong format

    script_request_file.save(path.join('./scripts', 'temp.py'))
    try:
        script = importlib.import_module('scripts.temp')
        script = importlib.reload(script)
    except (SyntaxError, IndentationError):
        return 'Python script has syntax/indentation errors', 400

    # checking if the script has all the required functions

    try:
        if not isinstance(script.arguments, list):
            return 'arguments variable is not a list', 400
        if not callable(script.main):
            return 'main is not a function', 400
    except AttributeError:
        return 'Python script does not have arguments object or main function'

    # saving the script in scripts folder
    rename('./scripts/temp.py', join('./scripts', script_request_file.filename))

    return 'Script uploaded successfully'


@app.route('/get_script_arguments/<script_name>', methods=['GET'])
@cross_origin()
def get_script_arguments(script_name):
    # validating
    if not isfile(join('./scripts', script_name)):
        return 'Script does not exist', 400

    # getting arguments
    try:
        script_module_name = script_name.split('.')[0]
        script = importlib.import_module('scripts.{}'.format(script_module_name))
        script = importlib.reload(script)
        arguments = script.arguments
    except:
        return traceback.format_exc(), 400

    return json.dumps(arguments)


@app.route('/run_script/<script_name>', methods=['POST'])
@cross_origin()
def run_script(script_name):
    # validating
    if not isfile(join('./scripts', script_name)):
        return 'Script does not exist', 400
    try:
        arguments = request.json
    except KeyError:
        return 'No attached arguments', 400

    # executing
    try:
        script_module_name = script_name.split('.')[0]
        script = importlib.import_module('scripts.{}'.format(script_module_name))
        script = importlib.reload(script)
        result = script.main(arguments)
    except:
        return traceback.format_exc(), 400

    return json.dumps(result)


@app.route('/delete_script/<script_name>', methods=['DELETE'])
@cross_origin()
def delete_script(script_name):
    script_path = join('./scripts', script_name)
    if not isfile(script_path):
        return 'Script does not exist', 400

    remove(script_path)
    return 'Script removed successfully', 204



if __name__ == '__main__':
    app.run()
