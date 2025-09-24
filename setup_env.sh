#!/bin/bash
# Setup environment variables for Airflow + AWS

export AIRFLOW_HOME=$(pwd)/airflow_home
export AIRFLOW__CORE__DAGS_FOLDER=$(pwd)/dags

# (Optional) Provide AWS creds if not using an EC2 role
export AWS_DEFAULT_REGION=us-east-1
echo "Environment set. AIRFLOW_HOME=$AIRFLOW_HOME"
