
############################################
############################################
####### Simple Web App using K8s demo ######
############################################
############################################

Architecture: 

Flask app that redirects all r-
equests to index.html, which shows the text
HELLO WORLD with both the Os = number of vis-
ts to the site. So, initially it would be  

HELL0 W0RLD, after 1 visit - 
HELL1 W1RLD, and so on.

Note: The number of visits is stored within 
the Postgresql database which is hosted on 
a different pod. Subsequent deletion of pods
or a rerun of any node due to failures will
not reset the total visit count.

############################################

Pods deployed:

One for application logic (as it is Fla-
sk in Python), we can keep our backend fetch
logic and HTML in the same pod and make it 
render smoothly

Another for database - POSTGRESQL, which has
access to persistant volumes for storing its
entries

############################################

Prerequisites:

Docker, Minikube and Helm installed and run-
ning

############################################

Instructures to run:

1. Pull this repository
2. Run the script.sh file (*)

(*)
Note: The script file will rerun minikube and
clean any pvc or pvs before. To avoid this, 
you can only run the below two commands only 
to run the entire application.

// Install postgresql setting password at the 
// time of creation
helm install web-app --set global.postgresql.auth.postgresPassword=user bitnami/postgresql

// Once web-app-postgresql-0 pod is running 
// and ready, install the web-app-frontend
// using the following command
helm install web-app-frontend web-app 

############################################

Logs to except while running:

😄  minikube v1.30.1 on Darwin 13.1 (arm64)
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🏃  Updating the running docker "minikube" container ...
🐳  Preparing Kubernetes v1.26.3 on Docker 23.0.2 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
release "web-app-frontend" uninstalled
release "web-app" uninstalled
persistentvolumeclaim "data-web-app-postgresql-0" deleted
error: there is no need to specify a resource type as a separate argument when passing arguments in resource/name form (e.g. 'kubectl get resource/<resource_name>' instead of 'kubectl get resource resource/<resource_name>'
"bitnami" already exists with the same configuration, skipping
NAME: web-app
LAST DEPLOYED: Thu Apr 13 11:18:13 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: postgresql
CHART VERSION: 12.2.7
APP VERSION: 15.2.0

** Please be patient while the chart is being deployed **

PostgreSQL can be accessed via port 5432 on the following DNS names from within your cluster:

    web-app-postgresql.default.svc.cluster.local - Read/Write connection

To get the password for "postgres" run:

    export POSTGRES_PASSWORD=$(kubectl get secret --namespace default web-app-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

To connect to your database run the following command:

    kubectl run web-app-postgresql-client --rm --tty -i --restart='Never' --namespace default --image docker.io/bitnami/postgresql:15.2.0-debian-11-r16 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
      --command -- psql --host web-app-postgresql -U postgres -d postgres -p 5432

    > NOTE: If you access the container using bash, make sure that you execute "/opt/bitnami/scripts/postgresql/entrypoint.sh /bin/bash" in order to avoid the error "psql: local user with ID 1001} does not exist"

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/web-app-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432

WARNING: The configured password will be ignored on new installation in case when previous Posgresql release was deleted through the helm command. In that case, old PVC will have an old password, and setting it through helm won't take effect. Deleting persistent volumes (PVs) will solve the issue.
NAME: web-app-frontend
LAST DEPLOYED: Thu Apr 13 11:18:13 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=web-app,app.kubernetes.io/instance=web-app-frontend" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

############################################

Thank you, it was a wonderful experience in 
building this small demo, and I surely lear-
nt a lot about Helm which I had never used
before, and managing k8s from the helm!

Feel free to contact me in case if any clar-
ifications is required.

Thanks,
Sudarshan Khasnis
352-848-8484
sudarshan.ufl@gmail.com

############################################
############################################