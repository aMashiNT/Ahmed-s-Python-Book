#Deploy Multiple Servers


def deploy_servers(*servers):
    for server in servers:
        print(f"Deploying server: {server}")

deploy_servers("web-1", "db-1", "cache-1")
