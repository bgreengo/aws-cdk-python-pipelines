#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_python_pipelines.aws_cdk_python_pipelines_stack import AwsCdkPythonPipelinesStack
from aws_cdk_python_pipelines.pipeline_stack import PipelineStack

app = core.App()
AwsCdkPythonPipelinesStack(app, "aws-cdk-python-pipelines")
PipelineStack(app, 'PipelineStack', env={
    'account': '987092829714',
    'region': 'us-west-2'
})

app.synth()
