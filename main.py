import os


def load_env(file_loc=".env"):
    with open(file_loc) as f:
        env_vars = [
            var.strip("\n").split("=") for var in f.readlines()
            if "=" in var and "#" not in var
        ]

        for k, v in env_vars:
            os.environ[k] = v
