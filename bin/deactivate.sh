if [ $_AB2CB_ACTIVATED ]; then
    
    if [ $_PATH_BEFORE_AB2CB_ACTIVATE ]; then
        export PATH=$_PATH_BEFORE_AB2CB_ACTIVATE
    fi

    if [ $_PYTHONPATH_BEFORE_AB2CB_ACTIVATE ]; then
        if [  $_PYTHONPATH_BEFORE_AB2CB_ACTIVATE != 0 ]; then
            export PYTHONPATH=$_PYTHONPATH_BEFORE_AB2CB_ACTIVATE
        else
            unset PYTHONPATH
        fi
    fi

    unset _PATH_BEFORE_AB2CB_ACTIVATE
    unset _PYTHONPATH_BEFORE_AB2CB_ACTIVATE
    unset _AB2CB_ACTIVATED
else
    echo 'Not active'
fi
    