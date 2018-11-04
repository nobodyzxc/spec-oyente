type oyente >/dev/null 2>&1 || { echo >&2 "oyente.py should be aliasing as oyente"; exit 1; }
for i in ./*.sol ;do echo "processing $i"; oyente -cfg -p -s $i 2> ${i%.*}.txt;done
