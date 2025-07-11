import os 
from azure.ai.ml import MLClient 
from azure.ai.ml.entities import CommandJob, Environment, CodeConfiguration 
from azure.identity import DefaultAzureCredential

subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
resource_group = os.environ.get()
