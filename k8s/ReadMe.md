# K8s deploy image from Habor

If Harbor registry requires authentication, create a Kubernetes secret with your Harbor credentials and reference it in your Deployment.

1. Create a Docker registry secret in Kubernetes:

```
kubectl create secret docker-registry <habor-secret-name> \
--docker-server=<harbor-registry-ip> \
--docker-username=<username> \
--docker-password=<password> \
-n <namespace>
```

2. Reference the Secret in your Deployment YAML:

```
apiVersion: apps/v1 
kind: Deployment 
metadata: 
	name: my-app 
	spec: 
		replicas: 1 
		template: 
			metadata: 
				labels: 
					app: my-app 
	spec: 
		containers: 
		- name: my-container 
		- image: <harbor-registry-ip>:<port>/my-project/my-image:latest 
		imagePullSecrets: 
		- name: <harbor-secret-name>
```

3. Verify Image Pulling

After configuring insecure registry settings on each node, deploying with the correct image reference should work without the `ImagePullBackOff` error. Run your deployment and check that the Pods pull the images successfully:

```
kubectl get pods -n <namespace>
```

If the Pods start without errors, then the configuration is correct. If there are issues, use `kubectl describe pod <pod-name> -n <namespace>` to view error details.