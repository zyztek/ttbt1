import random
from kubernetes import client, config

class ChaosMonkey:
    def __init__(self):
        config.load_kube_config()
        self.core_v1 = client.CoreV1Api()
    
    def random_pod_termination(self, namespace='tiktok-bot'):
        pods = self.core_v1.list_namespaced_pod(namespace)
        target = random.choice(pods.items)
        self.core_v1.delete_namespaced_pod(
            name=target.metadata.name,
            namespace=namespace
        )
    
    def network_chaos_injection(self):
        # Implementar usando LitmusChaos
        os.system("litmusctl run-experiment network-loss --duration=5m")