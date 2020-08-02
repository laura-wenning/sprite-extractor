files="$(find *png)"
# for file in $files; do
#   name="${file//_face.png/''}"
#   name="${name//_character.png/''}"
#   echo $name
#   python3 extractor.py "$file" "$name" $1
# done

echo $files
echo $@
./sprite_controller.py $@ $files