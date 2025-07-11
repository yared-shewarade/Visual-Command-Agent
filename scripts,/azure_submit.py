import os 
from azure.ai.ml import MLClient 
from azure.ai.ml.entities import CommandJob, Environment, CodeConfiguration 
from azure.identity import DefaultAzureCredential

subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
resource_group = os.environ.get("AZURE_RESOURCE_GROUP")
workspace_name = os.environ.get("AZURE_WORKSPACE_NAME")

ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace_name)

job = CommandJob(
    code=CodeConfiguration(code="../training", command="python train.py"),
    environment=Environment(image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"),
    compute="gpu-cluster",
    display_name="visual-command-train",
    experiment_name="visual-command-agent"
)

returned_job = ml_client.jobs.create_or_update(job)
print(f"Submitted Azure ML job: {returned_job.name}")
