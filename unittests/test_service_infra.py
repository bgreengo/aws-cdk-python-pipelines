from aws_cdk import core
from aws_cdk_python_pipelines.aws_cdk_python_pipelines_stack import AwsCdkPythonPipelinesStack

def test_lambda_handler():
    app = core.App()

    AwsCdkPythonPipelinesStack(app, 'Stack')

    template = app.synth().get_stack_by_name('Stack').template
    functions = [resource for resource in template['Resources'].values()
                if resource['Type'] == 'AWS::Lambda::Function']
    
    assert len(functions) == 1
    assert functions[0]['Properties']['Handler'] == 'handler.handler'