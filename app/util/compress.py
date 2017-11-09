import os
from flask import Blueprint, send_from_directory, make_response
from app.util.util import gzipped


# Define the blueprint: 'compress'
compress = Blueprint('compress', __name__)


""" Compress Static files """


# Template for serving static resources
def _response_path(static_path):
    return make_response(send_from_directory(os.path.join(compress.root_path, 'static'), static_path))


""" CSS """


@compress.route('/compress/static/assets/css/bootstrap.min.css')
@gzipped
def css_bootstrap():
    return _response_path('assets/css/bootstrap.min.css')


@compress.route('/compress/static/assets/css/material-dashboard.css')
@gzipped
def css_material_dashboard():
    return _response_path('assets/css/material-dashboard.css')


""" JS """


@compress.route('/compress/static/assets/js/bootstrap.min.js')
@gzipped
def js_bootstrap():
    return _response_path('assets/js/bootstrap.min.js')


@compress.route('/compress/static/assets/js/material.min.js')
@gzipped
def js_material():
    return _response_path('assets/js/material.min.js')


@compress.route('/compress/static/js/stats/stat.min.js')
@gzipped
def js_stats():
    return _response_path('js/stats/stat.min.js')


@compress.route('/compress/static/assets/js/chartist.min.js')
@gzipped
def js_chartist():
    return _response_path('assets/js/chartist.min.js')


@compress.route('/compress/static/assets/js/bootstrap-notify.js')
@gzipped
def js_notify():
    return _response_path('assets/js/bootstrap-notify.js')


@compress.route('/compress/static/assets/js/material-dashboard.js')
@gzipped
def js_material_dashboard():
    return _response_path('assets/js/material-dashboard.js')


@compress.route('/compress/static/assets/js/bootstrap-datepicker.js')
@gzipped
def js_datepicker():
    return _response_path('assets/js/bootstrap-datepicker.js')


@compress.route('/compress/static/d3pie.min.js')
@gzipped
def js_d3pie():
    return _response_path('d3pie.min.js')


""" Errors """


@compress.errorhandler(500)
def internal_error(e):
    print(e)