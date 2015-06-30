# add the dev directory to the path and pythonpath
if ( ${?_AB2CB_ACTIVATED} ) then
    echo 'Already activated'
else
    set pwd=`pwd`
    setenv _PATH_BEFORE_AB2CB_ACTIVATE $PATH
    setenv PATH $pwd/dev:$PATH

    if ( ${?PYTHONPATH} ) then
        setenv _PYTHONPATH_BEFORE_AB2CB_ACTIVATE $PYTHONPATH
        setenv PYTHONPATH $pwd/dev:$PYTHONPATH
    else
        setenv _PYTHONPATH_BEFORE_AB2CB_ACTIVATE
        setenv PYTHONPATH $pwd/dev
    endif

    setenv _AB2CB_ACTIVATED
endif
