import ast
import pkg_resources
import string
import numpy as np
from dateutil.parser import parse
import json
from ._comm_api import setup_comm_api
from io import StringIO

def id_generator(size=15):
    """Helper function to generate random div ids. This is useful for embedding
    HTML into ipython notebooks."""
    chars = list(string.ascii_uppercase)
    return ''.join(np.random.choice(chars, size, replace=True))


def make_html(dataset_results, id):
	lib_path = pkg_resources.resource_filename(__name__, "build/temporalViewer.js")
	bundle = open(lib_path, "r", encoding="utf8").read()
	html_all = """
	<html>
	<head>
	</head>
	<body>
	    <script>
	    {bundle}
	    </script>
	    <div id="{id}">
	    </div>
	    <script>
	        temporalViewer.renderDatasetsSummarizerBundle("{id}", {dataset_results});
	    </script>
	</body>
	</html>
	""".format(bundle=bundle, id=id, dataset_results=json.dumps(dataset_results))
	return html_all

def plot_temporal_viewer(dataset_results):
    from IPython.core.display import display, HTML
    from base64 import b64encode
    id = id_generator()

    # from IPython.display import HTML

    video_path = dataset_results['mainCameraPath']
    video = open(video_path,'rb').read()
    src = 'data:video/mp4;base64,' + b64encode(video).decode()
    dataset_results['mainCameraPath'] = src
#     display(HTML("""
#     <video alt="test" controls>
#         <source src={video_path} type="video/mp4">
#     </video>
# """.format(video_path=src)))
    html_all = make_html({"dataset": dataset_results}, id)
    display(HTML(html_all))