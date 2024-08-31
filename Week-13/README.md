# 1. Create 4 Notebooks for Inserting/Updating Data
Each notebook will read from the same source table and perform insert/update operations on 5 respective output Delta tables.
```
Notebook-01
Notebook-02
Notebook-03
Notebook-04
```

# 2. Create an Orchestration Notebook Using `dbutils`
The orchestration notebook will call the other notebooks sequentially.
`Orchestrator_Sequential`

# 3. Create a Parallel Orchestration Notebook
This notebook will call the other notebooks in parallel using concurrent.futures or similar methods.
`Orchestrator_Parallel`

# 4. Create Jobs Using Databricks Jobs API
You can create jobs for both the sequential and parallel orchestrators using the Databricks Jobs API.
```
%bash
curl -X POST https://<databricks-instance>/api/2.0/jobs/create \
--header "Authorization: Bearer <your-token>" \
--header "Content-Type: application/json" \
--data '{
  "name": "Sequential_Job",
  "notebook_task": {
    "notebook_path": "/Workspace/Orchestrator_Sequential"
  },
  "new_cluster": {
    "spark_version": "10.x-scala2.12",
    "node_type_id": "r5a.large",
    "num_workers": 4
  }
}'
```

# 5. Schedule the Jobs Using Jobs API
You can schedule the jobs with a cron expression or other scheduling options.
```
%bash
curl -X POST https://<databricks-instance>/api/2.0/jobs/runs/submit \
--header "Authorization: Bearer <your-token>" \
--header "Content-Type: application/json" \
--data '{
  "job_id": <job_id>,
  "notebook_task": {
    "notebook_path": "/Workspace/Orchestrator_Sequential"
  }
}'
```

# 6. Compare Runtime of Sequential and Parallel Jobs
Once the jobs have run, you can compare their runtime by looking at the execution logs in the Databricks UI or using the Databricks REST API to fetch job run details.
```
%bash
curl -X GET https://<databricks-instance>/api/2.0/jobs/runs/get \
--header "Authorization: Bearer <your-token>" \
--data '{
  "run_id": <run_id>
}'
```
