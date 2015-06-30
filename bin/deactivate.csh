if ( ${?_AB2CB_ACTIVATED} ) then
    
    if ( ${?_PATH_BEFORE_AB2CB_ACTIVATE} ) then
        setenv PATH $_PATH_BEFORE_AB2CB_ACTIVATE
    endif

    if ( ${?_PYTHONPATH_BEFORE_AB2CB_ACTIVATE} ) then
        if ( { eval 'test ! -z $_PYTHONPATH_BEFORE_AB2CB_ACTIVATE' } ) then
            setenv PYTHONPATH $_PYTHONPATH_BEFORE_AB2CB_ACTIVATE
        else
            unsetenv PYTHONPATH
        endif
    endif

    unsetenv _PATH_BEFORE_AB2CB_ACTIVATE
    unsetenv _PYTHONPATH_BEFORE_AB2CB_ACTIVATE
    unsetenv _AB2CB_ACTIVATED
else
    echo 'Not active'
endif
    