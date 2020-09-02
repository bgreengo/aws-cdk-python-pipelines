from aws_cdk import core

from .aws_cdk_python_pipelines_stack import AwsCdkPythonPipelinesStack

class WebServiceStage(core.Stage):

    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = AwsCdkPythonPipelinesStack(self, 'WebService')

        self.url_output = service.url_output