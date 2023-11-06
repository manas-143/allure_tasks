
import os
from pathlib import Path
from dotenv import load_dotenv
from behave.__main__ import run_behave
from behave.configuration import Configuration
from behave.tag_expression import TagExpression


# from features.environment import PROJECT_ROOT
# from utils.env import get_from_env
# from utils.env import is_truthy
# from utils.env import load_env
# from utils.logger import log
def main():
    load_dotenv()
    my_details = os.getenv("ENVIRONMENT")
    print(my_details)
    # tags = TagExpression(get_from_env("TAGS").split())
    # tags_option = " ".join([f"--tags={','.join(tag)}" for tag in tags.ands])
    # log.error(f"Using these tags: {tags_option}")
    #
    # stop_fail = "--stop" if is_truthy(os.getenv("STOP_FAIL")) else ""
    # log.info(f'Stop at first fail?: {get_from_env("STOP_FAIL")}')
    reports = "./" + "/" + os.getenv(
        "REPORTS_FOLDER")
    reports = os.path.normpath(f'"{reports}"')
    feature_order = '" "'.join(
        os.path.join("./",
                     feature_path.strip())
        for feature_path in os.getenv("FEATURE_ORDER").split(",")
        if Path(
            "./" + "/" + feature_path.strip()).exists()
    )
    feature_order = os.path.normpath(f'"{feature_order}"')
    print(feature_order)
    arguments = (
        f"{feature_order} -f allure_behave.formatter:AllureFormatter -o {reports}"
        # f"{stop_fail} --no-skipped -f plain {tags_option} --no-capture "
        # f"--no-capture-stderr --no-logcapture "
    )
    print(arguments)
    # log.error(arguments)
    configuration = Configuration(arguments)
    for i in range(1):
        run_behave(configuration)


if __name__ == "__main__":
    main()
