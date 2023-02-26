import json

file = open('en_us.json')

data = json.load(file)

java = 'public enum ItemMapper {'

for line in data:
    if (line.startswith('item.minecraft.') or line.startswith('block.minecraft.')) and len(line.split('.')) == 3:
        name = line.split('.')[2].upper()
        value = data[line]
        if line.startswith('block.minecraft.') and line.replace('block.minecraft.', 'item.minecraft.') not in data:
            if not (name + '("' + name + '", "' + value + '"),') in java:
                java += '\n   ' + name + '("' + name + '", "' + value + '"),'
java = java[:-1] + ';'

java += '\n'
java += '\n   String name, value;'
java += '\n'
java += '\n   private ItemMapper(String name, String value) {'
java += '\n      this.name = name;'
java += '\n      this.value = value;'
java += '\n   }'
java += '\n}'
file.close()

with open('ItemMapper.java', 'w') as f:
    f.write(java)
f.close()
