from dagster import asset, define_asset_job, repository, job, op


@asset
def simple_asset():
    return "Hello, Dagster!"


all_assets_job = define_asset_job("all_assets_job", selection="*")


@op
def log_message():
    # Dummy op that logs a line
    from dagster import get_dagster_logger
    get_dagster_logger().info("Dummy job says hello!")
    return "done"


@job
def simple_job():
    log_message()


@repository
def my_repository():
    # Expose assets, asset job, and the new simple job
    return [simple_asset, all_assets_job, simple_job]
