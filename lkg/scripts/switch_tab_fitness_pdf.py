import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("testai_CaseStudy_Gaming_v1.3.pdf")
    context.get_all_elements()