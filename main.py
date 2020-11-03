import sys
import glob

walk_dir = sys.argv[1]

condition = sys.argv[2]
replace = sys.argv[3]
value = sys.argv[4]

print('walk_dir = ' + walk_dir)
print()

for filename in glob.iglob(walk_dir + '**/**', recursive=True):
    if filename.find(".csproj") > 0 and filename[-1] == "j":
        print(filename)

        my_file = open(filename, "r")
        lines_of_file = my_file.readlines()

        for index, line in enumerate(lines_of_file):
            if line.find(condition) > 0:
                print(line)
                lines_of_file[index] = line.replace(
                    replace, value)

        my_file = open(filename, "w")
        my_file.writelines(lines_of_file)
