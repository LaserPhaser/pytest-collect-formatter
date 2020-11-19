for FORMAT in json yaml xml
do
    for TYPE in path classic
    do
        pytest examples/tests --collect-only --collect-format $FORMAT --collect-type $TYPE --collect-output-file examples/results/$TYPE.$FORMAT
    done
done
