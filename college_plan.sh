#!/bin/bash

# - college_plan.sh

GITHUB_URL="https://github.com/Baro-coder/RPi0_College_Plan"

APP_DIR="/home/pi/.Private/RPi0_College_Plan"
MAIN_FILE="${APP_DIR}/main.py"

update(){
    if [[ -d $APP_DIR ]]; then
            # App dir exists
            echo "Removing outdated source..."
            sudo rm -R ${APP_DIR}
    fi

    PARENT_DIR="${APP_DIR%/*}"

    cd $PARENT_DIR

    git clone $GITHUB_URL

    return $?
}

start(){
    if [[ -f $MAIN_FILE ]]; then
        echo "Starting program..."
        python $MAIN_FILE
        return 0
    else
        echo "$MAIN_FILE : The file does not exists!"
        return 1
    fi
}


case "$1" in
    run)
        start
        ;;
    update)
        update
        ;;
    *)
        echo "Usage: $0 {run | update}"
        exit 1
        ;;

esac
exit 0