from dagster import asset, define_asset_job, repository, job, op


@asset
def simple_asset():
    return "Hello, Dagster!"


all_assets_job = define_asset_job("all_assets_job", selection="*")


@op
def log_message():
    # Op that runs for ~10 minutes, logging progress each minute
    import time
    from dagster import get_dagster_logger
    logger = get_dagster_logger()
    total_minutes = 10
    for minute in range(1, total_minutes + 1):
        logger.info(f"simple_job progress: minute {minute}/{total_minutes}")
        time.sleep(60)  # Sleep 60 seconds
    logger.info("simple_job completed ~10 minute run")
    return "done"


@job
def simple_job():
    log_message()


@repository
def my_repository():
    # Expose assets, asset job, and the new simple job
    return [simple_asset, all_assets_job, simple_job]
