# Reference

- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
- [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
- [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)

# CLI

- Stop all the nginx pods in k8s, you can scale the deployment down to zero replicas with this command:\
  `kubectl scale deployment <pod_name> --namespace=<namespace_name> --replicas=0`