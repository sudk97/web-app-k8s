minikube start
helm uninstall web-app-frontend
helm uninstall web-app
kubectl delete pvc --all
kubectl delete pv --all / pv-name
helm repo add bitnami https://charts.bitnami.com/bitnami

helm install web-app --set global.postgresql.auth.postgresPassword=user bitnami/postgresql
helm install web-app-frontend web-app 