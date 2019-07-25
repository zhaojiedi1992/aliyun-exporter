import json

from aliyunsdkcore.client import AcsClient
from flask import (
    Flask, render_template
)
from prometheus_client import make_wsgi_app
from werkzeug.wsgi import DispatcherMiddleware

from aliyun_exporter import CollectorConfig
#from aliyun_exporter.QueryMetricMetaRequest import QueryMetricMetaRequest
#from aliyun_exporter.QueryProjectMetaRequest import QueryProjectMetaRequest

#from aliyun_exporter.QueryProjectMetaRequest import QueryProjectMetaRequest

from aliyunsdkcms.request.v20190101.DescribeMetricMetaListRequest import DescribeMetricMetaListRequest
#from aliyunsdkcms.request.v20190101.DescribeProjectMetaRequest import DescribeProjectMetaRequest

from aliyun_exporter.DescribeNamespaceMetaRequest import DescribeNamespaceMetaRequest


from aliyun_exporter.utils import format_metric, format_period


def create_app(config: CollectorConfig):

    app = Flask(__name__, instance_relative_config=True)

    client = AcsClient(
        ak=config.credential['access_key_id'],
        secret=config.credential['access_key_secret'],
        region_id=config.credential['region_id']
    )

    @app.route("/")
    def projectIndex():
        req = DescribeNamespaceMetaRequest()
        req.set_PageSize(100)
        try:
            resp = client.do_action_with_exception(req)
        except Exception as e:
            return render_template("error.html", errorMsg=e)
        data = json.loads(resp)
        return render_template("index.html", namespaces=data["Resources"]["Resource"])

    @app.route("/namespaces/<string:name>")
    def projectDetail(name):
        req = DescribeMetricMetaListRequest()
        req.set_PageSize(100)
        req.set_Namespace(name)
        try:
            resp = client.do_action_with_exception(req)
        except Exception as e:
            return render_template("error.html", errorMsg=e)
        data = json.loads(resp)
        return render_template("detail.html", metrics=data["Resources"]["Resource"], namespace=name)

    @app.route("/yamls/<string:name>")
    def projectYaml(name):
        req = DescribeMetricMetaListRequest()
        req.set_PageSize(100)
        req.set_Namespace(name)
        try:
            resp = client.do_action_with_exception(req)
        except Exception as e:
            return render_template("error.html", errorMsg=e)
        data = json.loads(resp)
        return render_template("yaml.html", metrics=data["Resources"]["Resource"], namespace=name)

    app.jinja_env.filters['formatmetric'] = format_metric
    app.jinja_env.filters['formatperiod'] = format_period

    app_dispatch = DispatcherMiddleware(app, {
        '/metrics': make_wsgi_app()
    })
    return app_dispatch
