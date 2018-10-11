#!/bin/bash
# g   c     l   m    .sh
# git changelog maker

strhashtags="$(git log --no-walk --tags --pretty="%H")"

#lasttag="$(git log -1 --no-walk --tags --pretty="%H")"
#hash="$(git log -1 $lasttag --pretty='format:%H')"
ifssave="$IFS"
IFS='
'
hashtags=( $strhashtags )
#for hashtag in "${hashtags[@]}"
((n_elements=${#hashtags[@]}, max_index=n_elements - 1))
for ((i = 0; i <= max_index; i++))
do
    hashtag=${hashtags[i]}
    #hashtagprev=${hashtags[i+1]}
    tag="$(git describe --exact-match $hashtag 2>/dev/null)"
    if [ $tag ] ; then
    #tagnext="$(git describe --exact-match $hashtagnext 2>/dev/null)"
        if [ $tagprev ] ; then
            #echo "["$tagprev"] to ["$tag"]"
            if [ $i -gt 1 ] ; then
            echo "
"
            fi
            echo "["$tagprev"] / $(git log -1 --date='short' --pretty='format:%ad' "$tagprev")"
            echo "$(git log --no-merges --pretty="- %s" $tagprev...$tag)"
        fi
        tagprev=$tag
    fi
    
    #if [ $tag ] ; then
    #    echo "["$tag"] to ["$tagnext"]"
        #echo "$(git log --pretty="+%s %b" $hashfromlasttag...HEAD)" >> "$path_to_changelog"
        #echo "$(git log --no-merges --pretty="+ %s" $tag...HEAD)"
    #fi
done
IFS="$ifssave"
