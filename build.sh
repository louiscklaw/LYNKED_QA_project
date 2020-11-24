#!/usr/bin/env bash

set -ex

# function shutdown {
#     ./scripts/down_docker_selenium.sh
#     echo "Shutdown complete"
# }

# trap shutdown SIGTERM SIGINT EXIT

./scripts/clear_report_directory.sh
rm -rf .pytest_cache

mkdir -p reports/functional/test_viewport/food
mkdir -p reports/functional/test_viewport/manage
mkdir -p reports/UI_test/functional/test_happyflow_1/result

# touch reports/functional/test_viewport/food/.gitkeep
# touch reports/functional/test_viewport/manage/.gitkeep


# sh docs/flows/test_site_flows/build.sh

# ./scripts/up_docker_selenium.sh
# echo 'sleep a while to let docker steady'
# sleep 30

# pipenv sync

# pipenv run pytest --html=reports/regression/report.html tests/UI_test/regression
# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional
# pipenv run pytest --html=reports/new_feature/report.html tests/UI_test/new_feature

# pipenv run pytest tests/self_test

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1/test_happyflow_1_chrome.py

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1/test_happyflow_1_firefox.py
# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/test_happyflow_1_chrome_click_accept_and_continue.py
# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/test_po_helloworld.py

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/test_po_helloworld.py


# pipenv run pytest tests/UI_test/functional/test_viewport/test_SeleniumCoolDown.py
# pipenv run pytest tests/UI_test/functional/test_functional_Helloworld.py

# pipenv run pytest tests/self_test

# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_viewport/test_ViewPort_food.py
# pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional/test_viewport/test_ViewPort_manage.py

# mkdir -p ~/.config/gspread
# cp ./creds/qa-reporting-296203-8b43a1a973e1.json ~/.config/gspread/service_account.json

# pipenv sync
# pipenv run pytest --json-report -v  --html=reports/functional/report.html tests/UI_test/functional
# pipenv run pytest --json-report -v  --html=reports/functional/report.html tests/UI_test/functional/test_local_chrome/test_local_chrome.py

# pipenv run pytest --json-report -v  --html=reports/functional/report.html tests/UI_test/functional/test_local_chrome/test_click_alert_box.py
# pipenv run pytest --json-report -v  --html=reports/functional/report.html tests/UI_test/functional/test_local_chrome/test_cart_page_chrome.py

# local test
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/happyflow_1_chrome_first_time_arrive_line_up_page.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_020.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_001.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_002.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_003.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_004.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_005.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_006.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_007.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_008.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_009.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_010.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_011.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_012.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_013.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_014.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_015.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_016.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_017.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_018.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_019.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_020.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_021.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_022.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_023.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_025.py
# pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_026.py
pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/test_local_chrome/test_TID_027.py

# pipenv run pytest -x --json-report -v  --html=reports/functional/report.html tests/UI_test/functional/test_local_chrome/test_take_seat_first_dialogue.py

# pipenv run python3 ./tests/fill_value_to_google.py
