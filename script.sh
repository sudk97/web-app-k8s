helm uninstall web-app-frontend
helm uninstall web-app
kubectl delete pvc --all
helm install web-app --set global.postgresql.auth.postgresPassword=user bitnami/postgresql
helm install web-app-frontend web-app 
