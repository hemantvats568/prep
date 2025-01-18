#!/opt/homebrew/bin/bash

#Q1: Write a shell script to calculate number of occurance of each word in a sentence.
#
#echo "please pass sentence"
#read sentence
#
#declare -A word_count
#for word in $sentence
#do
#  if [[ ${word_count[$word]} ]]
#  then
#    word_count["$word"]=$(( ${word_count[$word]} + 1 ))
#  else
#    word_count[$word]=1
#  fi
#done
#
#for key in "${!word_count[@]}"
#do
#  echo $key" : "${word_count[$key]}
#done

#Q2: Reverse a string

#echo "Please pass the string: "
#read string
#len=$(( $( echo $string|wc -c ) -1 ))
#until [[ $len -eq -1 ]]
#do
#  echo -n ${string:$len:1}
#  len=$(( $len-1 ))
#done

#Q3: Check prime

#checkprime() {
#    n=$1
#    i=2
#    while [[ $i*$i -le n ]]
#    do
#      if [[ $n%$i -eq 0 ]];then
#        echo "not prime"
#        exit
#      else
#        i=$(( $i + 1 ))
#      fi
#    done
#    echo "prime"
#}
#
#echo "Please enter number"
#read number
#if [[ $number -le 1 ]];then
#  echo "not prime"
#  elif [[ $number -eq 2  ]];then
#    echo "prime"
#  elif [[ $number -eq 3  ]];then
#      echo "prime"
#  else
#    checkprime $number
#fi

#Q4: Largest number in an array

#echo "Please enter the number"
#read numbers
#for num in $numbers
#do
#  if [[ $largest ]]; then
#    if [[ $largest -lt $num ]];then
#      largest=$num
#    fi
#  else
#    largest=$num
#  fi
#done
#echo "largest number is: "$largest

#Q5: Count lines, words and characters in a file
#echo  "number of lines in problems.txt is: "$( wc -l < problems.txt )
#echo "number of words in problems.txt is: "$( wc -w < problems.txt )
#echo "number of characters in problems.txt is: "$( wc -c < problems.txt )

#Q6: Check if a File is Empty
#if [[ $( wc -c < test.txt ) -eq 0 ]];then
#  echo "empty"
#else
#  echo "not empty"
#fi

#Q7: Sum of digits in a number
#echo "Please enter number"
#read number
#sum=0
#until [[ $number -eq 0 ]];do
#  sum=$(( $sum + $number%10 ))
#  number=$(( $number/10 ))
#done
#echo $sum

#Q8: Remove duplicate words from a sentence
#echo "Please enter the sentence"
#read old_sentence
#declare -A word_checked
#
#new_sentence=""
#
#for word in $old_sentence;do
#  if [[ ${word_checked[$word]} ]];then
#    new_sentence=$new_sentence
#  else
#    new_sentence="$new_sentence$word "
#    word_checked[$word]="checked"
#  fi
#done
#
#echo "$new_sentence"

#Q9. Find All Files of a Specific Type
#echo "please provide the extension to search for"
#read ext
#echo "$( ls -a  |grep $ext)"

#Q10. Remove Leading and Trailing Whitespaces

#echo "Please enter the string with spaces"
#read string
#echo "$( echo $string |xargs )" #awk can also be use. xargs without any arguments with trim spaces

#Q11: Check if a String is Palindrome
#echo "Please enter the string"
#read string
#ini=0
#len=$(( $( echo $string |wc -c ) - 1 ))
#last=len
#until [[ $ini -ge $last ]];do
#  if [[ "${string:$ini:1}" = "${string:$last-1:1}" ]];then
#    ini=$(( $ini+1 ))
#    last=$(( $last-1 ))
#  else
#    echo "false"
#    exit
#  fi
#done
#echo "true"

#Q12: Create a Backup of a File.Write a Bash script that takes a filename as input and creates a backup of that file by appending the current date to the filename.
#echo "Please provide the filename"
#read filename
#cp $filename "$filename"-"$( date -I)"

#Q13: Find the Number of Occurrences of a Word in a File
#echo "Please enter the filename"
#read filename
#echo "Please enter the word"
#read word
#echo $( cat $filename |grep -o $word |wc -l )

#Q14. Calculate Factorial of a Number
#read -p "Please enter the number: " num
#fact=1
#until [[ $num -eq 0 ]];do
#  fact=$(( $num*$fact ))
#  num=$(( $num -1 ))
#done
#echo "The factorial is: "$fact

#Q15. Remove Empty Directories
#read -p "Please provide path to directory to check: " dir
#cd $dir
#find . -type d -empty |xargs rm -rf

