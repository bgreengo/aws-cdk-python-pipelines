#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_python_pipelines.aws_cdk_python_pipelines_stack import AwsCdkPythonPipelinesStack


app = core.App()
AwsCdkPythonPipelinesStack(app, "aws-cdk-python-pipelines")

app.synth()
