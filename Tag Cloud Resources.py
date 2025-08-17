#Tag Cloud Resources


def tag_resources(**tags):
    for resource, tag in tags.items():
        print(f"{resource} tagged as {tag}")

tag_resources(EC2="Production", S3="Backup", RDS="Database")
