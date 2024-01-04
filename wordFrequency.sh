#!/bin/bash    
value=$(<words.txt)
declare -A my_dict
for word in $value; do
	if [[ -n "${my_dict[$word]}" ]] 
	then
		 
		((my_dict[$word]++))
	else 
		my_dict[$word]=1
	fi
done
for key in $(printf '%s\n' "${!my_dict[@]}" | sort); do
	    echo "$key ${my_dict[$key]}"
    done
