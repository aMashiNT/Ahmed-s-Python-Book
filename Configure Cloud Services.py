#Configure Cloud Services


def configure_service(**settings):
    for key, value in settings.items():
        print(f"{key} set to {value}")

configure_service(region="us-east-1", instance_type="t2.micro", storage="50GB")
