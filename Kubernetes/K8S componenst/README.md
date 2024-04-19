

onyl edit current file data

kubectl edit 'deployment' 'name'

## ReplecaSet

Scale up yr ReplicaSet

rewrite ReplicaSet replicas param and run

`kubectl replace -f ReplicaSet/rplicaSet.yaml`
`kubectl scale --replicas=2 -f ReplicaSet/rplicaSet.yaml`
`kubectl scale --replicas=2 replicaset myapp-replicaset`

## Deployment

rollout status
`kubectl rollout status deployment/mydeployment`
`kubectl rollout history deployment/mydeployment`

version update strategies:
- recreate
- rolling

undo rollout
`kubectl rollout undo deployment/mydeployment`